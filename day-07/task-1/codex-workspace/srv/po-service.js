// Service logic: rules that run around each request
import cds from '@sap/cds';

export default cds.service.impl(async function () {
  const { PurchaseOrders } = this.entities;

  // Rule 1: before creating a PO, reject amount <= 0
  this.before('CREATE', PurchaseOrders, (req) => {
    const amount = req.data.amount;
    // Only check when an amount is sent
    if (amount !== undefined && amount !== null && amount <= 0) {
      return req.reject(400, 'Amount must be greater than 0.');
    }
  });

  // Rule 2: before creating a PO, check quantities.
  this.before('CREATE', PurchaseOrders, (req) => {
    const { orderedQty, deliveredQty } = req.data;
    const hasOrdered = orderedQty !== undefined && orderedQty !== null;
    const hasDelivered = deliveredQty !== undefined && deliveredQty !== null;

    if (hasOrdered && orderedQty < 0) {
      return req.reject(400, 'Ordered quantity must not be negative.');
    }
    if (hasDelivered && deliveredQty < 0) {
      return req.reject(400, 'Delivered quantity must not be negative.');
    }
    if (hasOrdered && hasDelivered && deliveredQty > orderedQty) {
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
