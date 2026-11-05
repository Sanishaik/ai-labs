// Service logic: rules that run around each request
import cds from '@sap/cds';

export default cds.service.impl(async function () {
  const { PurchaseOrders } = this.entities;
  const { SELECT } = cds.ql;

  // Rule 1: before creating a PO, reject amount <= 0
  this.before('CREATE', PurchaseOrders, (req) => {
    const amount = req.data.amount;
    // Only check when an amount is sent
    if (amount !== undefined && amount !== null && amount <= 0) {
      return req.reject(400, 'Amount must be greater than 0.');
    }
  });

  // Rule 2: before creating or updating a PO, check quantities.
  // On PATCH the body may hold only some fields, so a missing one is read
  // from the stored PO before the comparison.
  this.before(['CREATE', 'UPDATE'], PurchaseOrders, async (req) => {
    const { orderedQty, deliveredQty } = req.data;
    const hasOrdered = orderedQty !== undefined && orderedQty !== null;
    const hasDelivered = deliveredQty !== undefined && deliveredQty !== null;

    // Negative checks: only on values sent in this request
    if (hasOrdered && orderedQty < 0) {
      return req.reject(400, 'Ordered quantity must not be negative.');
    }
    if (hasDelivered && deliveredQty < 0) {
      return req.reject(400, 'Delivered quantity must not be negative.');
    }

    // Comparison needs both values. On UPDATE, fill a missing one from the stored PO.
    let ordered = orderedQty;
    let delivered = deliveredQty;
    if (req.event === 'UPDATE' && (!hasOrdered || !hasDelivered)) {
      const poNumber = req.data.poNumber ?? req.params[0]?.poNumber;
      const current = await SELECT.one
        .from(PurchaseOrders)
        .columns('orderedQty', 'deliveredQty')
        .where({ poNumber });
      if (current) {
        if (!hasOrdered) ordered = current.orderedQty;
        if (!hasDelivered) delivered = current.deliveredQty;
      }
    }
    if (ordered != null && delivered != null && delivered > ordered) {
      return req.reject(400, 'Delivered quantity must not exceed ordered quantity.');
    }
  });

  // Rule 3: after reading POs, set isLate (not stored in the database)
  this.after('READ', PurchaseOrders, (rows) => {
    // Today's date as YYYY-MM-DD (UTC), same format as dueDate
    const today = new Date().toISOString().slice(0, 10);
    // A read can return one row or a list of rows
    const list = Array.isArray(rows) ? rows : [rows];

    for (const row of list) {
      if (!row) continue;
      row.isLate = Boolean(
        row.dueDate && row.dueDate < today && row.deliveredQty < row.orderedQty
      );
    }
  });
});
