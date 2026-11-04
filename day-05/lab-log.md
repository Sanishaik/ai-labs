cat > lab-log.md <<'EOF'
# Day 05 - Task 3: Guardrails in Code

## Objective
Implement safety guardrails in the Python AI agent.

## Technologies Used
- Python
- Anthropic Python SDK
- Claude Haiku 5.5
- JSON Lines (JSONL)

## Guardrails Implemented

1. Human approval (y/n) is required before email sending.
2. Maximum agent execution is limited to 10 steps.
3. Purchase order data is accessed using read-only functions.
4. Every tool call is recorded in audit.jsonl.
5. Refused email requests are recorded in the audit log.

## Execution Results

| Test | Result |
|---|---|
| Open purchase orders found | 6 |
| Late purchase orders found | 4 |
| Email drafts created | 4 |
| Email requests refused | 4 |
| Actual emails sent | 0 |
| Agent steps used | 5 |
| Audit records | 13 |

## Human Approval Test

The agent requested approval before each email sending attempt.

All four requests were refused by entering n.

Result: No emails were sent.

## Audit Log

File: audit.jsonl

Total records: 13

The audit log records tool names, inputs, timestamps and results, including refused email requests.

## Conclusion

Successfully implemented guardrails in the AI agent. Human approval, execution limits and audit logging helped prevent unauthorized email sending and maintain a record of tool activity.
EOFcat prompts/prompt-3-functional-to-technical-spec.md