# Day 7 – Task 1: Codex vs Claude Code Comparison

## 1. Objective
Compare the Purchase Order Quantity Validation implementation using Codex and Claude Code.

## 2. Feature Specification
The feature requires:
- Reject negative ordered quantity.
- Reject negative delivered quantity.
- Reject delivered quantity greater than ordered quantity.
- Return HTTP 400 with clear error messages.
- Apply the new validation to CREATE requests.
- Preserve existing amount validation and isLate calculation.
- Do not add new packages or dependencies.

## 3. Claude Code Implementation

Reference: Day 6 – Task 2

Files:
- srv/po-service.js
- test/po-quantity.test.js
- package.json

Implemented:
- CREATE quantity validation.
- Negative ordered and delivered quantity checks.
- Delivered quantity limit validation.
- Existing amount validation preserved.
- Existing isLate calculation preserved.
- Automated tests for valid and invalid quantities.

Reported test result: 8 passed, 0 failed.

## 4. Codex Implementation

Workspace: codex-workspace/

File changed:
- srv/po-service.js

Implemented and preserved:
- CREATE quantity validation.
- Existing PATCH/UPDATE quantity validation.
- Existing amount validation.
- Existing isLate calculation.
- Clear HTTP 400 error messages.
- No new dependencies.
- No unrelated files modified.

Codex reviewed the existing implementation and separated CREATE and UPDATE validation while preserving existing behavior.

Test result: 10 passed, 0 failed across 3 suites.

## 5. Comparison

| Comparison Area | Claude Code | Codex |
|---|---|---|
| CREATE quantity validation | Yes | Yes |
| Negative ordered quantity | Yes | Yes |
| Negative delivered quantity | Yes | Yes |
| Delivered quantity limit | Yes | Yes |
| HTTP 400 error handling | Yes | Yes |
| PATCH validation | Not in Day 6 submission | Preserved |
| Amount validation | Yes | Preserved |
| isLate calculation | Yes | Preserved |
| Automated tests | 8 passed (reported) | 10 passed |
| New dependencies | None | None |

## 6. Diff Review

Service file observations:
- Both versions contain CREATE quantity validation.
- Codex uses a separate UPDATE handler to preserve PATCH validation.
- Codex uses SELECT to retrieve existing quantities when PATCH requests omit fields.
- Amount validation and isLate calculation remain intact.

Test file observations:
- The Codex workspace contains an additional PATCH test.
- The PATCH test verifies that delivered quantity greater than ordered quantity is rejected with HTTP 400.
- The test files differ in their cleanup logic.

Note: The Codex workspace was copied from the existing CAP project, which already contained PATCH validation and its test. Therefore, this comparison is not a completely independent implementation from an unmodified starting project.

## 7. Final Decision

Selected implementation: Codex version.

Reason:
The Codex workspace preserves existing functionality, including PATCH validation, and all 10 automated tests passed without adding dependencies.

## 8. Conclusion

Both Claude Code and Codex support the required Purchase Order quantity validation. Codex preserved the existing PATCH behavior, amount validation, and isLate calculation. The Codex workspace passed all 10 automated tests with zero failures.
