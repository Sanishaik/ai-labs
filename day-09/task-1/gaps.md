# Day 9 - Task 1: Guardrail Audit

## Project
Day 8 Capstone 2 - Invoice Validation MCP Server

## 1. Human in the Loop

Status: GAP

- The current system validates invoices automatically.
- There is no human approval or rejection step before an invoice can proceed.
- An approval gate is required before any future financial posting.

## 2. Least Privilege

Status: PARTIALLY IMPLEMENTED

- The MCP server provides read-only purchase order lookup and invoice validation tools.
- No invoice posting or payment tool is present in the inspected server.py.
- Explicit user roles, authentication, and permission checks are not visible in the inspected code.
- Future tools must receive only the permissions required for their specific task.

## 3. Audit Trail

Status: PARTIALLY IMPLEMENTED

- The existing audit.log records timestamps, invoice numbers, validation statuses, and PO numbers.
- It records five invoices: three CLEAN and two EXCEPTION.
- Exception reasons are not recorded in the existing audit.log.
- Human approval details and the identity of the approver are not recorded.
- The server also writes application logs to a separate server.log file.

## 4. Boss and Workers

Status: GAP

- The current project has one MCP server with individual tools.
- No separate planning agent or worker agents are implemented.
- A future design could use one coordinator to assign validation tasks to specialised workers.
- Each worker should perform only its assigned responsibility.

## Summary of Findings

| Guardrail | Result |
|---|---|
| Human in the Loop | GAP |
| Least Privilege | PARTIALLY IMPLEMENTED |
| Audit Trail | PARTIALLY IMPLEMENTED |
| Boss and Workers | GAP |

## Conclusion

The current Capstone 2 project validates invoices and separates clean invoices from exceptions. It does not implement human approval or a boss-and-workers agent structure. Audit logging exists but needs more details, including exception reasons and approval records. Access permissions also need to be defined and verified before production use.

No financial posting capability was found in the inspected MCP server.
