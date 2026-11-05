# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- Install: `npm install`
- Dev server (watch mode, SQLite, auto-reloads on change): `npx cds watch` → `http://localhost:4004`
- Run without watch: `npm start` (runs `cds-serve`)
- Tests: there is no test runner or lint script. `test/po.http` holds manual REST requests; run them with `cds watch` already running (e.g. VS Code REST Client). To exercise one case, send only that request block.

## Architecture

This is a SAP CAP (CDS) service, `package.json` `"type": "module"`, with no UI yet (`app/` is empty). The behaviour is spread across four files:

- **Data model** `db/schema.cds` (namespace `resoftwa.po`): `Vendors` and `PurchaseOrders`. `PurchaseOrders.vendor` is an association, so the foreign key column is `vendor_ID`. `isLate` is declared `virtual`, so it is not stored.
- **Service surface** `srv/po-service.cds`: `POService` at `/odata/v4/po`. It exposes only projections of the two entities. Anything not projected here is not reachable over OData, even if it exists in the schema.
- **Business rules** `srv/po-service.js`, registered as handlers on the service:
  - `before CREATE` on `PurchaseOrders` rejects `amount <= 0` with 400. It only checks when `amount` is present in the payload.
  - `after READ` computes `isLate` per row in memory: `dueDate` before today (UTC `YYYY-MM-DD` string comparison) and `deliveredQty < orderedQty`.
- **Seed data** `db/data/resoftwa.po-Vendors.csv` and `resoftwa.po-PurchaseOrders.csv`. CAP loads these by its `<namespace>-<entity>.csv` naming convention. The root-level `po_list.csv` and `vendors.csv` are not loaded by the app. `po_list.csv` has an `isLate` column that the model does not define.

## Gotchas

- Because `isLate` is virtual and computed after READ, it cannot be used in `$filter` or `$orderby`. Filter on `dueDate` and `deliveredQty`/`orderedQty` instead, as `test/po.http` request 2 does. `readme.md` section 9 shows `$filter=isLate eq true`, which will not work.
- The `isLate` date boundary is evaluated against the current UTC date, so results change at UTC midnight.
