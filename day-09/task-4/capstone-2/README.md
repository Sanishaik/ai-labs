# Capstone 2 – Invoice Validation using MCP

## Project Overview
This project validates supplier invoices against purchase order data using a Python MCP server.

## Technologies Used
- Python
- Model Context Protocol (MCP)
- JSON
- CSV

## Project Structure
- invoices/ – Five sample invoice files
- data/ – Purchase order data
- po-mcp/server.py – MCP server
- po-mcp/test_mcp_validation.py – MCP client
- results/clean_invoice_summary.json – Clean invoice summary
- results/exceptions.json – Exception details
- logs/audit.log – Audit log

## Validation Checks
1. Required invoice fields
2. Purchase order existence
3. Vendor matching
4. Invoice amount matching

## Test Results
- Total invoices: 5
- Clean invoices: 3
- Exceptions: 2

INV001 – CLEAN
INV002 – CLEAN
INV003 – CLEAN
INV004 – EXCEPTION – Vendor mismatch
INV005 – EXCEPTION – Amount mismatch

## How to Run
Go to the po-mcp folder and run:

python test_mcp_validation.py

## Output Files
- clean_invoice_summary.json
- exceptions.json
- audit.log

## Conclusion
This project demonstrates automated invoice validation using MCP, exception identification, summary generation, and audit logging.

No real financial posting is performed.

## Human Approval Gate
- Only CLEAN invoices can be approved or rejected.
- EXCEPTION invoices are blocked.
- Approval decisions are recorded in `results/approval_records.json`.
- Successful and blocked attempts are recorded in `logs/audit.log`.
- Approval records include the approver, decision, timestamp and `posted: false`.
- No real financial posting or payment is performed.
- Approver identity is demo input; authentication and role-based access control are not implemented.

## Approval Workflow Test
- INV001: APPROVED by Demo Manager.
- INV004: BLOCKED due to vendor mismatch.
- No financial transaction was performed.

## Additional MCP Tool
- `approve_invoice` – Records approval or rejection for a CLEAN invoice.

## Approval Test Command
Run from the `po-mcp` directory using the project virtual environment:

`/home/user/projects/ai-labs/.venv/bin/python test_approval.py`
