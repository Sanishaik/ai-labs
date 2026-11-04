# Day 05 – Agentic AI

**Training Program:** Resoftwa – Future-Ready Tech Training Program  
**Phase:** Phase 5 – Agentic AI  
**Day:** 05  
**Developer:** Shaik Saniya

## Overview

Day 05 focuses on Agentic AI and how AI models can use Python tools to perform tasks, make decisions, process information, and complete multi-step workflows.

During this phase, I learned how to build an AI agent using Claude, Python, and the Anthropic API. I also implemented tool calling, human approval, execution limits, audit logging, and SAP-focused prompt engineering.

## Learning Objectives

- Understand how AI agents work.
- Create Python functions as tools for an AI agent.
- Connect Claude AI with Python tools.
- Build an agent loop without using an agent framework.
- Implement safety guardrails and human approval.
- Maintain audit logs for tool execution.
- Create and test SAP ABAP troubleshooting prompts.

## Tasks Completed

### Task 1 – Tools as Functions

Created Python functions that allow the AI agent to interact with Purchase Order data.

**Tools implemented:**

| Function | Purpose |
|---|---|
| `list_open_pos()` | Lists open purchase orders |
| `get_po_status(po_number)` | Retrieves the status of a purchase order |
| `draft_email(vendor, text)` | Creates a vendor reminder email draft |
| `send_email(draft_id)` | Simulates sending an approved email |

**Files:**
- `pos.json`
- `tools.py`
- `task-1-test-results.md`

### Task 2 – Agent Loop Yourself

Built an agent loop using Python and Claude tool calling without using an agent framework.

**Workflow:**
1. Send the user request to Claude.
2. Claude decides which tool is required.
3. Python executes the requested tool.
4. The tool result is returned to Claude.
5. The agent continues until the task is completed or the step limit is reached.

**Result:**
- Identified 6 open purchase orders.
- Checked late purchase orders.
- Created 4 vendor reminder email drafts.
- No emails were sent.

**Files:**
- `agent.py`
- `agent-loop-results.md`

### Task 3 – Guardrails in Code

Implemented safety controls to make agent execution more reliable.

**Guardrails implemented:**
- Maximum 10 agent steps.
- Human approval before sending emails.
- Email sending is refused when the user enters `n`.
- Audit logging for tool calls.
- No email is sent without approval.

**Result:**
- 4 reminder drafts created.
- 4 email requests refused.
- 0 emails sent.
- 5 agent steps completed.
- 13 audit records generated.

**Files:**
- `agent.py`
- `audit.jsonl`
- `lab-log.md`

### Task 4 – Capstone 1: SAP Prompt Toolkit

Created a collection of five reusable AI prompts for SAP ABAP development and troubleshooting.

**Prompts developed:**

1. ABAP Code Explainer
2. ST22 Dump Analyzer
3. OData Error Analyzer
4. ABAP Performance Optimizer
5. Functional Specification to ABAP

**Testing:**
- Total prompts tested: 5
- Successful prompts: 5
- Failed prompts: 0
- Success rate: 100%

**Folder:** `capstone-1/`

**Important files:**
- `prompts/` – Five SAP prompts.
- `results/` – AI-generated results.
- `failure-notes/failure-notes.md` – Limitations and failure observations.
- `testing-results.md` – Prompt testing summary.
- `test_prompts.py` – Python script to test all prompts.
- `README.md` – Capstone documentation.
- `agent-loop-diagram.md` – Agent workflow diagram.

### Task 5 – Proof and Lab Log

Documented the work completed during Day 05 and created an agent loop diagram using Mermaid.

**Documentation includes:**
- Tasks completed.
- Python tool names.
- Agent workflow.
- Human approval mechanism.
- Execution limits.
- Audit logging.
- Learning outcomes.

**Files:**
- `lab-log.md`
- `capstone-1/agent-loop-diagram.md`

## Technologies Used

- Python
- Claude AI
- Anthropic API
- Claude Tool Calling
- JSON
- Git and GitHub
- Markdown
- SAP ABAP concepts
- OData concepts

## Project Structure

```text
day-05/
│
├── README.md
├── pos.json
├── tools.py
├── agent.py
├── audit.jsonl
├── agent-loop-results.md
├── lab-log.md
├── task-1-test-results.md
│
└── capstone-1/
    ├── README.md
    ├── agent-loop-diagram.md
    ├── test_prompts.py
    ├── testing-results.md
    │
    ├── prompts/
    │   ├── 01-abap-code-explainer.md
    │   ├── 02-st22-dump-analyzer.md
    │   ├── 03-odata-analyzer.md
    │   ├── 04-performance-optimizer.md
    │   └── 05-functional-spec-to-abap.md
    │
    ├── results/
    └── failure-notes/
        └── failure-notes.md
```

*Note: Additional backup and supporting files may also be present in the Day 05 folder.*

## Key Learnings

1. Learned how AI agents interact with external Python functions.
2. Understood Claude tool calling and agent loops.
3. Learned how an agent selects and executes tools.
4. Implemented human approval before sensitive actions.
5. Understood the importance of execution limits and audit logs.
6. Created reusable prompts for SAP ABAP troubleshooting.
7. Learned to test AI-generated responses and document limitations.
8. Practised Git commands to manage and publish project files.

## Important Safety Note

AI-generated SAP code, troubleshooting suggestions, and technical recommendations must be reviewed and validated in the appropriate SAP system before implementation.

The email functionality in this project is simulated. No real vendor emails are sent.

## GitHub Repository

**Repository:** https://github.com/Sanishaik/ai-labs

**Day 05:** https://github.com/Sanishaik/ai-labs/tree/main/day-05

**Capstone 1:** https://github.com/Sanishaik/ai-labs/tree/main/day-05/capstone-1

## Conclusion

Day 05 provided practical experience in building an AI agent, connecting Claude with Python tools, implementing safety guardrails, and developing SAP-focused prompt templates.

This work helped me understand the fundamentals of Agentic AI and how AI can support SAP development and troubleshooting workflows.

**Status:** Day 05 Tasks 1–5 completed and documented.  
