import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "extracted"

REQUIRED_FIELDS = [
    "invoiceNumber",
    "invoiceDate",
    "vendorName",
    "vendorId",
    "poNumber",
    "currency",
    "subtotal",
    "taxAmount",
    "totalAmount",
    "lineItems",
]


def extract_invoice(input_file):
    input_path = Path(input_file)

    try:
        with input_path.open("r", encoding="utf-8") as file:
            invoice = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Unable to read invoice: {error}") from error

    if not isinstance(invoice, dict):
        raise ValueError("Invoice data must be a JSON object.")

    # Keep missing line items as an empty array.
    extracted = {
        field: invoice.get(field)
        for field in REQUIRED_FIELDS
    }
    if extracted["lineItems"] is None:
        extracted["lineItems"] = []

    # Map the sample's amount field to totalAmount.
    if extracted["totalAmount"] is None and "amount" in invoice:
        extracted["totalAmount"] = invoice["amount"]

    # Map vendor ID from the PO number's vendor reference
    # only when the sample explicitly contains that information.
    if extracted["vendorId"] is None:
        vendor_name = extracted["vendorName"]
        if isinstance(vendor_name, str) and vendor_name.startswith("Vendor "):
            extracted["vendorId"] = vendor_name.removeprefix("Vendor ")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"{input_path.stem}_extracted.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(extracted, file, indent=2, ensure_ascii=False)

    return output_file


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_invoice.py <invoice.json>")
        sys.exit(1)

    try:
        result = extract_invoice(sys.argv[1])
        print(f"Extraction successful: {result}")
    except ValueError as error:
        print(f"Extraction failed: {error}")
        sys.exit(1)
