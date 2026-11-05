# Plan – Day 06 Task 3

Goal: add three Claude Code features to the CAP Purchase Order Service and fix a validation gap found while testing them.

## Steps

1. **Create and test the explain-cds skill.**
   Write `.claude/skills/explain-cds/SKILL.md`, which explains ABAP CDS views to beginners. Check that the file has valid frontmatter.

2. **Configure the PostToolUse hook.**
   Create `.claude/settings.json` with a `PostToolUse` hook that runs `npm test` after `Edit|Write` tool calls.

3. **Create and use the test-writer subagent.**
   Write `.claude/agents/test-writer.md`. Its first use failed because the agent was not loaded in the session, so the review was done directly. See the lab log.

4. **Add the PATCH quantity validation test.**
   Add a test that PATCHes seed PO `4500012` (ordered 100) with `deliveredQty: 150` and expects HTTP 400 with "Delivered quantity must not exceed ordered quantity."

5. **Fix PATCH validation in the CAP service.**
   The quantity rule ran only before CREATE. Extend it to UPDATE. When a PATCH leaves out one of the two quantities, read the stored value and compare.

6. **Run all tests and push the changes.**
   Run `npm test`, commit with clear messages, and push to `origin/main`. Rebase onto the remote first, because the remote had one commit the local branch did not.

## Constraints

- Each change was shown and approved before it was made.
- Unrelated untracked files in the repository were left alone.
- No commit was made without a stated message.
