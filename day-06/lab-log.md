# Day 6 – Phase 5: Agentic AI & Apps
## Claude Code – Lab Log

### 1. Warm-up – Claude Code on Phase 1 ABAP Project

**Project:** `ZPO_OPEN_LIST`

- Opened my Phase 1 ABAP project.
- Used Claude Code and the `/init` command to analyse the project.
- Created a `CLAUDE.md` file containing project instructions.
- Learned how Claude Code reads project files and follows the instructions in `CLAUDE.md`.
- Learned to review the project and identify possible risks before making changes.

**Learning:** `CLAUDE.md` provides standing instructions that help Claude Code understand the project and follow its coding rules.

### 2. Core Lab – Feature Development on Phase 3 Project

**Task:** Purchase Order Quantity Validation

- Worked on the purchase order service project.
- Reviewed the existing code before making changes.
- Used a structured approach to understand the requirement and plan the implementation.
- Worked on purchase order quantity validation.
- Added test coverage using `po-quantity.test.js`.
- Reviewed the code and test files.

**Learning:** Writing a clear requirement, reviewing the plan, and testing the changes helps improve code quality and reduce mistakes.

### 3. Level-up Lab – Make Claude Code Yours

Created the `.claude/` setup with the following components:

**A. Skill – Explain CDS**
- Created `SKILL.md`.
- Defined instructions for explaining CDS concepts in simple English.
- Learned how reusable skills help Claude Code perform repeated tasks.

**B. Hook – Automatic Test Execution**
- Created `settings.json`.
- Configured a `PostToolUse` hook for Edit and Write operations.
- Used `npm test` as the configured test command.
- Learned how hooks can automate checks after file changes.

**C. Subagent – Test Writer**
- Created `test-writer.md`.
- Defined the test-writer subagent instructions.
- Learned how subagents can help with separate tasks such as writing and reviewing tests.

**Learning:** Skills provide reusable instructions, hooks automate actions, and subagents help divide work into smaller tasks.

### 4. Capstone 2 – Invoice-to-Insight Setup

**Project:** Invoice-to-Insight

Prepared the initial project structure for the Capstone 2 assignment.

**Project files:**
- `data/po_list.csv` – Purchase Order data.
- `invoices/invoice1.json` – Sample invoice data.
- `invoices/invoice2.json` – Sample invoice data.
- `spec.md` – Project requirements and specifications.
- `README.md` – Project overview and documentation.

**Work completed:**
- Prepared the project folder structure.
- Added the PO list and invoice JSON files.
- Prepared the initial project specification.
- Added project documentation.
- Kept the shared `CLAUDE.md` outside the Capstone project folder, as instructed.
- Committed and pushed the Capstone 2 setup to GitHub.

**Learning:** Understood the initial structure of an agentic invoice-processing project and how invoice data, purchase order validation, documentation, and specifications fit together.

### 5. Proof & Log

**Question: Which Claude Code habit saved you the most time?**

The habit that saved me the most time was using Plan mode before making changes. Claude Code first analysed my project and provided a step-by-step plan. I reviewed the plan before approving the changes. This helped me understand the work, avoid unnecessary edits, and reduce mistakes. Regular Git commits also helped me track my progress safely.

**Proof of work:**
- Day 6 task files organised in the repository.
- Capstone 2 setup committed and pushed to GitHub.
- Day 6 folder pushed to the GitHub repository.

### Key Learnings from Day 6

1. Learned how to install, start, and work with Claude Code.
2. Understood the purpose of `CLAUDE.md`.
3. Practised the Plan → Approve → Act → Review workflow.
4. Learned about Manual mode, Plan mode, and checkpoints.
5. Worked on purchase order quantity validation and tests.
6. Explored skills, hooks, and subagents.
7. Learned how to organise and document the Capstone 2 project.
8. Understood why reviewing AI-generated code and running tests are important.

### Conclusion

Day 6 helped me understand how to use Claude Code as an AI coding agent rather than just a coding assistant. I learned to give clear instructions, review plans before approving changes, use reusable skills, automate checks with hooks, and organise project work using Git and GitHub.
