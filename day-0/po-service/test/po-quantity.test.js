// Automated tests for PO quantity validation (CREATE only) and regression checks
// for the existing amount rule and the isLate calculation.
// Run with: npm test   (from the po-service folder; no cds watch needed)
import { describe, it, before, after } from 'node:test';
import assert from 'node:assert/strict';
import cds from '@sap/cds';

const BASE = '/odata/v4/po/PurchaseOrders';
let server;
let base;

// POST a new PO and return { status, body }
async function createPO(payload) {
  const res = await fetch(base + BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
    body: JSON.stringify(payload),
  });
  const body = await res.json().catch(() => ({}));
  return { status: res.status, body };
}

// GET one PO by key and return { status, body }
async function getPO(poNumber) {
  const res = await fetch(`${base}${BASE}('${poNumber}')`, {
    headers: { Accept: 'application/json' },
  });
  const body = await res.json().catch(() => ({}));
  return { status: res.status, body };
}

// Base payload; each test overrides only the fields it cares about
function po(poNumber, overrides = {}) {
  return {
    poNumber,
    vendor_ID: 'V001',
    dueDate: '2026-12-15',
    orderedQty: 10,
    deliveredQty: 0,
    amount: 1000,
    ...overrides,
  };
}

before(async () => {
  // In-memory SQLite, seed CSVs loaded, random free port
  cds.env.requires.db = { kind: 'sqlite', credentials: { url: ':memory:' } };
  server = await cds.server({ port: 0, in_memory: true });
  base = `http://localhost:${server.address().port}`;
});

after(async () => {
  await new Promise((resolve) => server.close(resolve));
  await cds.shutdown?.();
});

describe('PO quantity validation (CREATE)', () => {
  it('accepts valid quantities (ordered 10, delivered 5)', async () => {
    const r = await createPO(po('QV0001', { orderedQty: 10, deliveredQty: 5 }));
    assert.equal(r.status, 201);
  });

  it('accepts equal quantities (ordered 10, delivered 10)', async () => {
    const r = await createPO(po('QV0002', { orderedQty: 10, deliveredQty: 10 }));
    assert.equal(r.status, 201);
  });

  it('rejects a negative ordered quantity with 400', async () => {
    const r = await createPO(po('QV0003', { orderedQty: -1, deliveredQty: 0 }));
    assert.equal(r.status, 400);
    assert.match(r.body.error.message, /Ordered quantity must not be negative/);
  });

  it('rejects a negative delivered quantity with 400', async () => {
    const r = await createPO(po('QV0004', { orderedQty: 10, deliveredQty: -1 }));
    assert.equal(r.status, 400);
    assert.match(r.body.error.message, /Delivered quantity must not be negative/);
  });

  it('rejects delivered quantity greater than ordered with 400', async () => {
    const r = await createPO(po('QV0005', { orderedQty: 10, deliveredQty: 11 }));
    assert.equal(r.status, 400);
    assert.match(r.body.error.message, /Delivered quantity must not exceed ordered quantity/);
  });

  it('does not persist a rejected PO', async () => {
    const r = await getPO('QV0003');
    assert.equal(r.status, 404);
  });
});

describe('existing behaviour is preserved', () => {
  it('still rejects amount <= 0 with 400', async () => {
    const r = await createPO(po('QV0006', { amount: 0 }));
    assert.equal(r.status, 400);
    assert.equal(r.body.error.message, 'Amount must be greater than 0.');
  });

  it('computes isLate = true for a past-due, under-delivered seed PO', async () => {
    // Seed 4500014: due 2026-10-05, delivered 0 of 50
    const r = await getPO('4500014');
    assert.equal(r.status, 200);
    assert.equal(r.body.isLate, true);
  });

  it('computes isLate = false when fully delivered (boundary: not <)', async () => {
    // Seed 4500013: due 2026-10-20, delivered 100 of 100
    const r = await getPO('4500013');
    assert.equal(r.status, 200);
    assert.equal(r.body.isLate, false);
  });
});
