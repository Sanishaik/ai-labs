# Day 9 – AI Agent Security, Testing and Capstone 2

## Overview

Day 9 focuses on improving the reliability and safety of AI-powered agents through security analysis, adversarial testing, evaluation, and an invoice validation and approval workflow.

The work builds on the previous day's invoice-processing project and adds stronger validation, exception handling, approval controls, and audit logging.

## Learning Objectives

- Understand potential security gaps in AI-powered agents.
- Identify and test malicious or incorrect invoice inputs.
- Validate agent behaviour using automated tests.
- Evaluate the agent's reliability and safety.
- Implement an approval gate for invoice processing.
- Maintain audit records for approval decisions.
- Understand production-readiness requirements.

## Task 1 – Security Gap Analysis

**Objective:** Review the existing invoice-processing agent and identify potential gaps and risks.

The gap analysis focuses on areas that could affect the reliability, security, and correctness of invoice processing.

Key areas considered include:

- Incorrect or missing invoice information.
- Vendor and purchase order mismatches.
- Duplicate invoice submissions.
- Unusually high invoice amounts.
- Invalid input formats.
- Prompt injection and untrusted input.
- Approval and audit controls.

**Documentation:** `gaps.md`

## Task 2 – Adversarial Testing

**Objective:** Test the invoice-processing workflow against 10 potentially harmful or incorrect inputs.

The attack scenarios include:

1. Prompt injection.
2. Purchase order amount differs by ₹1.
3. Nonexistent purchase order.
4. Duplicate invoice.
5. Extremely large invoice amount (₹99,99,99,999).
6. Due date earlier than invoice date.
7. Invalid 14-character GSTIN.
8. Vendor mismatch.
9. Empty invoice file.
10. Invoice total does not match the line-item sum.

**Expected safe behaviour:**

- Invalid invoices must be identified as exceptions.
- Each exception must include a reason.
- Exception invoices must not be posted.
- Every decision must be recorded in the audit log.

**Test file:** `tests/test_attacks.py`

**Recorded result:** 10 out of 10 attack tests passed.

## Task 3 – Agent Evaluation

**Objective:** Evaluate the agent's behaviour using the testing results and documented findings.

The evaluation focuses on:

- Correct identification of clean invoices.
- Detection of invalid or suspicious invoice data.
- Safe handling of adversarial inputs.
- Correct exception reporting.
- Prevention of unintended posting.
- Audit-log recording.

**Documentation:** `eval.md`

The evaluation helps identify areas that need further improvement before the agent can be considered for production use.

## Task 4 – Capstone 2: Invoice Validation and Approval Agent

**Objective:** Complete an invoice validation and approval workflow using the Model Context Protocol (MCP).

### Project Structure

```text
task-4/
└── capstone-2/
    ├── README.md
    ├── data/
    │   └── po_list.csv
    ├── invoices/
    │   ├── invoice1.json
    │   ├── invoice2.json
    │   ├── invoice3.json
    │   ├── invoice4.json
    │   └── invoice5.json
    ├── logs/
    │   └── audit.log
    ├── po-mcp/
    │   ├── server.py
    │   ├── test_mcp_validation.py
    │   └── test_approval.py
    └── results/
        ├── approval_records.json
        ├── clean_invoice_summary.json
        └── exceptions.json
```

### MCP Tools

The MCP server provides these tools:

- `get_po` – retrieves purchase order information.
- `list_late_pos` – lists late purchase orders.
- `check_invoice_po` – checks invoice and purchase order details.
- `validate_invoice` – validates invoice information.
- `approve_invoice` – records approval or rejection decisions for clean invoices.

### Validation Workflow

The agent checks:

- Required invoice fields.
- Purchase order existence.
- Vendor matching.
- Invoice amount matching.

### Approval Gate

- Only CLEAN invoices can proceed to approval.
- EXCEPTION invoices are blocked.
- Approval decisions are recorded with approver details and comments.
- Blocked attempts are recorded in the audit log.

### Test Results

Five sample invoices were tested:

| Result | Count |
|---|---:|
| CLEAN | 3 |
| EXCEPTION | 2 |
| Total | 5 |

The approval workflow was also tested. INV004 was blocked because of a vendor mismatch.

### Audit and Safety

The project maintains:

- `approval_records.json` for approval decisions.
- `exceptions.json` for invoice exceptions.
- `clean_invoice_summary.json` for clean invoice results.
- `audit.log` for validation and approval activity.

The approval record uses `posted: false`. This project does not perform real financial posting or payment.

## Important Production Readiness Considerations

Before using this type of agent in a real business environment, additional controls are required:

1. Authentication to verify the identity of approvers.
2. Role-based access control (RBAC).
3. Secure and tamper-resistant audit storage.
4. Duplicate approval prevention.
5. Safe integration with financial systems.
6. Additional security and integration testing.
7. Monitoring, alerting, and backup procedures.

## Day 9 Deliverables

- Security gap analysis.
- Adversarial test cases.
- Agent evaluation documentation.
- Invoice validation and approval MCP project.
- Approval records and audit log.
- Day 9 lab log.

## Final Summary

Day 9 strengthened the invoice-processing agent through security analysis, adversarial testing, evaluation, and an approval workflow.

The project demonstrates how an AI-powered invoice agent can validate purchase order information, identify exceptions, prevent unsafe approvals, and maintain an audit trail.

This is a learning prototype and is not connected to a real financial posting system.
