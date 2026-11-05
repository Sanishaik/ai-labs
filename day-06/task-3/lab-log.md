# Lab Log – Day 06 Task 3

## What I did

1. **Skill.** I created `explain-cds` as a project skill. The file has YAML frontmatter and teaches ABAP CDS views step by step. The examples are not run against an SAP system.
2. **Hook.** I created `.claude/settings.json` with a PostToolUse hook for `Edit|Write` that runs `npm test`. The file is valid JSON.
3. **Subagent.** I created the `test-writer` subagent. When I first tried to use it in the session, the session did not recognise it. I did the review directly, reading the files, and reported that clearly.
4. **PATCH test.** I added a test that PATCHes seed PO `4500012` with `deliveredQty: 150` and expects HTTP 400. The first run found a real gap: the service returned 200.
5. **Fix.** I extended the quantity rule to UPDATE. When a PATCH leaves out a quantity, the stored value is read for the comparison.
6. **Commits and push.** I committed the changes as `595db63` and `7ef2474`. The first push was rejected because the remote had one commit I did not have. I rebased onto it, reran the tests, and pushed. Both commits are on `origin/main`.

## Test result

- `npm test`: **10 passed, 0 failed**, exit code 0.

## Hook status

- The configuration file is in place and is valid JSON.
- Per your report, the hook was loaded and an earlier automatic run showed a **non-blocking error**. I did not verify this in this session, and I do not claim a clean automatic run.

## Problems I hit

- **Test runner hid failures.** An `after` hook called `cds.shutdown()`, which calls `process.exit()`. The run stopped before reporting, and it exited with code 0 even though a test had failed. I confirmed the cause on a temporary copy of the file, then removed the one line.
- **ESM import of `SELECT` failed.** `@sap/cds` is a CommonJS module, so `import { SELECT }` does not work. Using `cds.ql` did.
- **Push rejected.** The remote had a commit the local branch lacked. I rebased, did not force-push, and then pushed.

## What I learned

- **Skill:** a set of written instructions that Claude Code uses when the task matches. It changes how Claude explains or works, but it does not run code.
- **Hook:** a command Claude Code runs automatically at a defined point, such as after a file edit. It runs the command you configure, not Claude's own judgment.
- **Subagent:** a separate assistant with its own instructions and tool list. Its instructions and tool list limit what it can do.
- **Manual approval:** in Manual mode, Claude shows each change and waits for a yes before editing. This makes it easy to review each step.
- **PATCH validation:** a PATCH request sends only the fields that change. If a rule checks only the request body, it can miss a case where the stored value and the new value together break the rule. Here, a PATCH that set `deliveredQty` to 150 passed because the stored `orderedQty` was never read.
