
import anthropic
import json

from tools import (
    list_open_pos,
    get_po_status,
    draft_email,
    send_email
)

client = anthropic.Anthropic()

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
        "description": "Create a vendor reminder email draft. Do not send it.",
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
        "description": "Simulate sending an email draft. Human approval is required.",
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

# Connect tool names to Python functions
def run_tool(name, inputs):

    if name == "list_open_pos":
        return list_open_pos()

    elif name == "get_po_status":
        return get_po_status(inputs["po_number"])

    elif name == "draft_email":
        return draft_email(
            inputs["vendor"],
            inputs["text"]
        )

    elif name == "send_email":
        return send_email(inputs["draft_id"])

    return {"error": "Unknown tool"}


# Goal given to Claude
messages = [
    {
        "role": "user",
        "content": """
        Find all late purchase orders.

        Check their status and identify the vendor names.
        Draft a polite reminder email for each vendor
        with late purchase orders.

        Do not send any emails.
        Only create email drafts.
        Explain the results in simple English.
        """
    }
]

print("\nDAY 05 - TASK 2: AGENT LOOP")
print("=" * 50)

# Agent loop: maximum 10 steps
for step in range(10):

    print(f"\nAGENT STEP {step + 1}")

    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=1500,
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

            # Safety: do not send emails automatically
            if block.name == "send_email":
                output = {
                    "status": "Blocked",
                    "message": "Human approval required. Email not sent."
                }
            else:
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
