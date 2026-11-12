import csv
import logging
import json
from datetime import date, datetime, timezone
from pathlib import Path

from mcp.server.fastmcp import FastMCP

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR.parent / "data" / "po_list.csv"
LOG_FILE = BASE_DIR / "logs" / "server.log"
AUDIT_FILE = BASE_DIR.parent / "logs" / "audit.log"
APPROVAL_FILE = BASE_DIR.parent / "results" / "approval_records.json"

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

mcp = FastMCP("invoice-po-tools")


def load_purchase_orders():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"PO data file not found: {CSV_FILE}")

    with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    for row in rows:
        row["orderedQty"] = int(row["orderedQty"])
        row["deliveredQty"] = int(row["deliveredQty"])
        row["amount"] = float(row["amount"])
        row["isLate"] = row["isLate"].strip().lower() == "true"

    return rows


@mcp.tool()
def get_po(po_number: str) -> dict:
    """Get details of one purchase order using its PO number."""
    logging.info("Looking up purchase order %s", po_number)

    for po in load_purchase_orders():
        if po["poNumber"] == po_number:
            return po

    raise ValueError(f"Purchase order {po_number} was not found.")


@mcp.tool()
def list_late_pos(today: str) -> list[dict]:
    """List overdue purchase orders that still have pending quantities. Date format: YYYY-MM-DD."""
    try:
        current_date = date.fromisoformat(today)
    except ValueError:
        raise ValueError("Invalid date. Please use YYYY-MM-DD format.")

    late_pos = []

    for po in load_purchase_orders():
        due_date = date.fromisoformat(po["dueDate"])
        has_pending_quantity = po["deliveredQty"] < po["orderedQty"]

        if due_date < current_date and has_pending_quantity:
            late_pos.append(po)

    logging.info("Found %s late purchase orders for %s", len(late_pos), today)
    return late_pos


@mcp.tool()
def check_invoice_po(po_number: str, vendor_id: str) -> dict:
    """Check whether an invoice PO exists and its vendor ID matches the invoice."""
    logging.info(
        "Checking invoice PO %s for vendor %s",
        po_number,
        vendor_id,
    )

    for po in load_purchase_orders():
        if po["poNumber"] == po_number:
            vendor_match = po["vendor_ID"] == vendor_id

            return {
                "po_found": True,
                "vendor_match": vendor_match,
                "po_number": po_number,
                "invoice_vendor_id": vendor_id,
                "po_vendor_id": po["vendor_ID"],
                "message": (
                    "PO found and vendor matches."
                    if vendor_match
                    else "PO found, but vendor does not match."
                ),
            }

    return {
        "po_found": False,
        "vendor_match": False,
        "po_number": po_number,
        "invoice_vendor_id": vendor_id,
        "po_vendor_id": None,
        "message": "Purchase order was not found.",
    }



