# Invoice-to-Insight
## Final Specification — Day 7 Capstone 2

### 1. Objective
Build an AI-assisted invoice extraction workflow that converts invoice data into structured JSON, tests extraction accuracy, and checks purchase orders through a custom MCP server.

### 2. Input Data
- Synthetic invoice samples: invoice1.json and invoice2.json.
- Purchase order data: Day 6 Capstone 2 PO CSV.
- Only training sample data will be used.

### 3. Invoice Extraction
Extract the following fields:
- invoiceNumber
- invoiceDate
- vendorName
- vendorId
- poNumber
- currency
- subtotal
- taxAmount
- totalAmount
- lineItems

Missing fields must be represented as null or an empty array where appropriate. Never invent missing information.

### 4. Extraction Output
Each invoice must produce a structured JSON file in the extracted/ folder.

### 5. Automated Tests
Tests must verify:
- Required invoice fields are extracted.
- Numeric amounts retain numeric types.
- Missing fields are handled safely.
- Invalid invoice input produces a clear error.
- Extracted JSON is valid and readable.

### 6. MCP Integration
Extend the existing PO MCP server with invoice-related PO checking.
The server must:
- Retrieve a PO using its PO number.
- Check whether a PO exists.
- Compare invoice vendor information with PO vendor information.
- Return a clear result for valid and invalid PO references.

### 7. Safety
- Do not modify source invoice files.
- Do not invent missing invoice values.
- Do not connect to external financial or ERP systems.
- Do not perform actual financial postings.
- Keep human approval for any future simulated posting.

### 8. Deliverables
- Final spec.md
- Source invoice samples
- Invoice extraction Python implementation
- Extracted JSON files
- Automated extraction tests
- Updated PO MCP server
- Test proof screenshots
- README.md

### 9. Completion Criteria
Task 3 is complete when invoice extraction tests pass, structured JSON outputs are generated, and PO checking is available through the MCP server.
