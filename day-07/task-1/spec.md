# Day 7 Task 1 – Codex Round 2

## GOAL
Implement Purchase Order Quantity Validation in the existing SAP CAP Node.js Purchase Order service.

## RULES
1. orderedQty must not be negative.
2. deliveredQty must not be negative.
3. deliveredQty must not exceed orderedQty.
4. Reject invalid CREATE requests with HTTP 400 and clear error messages.
5. Preserve the existing amount validation and isLate calculation.
6. Apply validation to CREATE requests only.

## DONE WHEN
1. Valid quantities are accepted.
2. Equal ordered and delivered quantities are accepted.
3. Negative ordered quantity is rejected.
4. Negative delivered quantity is rejected.
5. Delivered quantity greater than ordered quantity is rejected.
6. Rejected Purchase Orders are not persisted.
7. Existing amount validation and isLate tests still pass.
8. All automated tests pass.

## DON'T
- Do not add new packages or dependencies.
- Do not change the database schema or OData service definition.
- Do not modify unrelated functionality.
- Do not remove or weaken existing tests.
