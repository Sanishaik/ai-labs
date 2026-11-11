# Day 8 Lab Log

**Date:** 2026-11-11

## Answer: Difference Between Skill and Agent

A **skill** is an individual, reusable action that performs a specific task, such as retrieving a purchase order, checking whether a PO is late, or validating an invoice. In my Day 8 project, the MCP server exposed these individual functions as tools.

An **agent** is the workflow layer that uses these skills and tools to complete a larger task. In my work, I designed an agent workflow and implemented an invoice-validation process that used MCP tools to check five invoices against purchase order data, identify mismatches, separate clean invoices from exceptions, and generate summary reports and audit logs.

**In simple words:** A skill performs one specific action, whereas an agent decides how to use multiple skills and tools to complete the overall business workflow.

## Evidence from My Day 8 Work

| Category | Example from my work | File | What it does |
|---|---|---|---|
| Skill (MCP Tool) | `get_po` | `po-mcp/server.py` | Retrieves purchase order details. |
| Skill (MCP Tool) | `list_late_pos` | `po-mcp/server.py` | Retrieves purchase orders that are late. |
| Skill (MCP Tool) | `check_invoice_po` | `po-mcp/server.py` | Checks invoice details against purchase order information. |
| Skill (MCP Tool) | `validate_invoice` | `po-mcp/server.py` | Validates an invoice and identifies mismatches. |
| Agent / Workflow | Invoice validation workflow | `capstone-2` | Uses the validation tools to process multiple invoices and organize the results. |
| Agent / Workflow | Exception handling and audit logging | `logs/audit.log` | Records invoice validation results. |
| Agent / Workflow | Result generation | `results/` | Produces clean invoice summaries and exception reports. |

## Results from My Capstone 2 Project

| Check | Actual Result | Evidence File |
|---|---|---|
| Total invoices processed | 5 | `invoices/` |
| Clean invoices | 3 (INV001, INV002, INV003) | `results/clean_invoice_summary.json` |
| Exception invoices | 2 (INV004, INV005) | `results/exceptions.json` |
| INV004 exception | Vendor mismatch | `results/exceptions.json` |
| INV005 exception | Amount mismatch | `results/exceptions.json` |
| Audit logging | Validation results recorded | `logs/audit.log` |
| Actual SAP financial posting | Not performed | Capstone 2 validation scope |

## What I Learned

I learned that individual MCP tools act as reusable skills for performing specific operations, while an agent or workflow combines these tools to complete a business process. I also gained practical experience in Python, MCP server development, purchase order retrieval, invoice validation, exception handling, JSON and CSV processing, and audit logging.

## Proof

Successfully completed the Day 8 tasks and pushed the Day 8 folder, including the lab log and Capstone 2 project, to my GitHub repository `Sanishaik/ai-labs` on the `main` branch.
