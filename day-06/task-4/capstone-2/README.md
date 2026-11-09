# Invoice-to-Insight

## Project Overview
Invoice-to-Insight is an agentic AI project designed to extract invoice information, validate invoices against purchase orders, and prepare a review-ready summary.

## Project Objectives
- Extract structured data from trainer-provided sample invoices.
- Convert extracted invoice information into JSON.
- Validate invoice details against the Purchase Order (PO) list.
- Prepare posting summaries for clean invoices.
- Send exceptions to a human reviewer.
- Maintain audit logs and require human approval before posting.

## Project Structure
- invoices/ - Trainer-provided sample invoices.
- data/ - Purchase Order list and supporting data.
- CLAUDE.md - Project-specific instructions for Claude Code.
- spec.md - Project requirements and design.

## Safety Requirements
- Use trainer-provided sample invoices only.
- Never use real client data.
- Require human approval before any posting action.
- Follow least-privilege access principles.

## Development Plan
- Day 6: Project setup and initial specification.
- Day 7: Invoice extraction and PO validation.
- Day 8: Validation results, summaries, and exception handling.
- Day 9: Security tests, approval gate, audit log, evaluation, and documentation.
- Day 10: Final demonstration.

## Dataset Status

- `data/po_list.csv` is currently a provisional copy of the Day 0 PO dataset. Confirm it against the trainer's Capstone 2 data before using it.
- `invoices/invoice1.json` and `invoices/invoice2.json` contain synthetic practice examples for initial testing; they are not trainer-provided invoices.
- Replace or verify these examples against the trainer's official sample invoices when available.
