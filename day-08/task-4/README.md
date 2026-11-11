# Day 8 – Task 4
# Capstone 2: AI-Powered Invoice Validation using MCP

## 1. Project Overview

This capstone project demonstrates an automated supplier invoice validation system using Python and Model Context Protocol (MCP).

The system validates supplier invoice details against existing Purchase Order (PO) records. It identifies matching invoices, detects discrepancies, generates exception reports, and maintains an audit log of validation activities.

The main objective is to demonstrate how MCP tools can be used to automate business validation workflows and provide structured results for further review.

## 2. Project Objectives

- Build an MCP server for Purchase Order and invoice validation.
- Retrieve Purchase Order information from CSV data.
- Validate supplier invoice details against PO records.
- Identify clean invoices and invoices containing discrepancies.
- Generate a summary of successfully validated invoices.
- Generate an exception report for invoices requiring human review.
- Maintain an audit log of invoice validation results.

## 3. Technologies Used

- **Python:** Core programming language.
- **Model Context Protocol (MCP):** Enables communication between the MCP client and server tools.
- **JSON:** Stores supplier invoice details and validation results.
- **CSV:** Stores Purchase Order information.
- **Asyncio:** Supports asynchronous MCP client communication.

## 4. Project Folder Structure

```text
capstone-2/
│
├── data/
│   └── po_list.csv
│
├── invoices/
│   ├── invoice1.json
│   ├── invoice2.json
│   ├── invoice3.json
│   ├── invoice4.json
│   └── invoice5.json
│
├── logs/
│   └── audit.log
│
├── po-mcp/
│   ├── server.py
│   └── test_mcp_validation.py
│
├── results/
│   ├── clean_invoice_summary.json
│   └── exceptions.json
│
└── README.md
```

## 5. Main Components

### A. Purchase Order Data
The `data/po_list.csv` file contains Purchase Order details such as PO number, vendor ID, due date, ordered quantity, delivered quantity, amount, and late status.

### B. Supplier Invoices
The `invoices/` folder contains five sample supplier invoices in JSON format. These files are used to test the validation process.

### C. MCP Server
The `po-mcp/server.py` file implements the MCP server and exposes the following tools:

- `get_po` – Retrieves details of a Purchase Order.
- `list_late_pos` – Lists late Purchase Orders.
- `check_invoice_po` – Checks invoice and Purchase Order details.
- `validate_invoice` – Validates invoice information against Purchase Order records.

### D. MCP Client
The `po-mcp/test_mcp_validation.py` file connects to the MCP server, sends all five invoices for validation, and collects the results.

## 6. Invoice Validation Process

The system performs the following checks:

1. Checks whether required invoice fields are available.
2. Verifies whether the Purchase Order number exists.
3. Compares the invoice vendor ID with the PO vendor ID.
4. Compares the invoice amount with the PO amount.
5. Classifies each invoice as CLEAN or EXCEPTION.
6. Saves the validation results into JSON reports.
7. Generates an audit log containing invoice numbers, statuses, and PO numbers.

## 7. Test Scenarios and Results

Five sample invoices were tested using the MCP client.

| Invoice | Purchase Order | Validation Result |
|---|---|---|
| INV001 | 4500012 | CLEAN |
| INV002 | 4500014 | CLEAN |
| INV003 | 4500013 | CLEAN |
| INV004 | 4500015 | EXCEPTION – Vendor mismatch |
| INV005 | 4500017 | EXCEPTION – Amount mismatch |

### Final Validation Summary

- Total invoices tested: 5
- Successfully validated invoices: 3
- Invoices requiring review: 2
- Validation success rate: 60%

## 8. Generated Output Files

### clean_invoice_summary.json
Stores the total invoice count, clean invoice count, exception count, and details of successfully validated invoices.

### exceptions.json
Stores invoice details and the reasons for validation failures.

### audit.log
Maintains a record of invoice numbers, validation status, and corresponding Purchase Order numbers.

## 9. How to Execute the Project

Open the SAP Business Application Studio terminal.

Navigate to the MCP server directory:

```bash
cd /home/user/projects/ai-labs/day-08/task-4/capstone-2/po-mcp
```

Run the MCP validation client:

```bash
python test_mcp_validation.py
```

The client connects to the MCP server and validates all five sample invoices.

After successful execution, the generated summary and exception reports are saved in the `results/` folder.

## 10. Expected Output

```text
MCP connection successful!
INV001: CLEAN
INV002: CLEAN
INV003: CLEAN
INV004: EXCEPTION
INV005: EXCEPTION

Results saved successfully.
```

## 11. Important Notes and Limitations

- This project uses sample training data.
- No actual SAP financial posting is performed.
- Quantity and line-item calculations are not implemented because the sample invoice files do not contain invoice quantity and line-item details.
- Exception invoices require human review before further processing.
- The audit log records validation results and does not represent a financial posting record.

## 12. Conclusion

This project demonstrates how Python and Model Context Protocol can be used to build an automated invoice validation workflow.

The system successfully validates five sample invoices, identifies three clean invoices, detects two exceptions, generates structured JSON reports, and maintains an audit log.

Through this capstone project, practical experience was gained in MCP server development, tool integration, JSON and CSV processing, automated validation, exception handling, and audit logging.
