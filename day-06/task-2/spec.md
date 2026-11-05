
# DAY 06 – TASK 2
## Feature Development Using Claude Code

### 1. Task Overview
**Task:** A Feature, the Right Way

**Objective:** Add one new feature to the existing Phase 3 CAP Purchase Order application using the workflow:

Specification → Plan → Approve → Implement → Test → Commit

### 2. Project Details
- Project: CAP Purchase Order Service
- Technology: SAP CAP Node.js
- Service: POService
- OData Endpoint: `/odata/v4/po`
- Application Location: `day-0/po-service/`

### 3. Proposed Feature
**Purchase Order Quantity Validation**

Add validation to prevent invalid quantities when creating a Purchase Order.

### 4. Functional Requirements

1. Ordered quantity (`orderedQty`) must not be negative.
2. Delivered quantity (`deliveredQty`) must not be negative.
3. Delivered quantity (`deliveredQty`) must not exceed ordered quantity (`orderedQty`).

### 5. Expected Results

| Test Case | Input | Expected Result |
|---|---|---|
| Valid quantities | Ordered: 10, Delivered: 5 | Accept |
| Equal quantities | Ordered: 10, Delivered: 10 | Accept |
| Negative ordered quantity | Ordered: -1 | Reject |
| Negative delivered quantity | Delivered: -1 | Reject |
| Excess delivered quantity | Ordered: 10, Delivered: 11 | Reject |

### 6. Error Handling
Invalid quantities must be rejected with HTTP 400 and a clear error message.

### 7. Existing Functionality to Preserve
- Existing Purchase Order amount validation.
- Existing `isLate` calculation.
- Existing OData service.
- Existing database entities and sample data.

### 8. Testing Requirements
Create automated tests to verify:
- Valid quantity combinations.
- Negative ordered quantity rejection.
- Negative delivered quantity rejection.
- Delivered quantity greater than ordered quantity rejection.

All automated tests must pass.

### 9. Implementation Scope
- Apply the new validation to CREATE requests only.
- Do not modify unrelated functionality.
- Follow the existing CAP project structure.

### 10. Acceptance Criteria
- Specification reviewed in Claude Code Plan Mode.
- Implementation completed after plan approval.
- Automated tests added and passing.
- Changes committed to Git.

**Task 2 Status:** Specification preparation.
