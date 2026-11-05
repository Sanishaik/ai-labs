# Specification – Day 06 Task 3

## 1. Skill: `explain-cds`

- **Purpose:** explain SAP ABAP CDS views to a beginner in simple English, step by step, with small examples.
- **Behaviour:** Claude Code loads the skill when the user asks about CDS views, CDS syntax, annotations, or associations. The skill's instructions shape the explanation.
- **Original location:** `day-0/po-service/.claude/skills/explain-cds/SKILL.md`
- **Format:** YAML frontmatter with `name: explain-cds` and a description, followed by Markdown instructions.

## 2. Hook: PostToolUse `npm test`

- **Purpose:** run the test suite automatically after file changes, so failures show up straight away.
- **Behaviour:** after any tool call whose name matches `Edit|Write`, Claude Code runs the command `npm test`.
- **Original location:** `day-0/po-service/.claude/settings.json`
- **Configuration:**
  - event: `PostToolUse`
  - matcher: `Edit|Write`
  - command: `npm test`
- **Known limitation:** a failing test makes `npm test` exit non-zero. For PostToolUse, that is reported to the user but does not block the edit that has already happened.

## 3. Subagent: `test-writer`

- **Purpose:** write and review automated tests for the PO service.
- **Behaviour:** a separate assistant that Claude Code can delegate to. It has its own instructions and a restricted tool list: Read, Glob, Grep, Write, Edit, and Bash.
- **Scope rules in its instructions:** write test files only. Do not change `srv/`, `db/`, `package.json`, or `CLAUDE.md`. Report service bugs instead of fixing them.
- **Original location:** `day-0/po-service/.claude/agents/test-writer.md`

## 4. PATCH quantity validation requirement

- **Rule:** on a PATCH to a purchase order, the same quantity rules apply as on CREATE:
  - ordered quantity must not be negative
  - delivered quantity must not be negative
  - delivered quantity must not exceed ordered quantity
- **Missing values:** if the PATCH body leaves out one quantity, the stored value is used for the comparison. Negative checks use only the values sent in the request.
- **Expected response:** HTTP **400** with the message `Delivered quantity must not exceed ordered quantity.`
- **Test:** PATCH seed PO `4500012` (ordered 100, delivered 60) with `deliveredQty: 150`.
- **Implementation:** `srv/po-service.js`, Rule 2, registered for `['CREATE', 'UPDATE']`.
- **Verification:** `npm test` passes 10 of 10 tests.

## 5. Original file locations

| Item | Path |
|---|---|
| Skill | `day-0/po-service/.claude/skills/explain-cds/SKILL.md` |
| Hook | `day-0/po-service/.claude/settings.json` |
| Subagent | `day-0/po-service/.claude/agents/test-writer.md` |
| Service fix | `day-0/po-service/srv/po-service.js` |
| PATCH test | `day-0/po-service/test/po-quantity.test.js` |
