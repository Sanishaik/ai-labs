# Day 9 – Lab Log

## 1. Objective

The objective of Day 9 was to improve the security, reliability, and safety of an AI-powered invoice-processing agent.

The work covered security gap analysis, adversarial testing, agent evaluation, and completion of the invoice validation and approval workflow.

## 2. Work Completed

### Task 1 – Security Gap Analysis

Reviewed the invoice-processing workflow and documented potential security and validation gaps.

The review considered incorrect invoice details, purchase order mismatches, duplicate submissions, invalid inputs, and approval controls.

**Deliverable:** `gaps.md`

### Task 2 – Adversarial Testing

Created and executed 10 attack tests to check whether the invoice agent could safely handle incorrect or malicious inputs.

The tests covered prompt injection, amount mismatches, nonexistent purchase orders, duplicate invoices, unusually large amounts, invalid dates, invalid GSTIN, vendor mismatches, empty files, and line-item total mismatches.

**Result:** 10 out of 10 tests passed.

Invalid invoices were expected to be identified as exceptions with reasons, not posted, and recorded in the audit log.

**Deliverable:** `tests/test_attacks.py`

### Task 3 – Agent Evaluation

Documented the agent evaluation based on its validation behaviour, security tests, exception handling, and safe processing requirements.

The evaluation helps identify areas for improvement before production deployment.

**Deliverable:** `eval.md`

### Task 4 – Capstone 2: Invoice Validation and Approval Agent

Completed the invoice validation and approval workflow using MCP.

Implemented invoice validation, purchase order checks, an approval gate, and audit logging.

Five sample invoices were tested:

- 3 invoices identified as CLEAN.
- 2 invoices identified as EXCEPTION.
- INV004 approval attempt was blocked because of a vendor mismatch.
- A previous successful approval of INV001 was recorded.
- Approval records and audit logs were verified.
- No real financial posting was performed; records show `posted: false`.

**Project folder:** `day-09/task-4/capstone-2/`

## 3. Testing Summary

| Test Area | Result |
|---|---|
| Adversarial attack tests | 10/10 passed |
| Invoice validation | 3 CLEAN, 2 EXCEPTION |
| Approval gate | Tested |
| Vendor mismatch handling | Blocked correctly |
| Approval records | Verified |
| Audit log | Verified |
| Financial posting | Not performed |

## 4. Production Readiness Gaps

The project is a learning prototype. Before production deployment, the following improvements are required:

1. Authentication to verify approver identity.
2. Role-based access control for approval permissions.
3. Secure audit-log storage and tamper protection.
4. Duplicate approval prevention.
5. Safe financial-system integration.
6. More security and integration testing.
7. Monitoring, alerts, and backups.

## 5. Learning Outcomes

Through Day 9, I learned:

- How to identify security gaps in an AI agent.
- How to test an agent using adversarial inputs.
- How to evaluate validation and exception-handling behaviour.
- How MCP tools support invoice-processing workflows.
- How to implement an approval gate.
- How to maintain approval records and audit logs.
- Why authentication, authorization, and monitoring are important for production systems.

## 6. Proof of Completion

- Repository: `Sanishaik/ai-labs`
- Main branch: `main`
- Day 9 folder: `day-09/`
- Capstone 2 folder: `day-09/task-4/capstone-2/`
- Capstone 2 commit: `80030f2`
- Lab log commit: `1618a5f`
- GitHub push: Successfully completed.

## 7. Final Status

Day 9 project files and lab documentation have been pushed to GitHub.

The Capstone 2 video recording and two demo rehearsals remain to be completed and saved in OneDrive.

**Final note:** This project demonstrates a learning prototype. It does not perform real financial posting or payment.
