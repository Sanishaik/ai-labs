# Invoice-to-Insight

## Day 6 – Task 4: Capstone 2 Setup

### Project Overview

Invoice-to-Insight is a practice project designed to explore invoice processing, purchase order (PO) matching, validation, and exception handling using AI-assisted development.

The project will gradually include invoice data extraction, PO verification, validation checks, approval controls, and audit logging.

### Project Structure

```text
capstone-2/
├── data/
│   └── po_list.csv
├── invoices/
│   ├── invoice1.json
│   └── invoice2.json
├── README.md
└── spec.md
```

### Current Files

| File | Description |
|---|---|
| `data/po_list.csv` | Purchase order reference data |
| `invoices/invoice1.json` | Sample invoice JSON |
| `invoices/invoice2.json` | Sample invoice JSON |
| `spec.md` | Initial project specification |
| `README.md` | Project documentation |

### Data Information

- The current PO list is a provisional copy of the Day 0 dataset and must be verified against the official Capstone 2 PO data.
- The two invoice JSON files are synthetic practice examples, not trainer-provided invoices.
- The datasets will be updated when the official trainer samples are available.

### Development Plan

1. Finalize the project specification.
2. Extract invoice information into structured JSON.
3. Validate invoice details against purchase orders.
4. Identify mismatches and exceptions.
5. Generate clean-invoice summaries and exception reports.
6. Add security checks, human approval, and audit logging.
7. Test the workflow and document the results.

### Instructions

Shared development instructions are maintained in the global `CLAUDE.md` file outside this project folder.

### Summary

The Capstone 2 project folder has been created with the required invoice examples, PO reference data, initial project specification, and README documentation.

The project has been committed and successfully pushed to the `main` branch of the GitHub repository.

**Completion Status:** Completed

**Proof:** Project setup committed and pushed to the `main` branch of the `ai-labs` repository.

**Status:** Day 6 – Task 4 setup completed.