@mcp.tool()
def validate_invoice(invoice_json: str) -> dict:
    """Validate an invoice against purchase order data."""
    import json
    from decimal import Decimal, InvalidOperation

    try:
        invoice = json.loads(invoice_json)
    except json.JSONDecodeError:
        return {
            "status": "EXCEPTION",
            "reasons": ["Invalid invoice JSON."]
        }

    if not isinstance(invoice, dict):
        return {
            "status": "EXCEPTION",
            "reasons": ["Invoice must be a JSON object."]
        }

    invoice_number = invoice.get("invoiceNumber")
    po_number = invoice.get("poNumber")
    vendor_id = invoice.get("vendorId")
    vendor_name = invoice.get("vendorName")
    invoice_amount = invoice.get("totalAmount", invoice.get("amount"))

    if not vendor_id and isinstance(vendor_name, str):
        if vendor_name.startswith("Vendor "):
            vendor_id = vendor_name.removeprefix("Vendor ")

    reasons = []
    required_fields = {
        "invoiceNumber": invoice_number,
        "poNumber": po_number,
        "vendorId": vendor_id,
        "amount": invoice_amount,
        "currency": invoice.get("currency"),
    }

    for field, value in required_fields.items():
        if value is None or value == "":
            reasons.append(f"Missing required field: {field}")

    if reasons:
        return {
            "invoice_number": invoice_number,
            "status": "EXCEPTION",
            "reasons": reasons,
        }

    purchase_orders = load_purchase_orders()
    po = next(
        (row for row in purchase_orders if row["poNumber"] == str(po_number)),
        None,
    )

    if po is None:
        reasons.append(f"PO {po_number} was not found.")
        po_amount = None
    else:
        po_amount = Decimal(str(po["amount"]))

        if po["vendor_ID"] != vendor_id:
            reasons.append(
                f"Vendor mismatch: invoice has {vendor_id}, "
                f"but PO has {po['vendor_ID']}."
            )

        try:
            amount = Decimal(str(invoice_amount))
            if amount != po_amount:
                reasons.append(
                    f"Amount mismatch: invoice has {amount}, "
                    f"but PO has {po_amount}."
                )
        except InvalidOperation:
            reasons.append("Invoice amount is not a valid number.")

    status = "CLEAN" if not reasons else "EXCEPTION"

    result = {
        "invoice_number": invoice_number,
        "po_number": po_number,
        "vendor_id": vendor_id,
        "invoice_amount": str(invoice_amount),
        "po_amount": str(po_amount) if po_amount is not None else None,
        "status": status,
        "reasons": reasons,
    }

    logging.info(
        "Invoice %s validation result: %s",
        invoice_number,
        status,
    )

    return result


@mcp.tool()
def approve_invoice(
    invoice_number: str,
    approver: str,
    decision: str,
    comments: str = "",
) -> dict:
    """Record an approval or rejection for a CLEAN invoice."""
    decision = decision.strip().upper()
    approver = approver.strip()

    if not invoice_number or not approver:
        raise ValueError("Invoice number and approver are required.")

    if decision not in ("APPROVED", "REJECTED"):
        raise ValueError("Decision must be APPROVED or REJECTED.")

    invoice_file = next(
        (
            path for path in (BASE_DIR.parent / "invoices").glob("invoice*.json")
            if json.loads(path.read_text(encoding="utf-8")).get("invoiceNumber")
            == invoice_number
        ),
        None,
    )

    if invoice_file is None:
        raise ValueError(f"Invoice {invoice_number} was not found.")

    invoice = json.loads(invoice_file.read_text(encoding="utf-8"))
    validation = validate_invoice(json.dumps(invoice))

    if validation["status"] != "CLEAN":
        timestamp = datetime.now(timezone.utc).isoformat()
        reason = "; ".join(validation["reasons"])
        AUDIT_FILE.parent.mkdir(parents=True, exist_ok=True)
        with AUDIT_FILE.open("a", encoding="utf-8") as audit:
            audit.write(
                f"{timestamp} | {invoice_number} | BLOCKED | "
                f"approver={approver} | reason={reason} | posted=False\n"
            )
        raise ValueError(
            f"Invoice {invoice_number} cannot be approved: " + reason
        )

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "invoice_number": invoice_number,
        "po_number": invoice["poNumber"],
        "validation_status": validation["status"],
        "approver": approver,
        "decision": decision,
        "comments": comments,
        "posted": False,
    }

    APPROVAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    records = (
        json.loads(APPROVAL_FILE.read_text(encoding="utf-8"))
        if APPROVAL_FILE.exists()
        else []
    )
    records.append(record)
    APPROVAL_FILE.write_text(json.dumps(records, indent=2), encoding="utf-8")

    AUDIT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_FILE.open("a", encoding="utf-8") as audit:
        audit.write(
            f"{record['timestamp']} | {invoice_number} | {decision} | "
            f"{invoice['poNumber']} | approver={approver} | "
            f"comments={comments} | posted=False\n"
        )

    logging.info("Invoice %s decision recorded: %s", invoice_number, decision)
    return record

if __name__ == "__main__":
    mcp.run()
