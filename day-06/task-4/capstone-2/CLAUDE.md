# Invoice-to-Insight - Project Instructions

## Project Purpose
Build an AI-assisted invoice extraction and purchase order validation workflow.

## Important Data Rules
- Current invoice JSON files are synthetic practice examples, not trainer-provided samples.
- The current PO CSV is a provisional copy of the Day 0 dataset; confirm it against the trainer's Capstone 2 data.
- Use trainer-provided samples when they become available.
- Never use real client or confidential business data.
- Do not silently modify or correct source data.
- Keep original source files unchanged.

## Development Rules
- Read spec.md before implementing project changes.
- Explain the plan before making significant changes.
- Do not install new packages without approval.
- Use clear, beginner-friendly explanations.
- Write tests for implemented functionality and run them after changes.
- Keep project files inside this capstone-2 folder.

## AI and Validation Rules
- Use consistent, structured JSON for extracted invoice information.
- Flag missing, unclear, or inconsistent values for human review.
- Validate invoice details against the supplied PO data.
- Do not silently assume that an invoice is correct.

## Security and Approval
- Follow least-privilege principles.
- Do not connect to or post data to SAP, ERP, email, or external systems.
- Require explicit human approval before any simulated posting action.
- Record relevant actions and results in an audit log.

## Project Scope
This project prepares invoice extraction results, PO validation results, summaries, and exceptions for review. It does not perform actual financial postings.
