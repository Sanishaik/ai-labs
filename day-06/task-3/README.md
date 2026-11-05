# Day 06 – Task 3: Make Claude Code Yours

## Objective

Customise Claude Code for a real project. This task adds three Claude Code features to the CAP Purchase Order Service (`day-0/po-service`), uses them, and fixes a gap found along the way: PATCH requests skipped the quantity validation that CREATE requests already had.

## The three Claude Code features

| Feature | What it is | Where it lives |
|---|---|---|
| **Skill** | A reusable instruction set. Here, `explain-cds` teaches SAP ABAP CDS views in simple English. | `.claude/skills/explain-cds/SKILL.md` |
| **Hook** | A shell command that Claude Code runs automatically at a set point. Here, `npm test` runs after each `Edit` or `Write`. | `.claude/settings.json` |
| **Subagent** | A specialised assistant with its own instructions and tools. Here, `test-writer` writes and reviews tests for the PO service. | `.claude/agents/test-writer.md` |

## Contents of `files/`

Copies of the five final files:

- `files/SKILL.md` – the explain-cds skill
- `files/settings.json` – the PostToolUse hook configuration
- `files/test-writer.md` – the test-writer subagent
- `files/po-service.js` – the service with the PATCH quantity fix
- `files/po-quantity.test.js` – the test file, including the PATCH test

The copies are flat in `files/`. The originals remain in `day-0/po-service/`.

## Test result

`npm test` in `day-0/po-service`, after the PATCH fix:

- **10 passed, 0 failed** (exit code 0)

## Commits

- `595db63` – Add Claude Code skill hook subagent and PATCH tests
- `7ef2474` – Fix PATCH quantity validation

Both are on `origin/main`.
