# Day 06 Task 2 – Purchase Order Quantity Validation

This submission adds one feature to the existing SAP CAP Purchase Order service: **quantity validation when creating a Purchase Order**. The feature was built with the workflow *Specification → Plan → Approve → Implement → Test → Commit*.

- **Application (source of truth):** `day-0/po-service/`
- **Committed change:** `71cbe30` on `main` (`Add purchase order quantity validation with tests`), pushed to `origin/main`
- **Plan:** [`plan.md`](plan.md) · **Specification:** [`spec.md`](spec.md)

## Folder contents

| Path | Purpose |
|---|---|
| `spec.md` | Task 2 specification (unchanged) |
| `plan.md` | Approved implementation plan and completed steps |
| `files/po-service.js` | Service logic with the new quantity rule |
| `files/po-quantity.test.js` | Automated tests |
| `files/po.http` | Manual REST requests, including new requests 7–10 |
| `files/package.json` | Adds the `npm test` script |
| `files/CLAUDE.md` | Project guidance, updated for the new rule and test command |
| `screenshots/` | Evidence screenshots (to be added) |

The files in `files/` are byte-identical copies of the committed files in `day-0/po-service/`.

## Feature

When a Purchase Order is **created** (`POST /odata/v4/po/PurchaseOrders`), the service now checks the quantities:

| Rule | Condition | Error message (HTTP 400) |
|---|---|---|
| 1 | `orderedQty < 0` | `Ordered quantity must not be negative.` |
| 2 | `deliveredQty < 0` | `Delivered quantity must not be negative.` |
| 3 | `deliveredQty > orderedQty` | `Delivered quantity must not exceed ordered quantity.` |

- The rules apply to **CREATE only**. Updates and reads are not affected.
- Each check runs only when its field is present, the same way the existing amount rule works.
- Rejected requests are not saved.

## Implementation

- **`srv/po-service.js`**: a new `this.before('CREATE', PurchaseOrders, …)` handler (Rule 2) sits beside the existing amount rule. The three checks run in the order above, and the first failing check rejects the request with `req.reject(400, message)`.
- **Preserved, unchanged:** the amount rule (`amount <= 0` → 400), the `after READ` calculation of `isLate`, the OData service surface, the data model, and the seed data. The only edit near existing code is a comment label, changed from "Rule 2" to "Rule 3" for the `isLate` rule.
- **No schema change.** `orderedQty` and `deliveredQty` are already `Integer` fields in `db/schema.cds`.
- **No new dependencies.**

## Automated tests

Tests live in `test/po-quantity.test.js` and use the Node.js built-in test runner.

```bash
cd day-0/po-service
npm test          # runs: node --test
```

The tests start the real HTTP service in-process, with an in-memory SQLite database loaded with the seed data. They send real HTTP requests and do not need `cds watch`.

| Test | Expected |
|---|---|
| Valid quantities (ordered 10, delivered 5) | 201 Created |
| Equal quantities (ordered 10, delivered 10) | 201 Created |
| Negative ordered quantity (-1) | 400, ordered-quantity message |
| Negative delivered quantity (-1) | 400, delivered-quantity message |
| Delivered greater than ordered (11 > 10) | 400, exceed-ordered message |
| Rejected PO is not persisted | 404 on GET |
| Amount 0 still rejected (regression) | 400, `Amount must be greater than 0.` |
| `isLate` true for past-due, under-delivered seed PO 4500014 (regression) | `isLate: true` |
| `isLate` false for fully delivered seed PO 4500013 (regression) | `isLate: false` |

## Verification results

- `npm test` (after the handler was added): **8 tests, 8 passed, 0 failed, exit code 0.**
- The copies in `files/` were compared with the originals using `cmp`: **all five identical.**
- **Not performed:** the initial red-test step. The tests were not run before the quantity handler was implemented, so it has not been verified that they fail without the rule.
- After implementation, `npm test` passed all 8 tests with 0 failures.

Manual checks with `test/po.http` (requests 7–10) are documented in the file and are not part of the automated run. Request 7 creates a record, so it should be run once.

## Notes

- Test helper: `cds.test` from `@sap/cds` is not available in this project, so the tests call `cds.server({ port: 0, in_memory: true })` instead. This is documented in `plan.md`.
- Only quantity fields that are present are validated. A request that omits `orderedQty` or `deliveredQty` is not rejected by these rules.
- `isLate` cannot be used in `$filter` or `$orderby` because it is a virtual field; this is unchanged.
