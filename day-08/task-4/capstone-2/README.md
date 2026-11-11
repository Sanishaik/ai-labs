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
