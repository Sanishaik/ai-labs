# Day 9 – Lab Log

## Task 5: Proof & Log

### Work Completed

On Day 9, I completed Capstone 2, an Invoice Validation and Approval Workflow using the Model Context Protocol (MCP).

I tested five sample invoices. Three invoices passed validation successfully, while two were identified as exceptions due to vendor and amount mismatches.

I implemented a human approval gate to ensure that only CLEAN invoices could be approved or rejected. Invoices with validation errors were blocked. I also implemented audit logging to record approval decisions and blocked attempts.

I verified the approval records and audit log, updated the project README, and committed the project to Git.

### What Would Stop Me from Putting This into Production?

I would not deploy this project directly into production because:

1. Authentication is needed to verify the approver's identity.
2. Role-based access control is not implemented.
3. Audit logs need secure storage and protection against unauthorized changes.
4. Duplicate approval handling needs improvement.
5. Real financial posting requires additional safeguards and testing.
6. More security and integration tests are necessary.
7. Production monitoring, alerting, and backups must be established.

### Final Summary

Through this task, I learned how to build an invoice validation workflow using MCP, handle exceptions, implement human approval, and maintain an audit trail. I also understood the importance of security and testing before deploying an AI-assisted workflow.

This project is a learning prototype and is not intended for real financial transactions.

### Proof of Completion

- Project: Day 9 – Task 4 – Capstone 2
- Project folder: day-09/task-4/capstone-2/
- Git commit: 80030f2
- Validation: 3 CLEAN and 2 EXCEPTION invoices
- Approval gate and audit log: Tested successfully
- GitHub push: Not yet confirmed
