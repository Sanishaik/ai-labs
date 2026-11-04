
# Day 05 - Task 2: Agent Loop Yourself

## Objective
Build a simple agent loop using Claude Haiku 5.5 and Python without using an agent framework.

## Technologies Used
- Python
- Anthropic Python SDK
- Claude Haiku 5.5
- JSON
- Existing Task 1 Python tools

## Tools Used
1. list_open_pos()
2. get_po_status(po_number)
3. draft_email(vendor, text)
4. send_email(draft_id)

## Execution Results

| Test | Expected Result | Actual Result |
|---|---|---|
| List open POs | Find open orders | 6 found |
| Identify late POs | Find overdue orders | 4 found |
| Check PO status | Get pending quantities | Successful |
| Draft vendor emails | Create reminder drafts | 4 created |
| Send emails | Require human approval | No emails sent |

## Late Purchase Orders

| PO Number | Vendor | Pending Quantity |
|---|---|---:|
| 4500012 | Sharma Steels | 40 |
| 4500014 | Guntur Cables | 50 |
| 4500015 | Vizag Paints | 60 |
| 4500016 | New Vendor Co | 25 |

## Agent Loop Execution

- Step 1: Listed open purchase orders.
- Step 2: Checked the status of four late purchase orders.
- Step 3: Created four vendor reminder email drafts.
- Step 4: Claude generated the final summary.
- Maximum allowed steps: 10.
- Actual agent steps: 4.

## Safety
The agent was instructed not to send emails automatically. Email sending was protected by a human approval requirement.

## Conclusion
Successfully implemented an agent loop using Claude Haiku 5.5. The agent called Python tools, processed purchase order data, identified late deliveries, and generated vendor reminder email drafts.
ls -lh