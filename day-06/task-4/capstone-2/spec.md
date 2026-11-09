# Invoice-to-Insight
## Initial Project Specification — Day 6

## 1. Project Overview
Invoice-to-Insight is an AI-assisted workflow that extracts information from supplier invoices, validates it against purchase order (PO) data, and prepares results for human review.

## 2. Objectives
- Extract invoice information into structured JSON.
- Validate invoice details against purchase orders.
- Identify clean invoices and exceptions.
- Prepare a posting summary for valid invoices.
- Require human approval before simulated posting.
- Maintain an audit log of important actions.

## 3. Input Data
- The current invoice JSON files are synthetic practice examples, not official trainer samples.
- The PO list in data/ is a provisional Day 0 copy and must be confirmed against the trainer's Capstone 2 data.
- Replace or verify both datasets against official trainer samples when available.

Only training sample data will be used. Real client data is not permitted.

## 4. Proposed Workflow
1. Read a sample invoice.
2. Extract invoice fields into structured JSON.
3. Validate the extracted information.
4. Use a custom MCP server to check invoice details against PO data.
5. Separate clean invoices from exceptions.
6. Prepare a summary for clean invoices.
7. Request human approval before any simulated posting.
8. Record actions and results in an audit log.

## 5. Invoice Extraction Fields
The initial extraction schema will include:
- Invoice number
- Invoice date
- Vendor name and vendor ID
- Purchase order number
- Currency
- Subtotal
- Tax amount
- Total amount
- Line items: description, quantity, unit price, and line total

Missing or unclear fields must be flagged for review.

## 6. Initial Validation Rules
- Check whether the referenced PO exists.
- Check whether the invoice vendor matches the PO vendor.
- Check invoice quantities against ordered quantities.
- Check whether invoice totals are consistent.
- Flag missing, unclear, or inconsistent information.
- Do not silently change source data or assume a value.

Detailed validation rules will be finalized during Day 7.

## 7. Expected Outputs
- Extracted invoice JSON.
- PO validation results.
- Clean-invoice posting summary.
- Exception list for human review.
- Audit log of relevant actions.

## 8. Security and Safety
- Use only trainer-provided sample data.
- Follow least-privilege access principles.
- Do not connect to external financial or ERP systems.
- Do not perform actual financial postings.
- Require explicit human approval for simulated posting.
- Test against prompt injection and unsafe instructions.

## 9. Development Plan
- Day 6: Set up the project, collect training data, create project instructions, and draft this specification.
- Day 7: Finalize the specification, implement invoice extraction, tests, and PO checking through a custom MCP server.
- Day 8: Implement validation results, clean-invoice summaries, and exception handling.
- Day 9: Add security tests, approval gate, audit logging, evaluation, and documentation.
- Day 10: Demonstrate the completed capstone.

## 10. Status
This is the initial Day 6 draft. Requirements and validation details may be refined during implementation.
