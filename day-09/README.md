## Task 1: Guardrail Audit of Capstone 2

### Objective

The objective of this task was to review the Day 8 Capstone 2 Invoice Validation MCP Server and identify security and governance gaps using four important AI guardrails.

### What I Did

I reviewed the existing MCP server implementation (`server.py`) and audit log (`audit.log`) to check whether the invoice validation workflow followed these four guardrails:

1. **Human in the Loop**
   - Checked whether a human must review and approve or reject an invoice before any financial action.
   - Finding: GAP. The current workflow does not include a human approval or rejection step.

2. **Least Privilege**
   - Checked whether the MCP tools have only the permissions needed for their tasks.
   - Finding: PARTIALLY IMPLEMENTED. The server provides read-only PO lookup and invoice validation tools. No invoice posting or payment tool was found in the inspected implementation. Explicit role-based access and permission checks were not visible.

3. **Audit Trail**
   - Checked whether invoice decisions are recorded for tracking and review.
   - Finding: PARTIALLY IMPLEMENTED. The audit log records timestamps, invoice IDs, validation statuses, and PO numbers. However, exception reasons and human approver details are missing.

4. **Boss and Workers**
   - Checked whether the AI workflow separates planning and individual tasks among specialised agents.
   - Finding: GAP. The current implementation uses one MCP server with multiple tools and does not include a separate planner and specialised worker agents.

### Implementation Approach

- Inspected the MCP server tools and their responsibilities.
- Reviewed the existing invoice validation and audit logging implementation.
- Compared the implementation against all four guardrails.
- Identified missing controls and partially implemented controls.
- Documented each finding with its status and explanation.

### Deliverable

- `task-1/gaps.md` – Contains the complete guardrail audit and identified gaps.

### Outcome

Completed the guardrail audit and identified the improvements needed before considering the invoice validation workflow for production. The review confirmed that the inspected MCP server does not currently provide financial posting or payment functionality.