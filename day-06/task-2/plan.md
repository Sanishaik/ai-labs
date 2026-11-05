# Day 06 Task 2 – Implementation Plan (Purchase Order Quantity Validation)

## 1. Context

The specification (`spec.md`) asks for three quantity rules on creating a Purchase Order in the existing CAP PO service (`day-0/po-service/`):

1. `orderedQty` must not be negative.
2. `deliveredQty` must not be negative.
3. `deliveredQty` must not exceed `orderedQty`.

Invalid requests must be rejected with HTTP 400 and a clear message. The existing amount validation, the `isLate` calculation, the OData service, the entities, and the seed data must be preserved. Automated tests must pass.

## 2. Approved plan (summary)

Plan mode was used. The plan was approved before any file was changed.

| Area | Decision |
|---|---|
| Location | Same application, `day-0/po-service/` (no new application) |
| Schema / service | No change to `db/schema.cds` or `srv/po-service.cds` |
| Business rule | Add a second `before CREATE` handler on `PurchaseOrders` in `srv/po-service.js`, mirroring the existing amount rule |
| Missing values | Checks run only for fields that are present (not `undefined`/`null`), consistent with the amount rule |
| Check order | Ordered negative → delivered negative → delivered > ordered |
| Tests | Node.js built-in test runner (`node --test`), no new dependencies |
| Test scope | Valid/equal quantities, the three rejections, rejected POs not persisted, amount regression, `isLate` regression |
| Docs | `CLAUDE.md` and `test/po.http` updated (approved as a separate step) |
| Submission | Copy the committed files into `day-06/task-2/files/` |

## 3. Files changed in the application

| File | Change |
|---|---|
| `srv/po-service.js` | New quantity `before CREATE` handler (Rule 2). The `isLate` rule is now labelled Rule 3; its code is unchanged. |
| `test/po-quantity.test.js` | New automated test file (8 tests) |
| `package.json` | Added `"test": "node --test"` only. `"start": "cds-serve"` is unchanged. |
| `CLAUDE.md` | Test instructions now point to `npm test`; one business-rule bullet added |
| `test/po.http` | Manual requests 7–10 added for the new rules |

Not changed: `db/`, `srv/po-service.cds`, seed data, `readme.md`, root-level CSV files.

## 4. Deviation from the approved plan

The approved plan assumed `cds.test` from `@sap/cds` would be available. In this project it is not installed (`@cap-js/cds-test` is absent), and the plan had ruled out adding new dependencies. The tests instead call `cds.server({ port: 0, in_memory: true })` from `@sap/cds`, which starts the real HTTP stack with an in-memory SQLite database and the seed data. The tests therefore still send real HTTP requests, without any new dependency.

## 5. Completed steps

1. Read the specification, `CLAUDE.md`, the model, the service, `package.json`, and the test folder.
2. Prepared and approved the implementation plan (plan mode).
3. Wrote `test/po-quantity.test.js`.
4. Added the `test` script to `package.json` (manual approval).
5. **Not performed:** the initial red-test step. `npm test` was not run before the quantity handler was implemented, so the expected failures for the rejection cases were not observed.
6. Added the quantity handler to `srv/po-service.js`.
7. Ran `npm test`: **8 tests, 8 passed, 0 failed**.
8. Updated `CLAUDE.md` and `test/po.http` (manual approval).
9. Re-ran `npm test`: **8 passed, 0 failed**, exit code 0.
10. Staged exactly five files and committed as `Add purchase order quantity validation with tests` (original hash `4d9211a`, rebased to `71cbe30`).
11. Rebased onto `origin/main` (no conflicts) and pushed to `origin/main`.
12. Copied the five committed files into `day-06/task-2/files/` and verified they are byte-identical to the originals.
13. Created this `plan.md`, `README.md`, and the `screenshots/` folder.

## 6. Remaining items

- Add evidence screenshots to `day-06/task-2/screenshots/` (folder created, empty).
- Review and commit the `day-06/task-2/` submission folder when ready (currently untracked; not committed).
