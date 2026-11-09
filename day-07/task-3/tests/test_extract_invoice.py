import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from extract_invoice import extract_invoice


BASE_DIR = Path(__file__).resolve().parents[1]
INVOICE_DIR = BASE_DIR / "invoices"


class TestInvoiceExtraction(unittest.TestCase):

    def test_invoice1_extraction(self):
        output_dir = Path(tempfile.mkdtemp())

        with patch("extract_invoice.OUTPUT_DIR", output_dir):
            output_file = extract_invoice(INVOICE_DIR / "invoice1.json")

        with output_file.open("r", encoding="utf-8") as file:
            result = json.load(file)

        self.assertEqual(result["invoiceNumber"], "INV001")
        self.assertEqual(result["vendorId"], "V001")
        self.assertEqual(result["poNumber"], "4500012")
        self.assertEqual(result["totalAmount"], 450000)
        self.assertIsInstance(result["totalAmount"], (int, float))
        self.assertEqual(result["lineItems"], [])

    def test_missing_fields(self):
        output_dir = Path(tempfile.mkdtemp())

        with tempfile.TemporaryDirectory() as temp_dir:
            input_file = Path(temp_dir) / "missing.json"
            input_file.write_text(
                json.dumps({"invoiceNumber": "INV003"}),
                encoding="utf-8",
            )

            with patch("extract_invoice.OUTPUT_DIR", output_dir):
                output_file = extract_invoice(input_file)

        with output_file.open("r", encoding="utf-8") as file:
            result = json.load(file)

        self.assertIsNone(result["totalAmount"])
        self.assertIsNone(result["subtotal"])
        self.assertEqual(result["lineItems"], [])

    def test_invalid_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file = Path(temp_dir) / "invalid.json"
            input_file.write_text("{invalid json", encoding="utf-8")

            with self.assertRaises(ValueError):
                extract_invoice(input_file)

    def test_invoice2_extraction(self):
        output_dir = Path(tempfile.mkdtemp())

        with patch("extract_invoice.OUTPUT_DIR", output_dir):
            output_file = extract_invoice(INVOICE_DIR / "invoice2.json")

        with output_file.open("r", encoding="utf-8") as file:
            result = json.load(file)

        self.assertEqual(result["invoiceNumber"], "INV002")
        self.assertEqual(result["vendorId"], "V003")
        self.assertEqual(result["totalAmount"], 175000)


if __name__ == "__main__":
    unittest.main()
