
import json
from pathlib import Path
from uuid import uuid4

# File containing the purchase order data
PO_FILE = Path(__file__).with_name("pos.json")

# Temporary storage for email drafts
DRAFTS = {}


# Tool 1: List open purchase orders
def list_open_pos():
    with open(PO_FILE, "r", encoding="utf-8") as file:
        pos = json.load(file)

    open_pos = [
        po for po in pos
        if po["deliveredQty"] < po["orderedQty"]
    ]

    return open_pos


# Tool 2: Get purchase order status
def get_po_status(po_number):
    with open(PO_FILE, "r", encoding="utf-8") as file:
        pos = json.load(file)

    for po in pos:
        if po["poNumber"] == str(po_number):
            return {
                **po,
                "pendingQty": po["orderedQty"] - po["deliveredQty"]
            }

    return {"error": "Purchase order not found"}


# Tool 3: Draft an email
def draft_email(vendor, text):
    draft_id = str(uuid4())

    draft = {
        "draft_id": draft_id,
        "vendor": vendor,
        "message": text,
        "status": "Draft"
    }

    DRAFTS[draft_id] = draft

    return draft


# Tool 4: Send email (safe simulation)
def send_email(draft_id):
    if draft_id not in DRAFTS:
        return {"error": "Draft not found"}

    return {
        "draft_id": draft_id,
        "status": "Pending human approval",
        "message": "Email not sent. Human approval required."
    }


# Manual testing of all four tools
if __name__ == "__main__":

    print("\nTEST 1: List Open Purchase Orders")
    open_pos = list_open_pos()
    print("Open POs:", len(open_pos))
    print(json.dumps(open_pos, indent=2))

    print("\nTEST 2: Get Purchase Order Status")
    status = get_po_status("4500012")
    print(json.dumps(status, indent=2))

    print("\nTEST 3: Draft Email")
    draft = draft_email(
        "Sharma Steels",
        "Please update the delivery status of PO 4500012."
    )
    print(json.dumps(draft, indent=2))

    print("\nTEST 4: Send Email")
    result = send_email(draft["draft_id"])
    print(json.dumps(result, indent=2))
