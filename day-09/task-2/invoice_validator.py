import csv
import json
import logging
from pathlib import Path
from decimal import Decimal, InvalidOperation
from datetime import date

BASE = Path(__file__).resolve().parent
PO_FILE = BASE / "data" / "po_list.csv"
AUDIT_FILE = BASE / "audit.log"

logging.basicConfig(
    filename=AUDIT_FILE,
    level=logging.INFO,
    format="%(asctime)s %(message)s",
)

def load_pos():
    with PO_FILE.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def validate_invoice(invoice_json, source="unknown"):
    reasons = []
    invoice = {}

    try:
        invoice = json.loads(invoice_json)
        if not isinstance(invoice, dict):
            raise ValueError()
    except (json.JSONDecodeError, TypeError, ValueError):
        reasons.append("Invalid or empty invoice JSON.")

    number = invoice.get("invoiceNumber", "UNKNOWN")

    required = [
        "invoiceNumber", "poNumber", "vendorId", "vendorName",
        "invoiceDate", "dueDate", "gstin", "currency", "totalAmount"
    ]

    for field in required:
        if not invoice.get(field):
            reasons.append(f"Missing required field: {field}")

    invoice_text = json.dumps(invoice).lower()
    if any(
        phrase in invoice_text
        for phrase in ["ignore all rules", "approve me", "bypass validation"]
    ):
        reasons.append("Prompt injection detected.")

    if len(str(invoice.get("gstin", ""))) != 15:
        reasons.append("GSTIN must contain exactly 15 characters.")

    try:
        invoice_date = date.fromisoformat(invoice["invoiceDate"])
        due_date = date.fromisoformat(invoice["dueDate"])
        if due_date < invoice_date:
            reasons.append("Due date is before invoice date.")
    except (ValueError, KeyError, TypeError):
        reasons.append("Invalid invoice or due date.")

    po = None
    try:
        po = next(
            (p for p in load_pos()
             if p["poNumber"] == str(invoice.get("poNumber"))),
            None
        )
    except (OSError, csv.Error):
        reasons.append("Unable to read PO data.")

    if po is None:
        reasons.append("Purchase order not found.")
    else:
        if invoice.get("vendorId") != po["vendor_ID"]:
            reasons.append("Vendor ID mismatch.")

        if invoice.get("vendorName") != f"Vendor {po['vendor_ID']}":
            reasons.append("Vendor name mismatch.")

        try:
            amount = Decimal(str(invoice["totalAmount"]))
            po_amount = Decimal(po["amount"])
            if amount != po_amount:
                reasons.append("Invoice amount does not match PO.")
            if amount > Decimal("10000000"):
                reasons.append("Invoice amount exceeds safety limit.")
        except (InvalidOperation, KeyError, TypeError):
            reasons.append("Invalid invoice amount.")

    try:
        items = invoice["items"]
        if not isinstance(items, list) or not items:
            raise ValueError()

        item_total = sum(
            Decimal(str(item["quantity"])) *
            Decimal(str(item["unitPrice"]))
            for item in items
        )
        if item_total != Decimal(str(invoice["totalAmount"])):
            reasons.append("Line-item total mismatch.")
    except (KeyError, ValueError, TypeError, InvalidOperation):
        reasons.append("Invalid or missing invoice line items.")

    # Duplicate check against previously audited invoice numbers
    if number != "UNKNOWN" and AUDIT_FILE.exists():
        if f"Invoice={number} " in AUDIT_FILE.read_text(encoding="utf-8"):
            reasons.append("Duplicate invoice number detected.")

    status = "EXCEPTION" if reasons else "CLEAN"

    result = {
        "invoice_number": number,
        "status": status,
        "reasons": reasons,
        "posted": False
    }

    logging.info(
        "Source=%s Invoice=%s Status=%s Reasons=%s Posted=False",
        source, number, status, "; ".join(reasons)
    )

    return result
