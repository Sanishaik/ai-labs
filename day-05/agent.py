
import anthropic
import json
from datetime import datetime, timezone

from tools import (
    list_open_pos,
    get_po_status,
    draft_email,
    send_email
)

client = anthropic.Anthropic()

AUDIT_FILE = "audit.jsonl"
MAX_STEPS = 10


# Tool descriptions for Claude
TOOLS = [
    {
        "name": "list_open_pos",
        "description": "List all open purchase orders with pending deliveries.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "get_po_status",
        "description": "Get the status and pending quantity of a purchase order.",
        "input_schema": {
            "type": "object",
            "properties": {
                "po_number": {
                    "type": "string",
                    "description": "Purchase order number"
                }
            },
            "required": ["po_number"]
        }
    },
    {
        "name": "draft_email",
        "description": "Create a vendor reminder email draft.",
        "input_schema": {
            "type": "object",
            "properties": {
                "vendor": {
                    "type": "string",
                    "description": "Vendor name"
                },
                "text": {
                    "type": "string",
                    "description": "Email message"
                }
            },
            "required": ["vendor", "text"]
        }
    },
    {
        "name": "send_email",
        "description": "Request human approval before sending an email.",
        "input_schema": {
            "type": "object",
            "properties": {
                "draft_id": {
                    "type": "string",
                    "description": "Email draft ID"
                }
            },
            "required": ["draft_id"]
        }
    }
]


# Record every tool call in audit.jsonl
def write_audit(tool_name, inputs, result):

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tool": tool_name,
        "input": inputs,
        "result": result
    }

    with open(AUDIT_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")


# Execute tools with human approval for email sending
def run_tool(name, inputs):

    if name == "list_open_pos":
        result = list_open_pos()

    elif name == "get_po_status":
        result = get_po_status(inputs["po_number"])

    elif name == "draft_email":
        result = draft_email(
            inputs["vendor"],
            inputs["text"]
        )

    elif name == "send_email":

        print("\nHUMAN APPROVAL REQUIRED")
        print("Draft ID:", inputs["draft_id"])

        approval = input("Approve this email? (y/n): ").strip().lower()

        if approval == "y":
            result = send_email(inputs["draft_id"])
            result["message"] = (
                "Approval received. Simulation only; "
                "no real email was sent."
            )

        else:
            result = {
                "status": "Refused",
                "approval": "n",
                "message": "Email sending refused by human. No email sent."
            }

    else:
        result = {"error": "Unknown tool"}

    write_audit(name, inputs, result)

    return result


# Goal given to Claude
messages = [
    {
        "role": "user",
        "content": """
        Find all late purchase orders.

        Check their status and identify the vendor names.
        Draft a polite reminder email for each vendor
        with late purchase orders.

        After drafting, request the send_email tool for
        each draft. The program will ask for human approval.

        Never bypass human approval.
        Explain the results in simple English.
        """
    }
]


print("\nDAY 05 - TASK 3: GUARDRAILS IN CODE")
print("=" * 50)

# Agent loop with a maximum of 10 steps
for step in range(MAX_STEPS):

    print(f"\nAGENT STEP {step + 1}")

    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=2000,
        tools=TOOLS,
        messages=messages
    )

    messages.append({
        "role": "assistant",
        "content": response.content
    })

    # Stop when Claude has finished
    if response.stop_reason != "tool_use":

        for block in response.content:
            if block.type == "text":
                print("\nCLAUDE FINAL RESPONSE:")
                print(block.text)

        break

    # Execute requested tools
    results = []

    for block in response.content:

        if block.type == "tool_use":

            print("\nTOOL:", block.name)
            print("INPUT:", json.dumps(block.input, indent=2))

            output = run_tool(block.name, block.input)

            print("RESULT:", json.dumps(output, indent=2))

            results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": json.dumps(output)
            })

    messages.append({
        "role": "user",
        "content": results
    })

else:
    print("\nMaximum 10 agent steps reached.")

print("\nAGENT LOOP COMPLETED")
print("Audit records saved in:", AUDIT_FILE)
