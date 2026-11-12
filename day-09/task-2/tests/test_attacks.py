import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

from invoice_validator import validate_invoice, AUDIT_FILE


def run_attack(filename):
    path = BASE / "invoices" / filename
    invoice_json = path.read_text(encoding="utf-8")
    result = validate_invoice(invoice_json, source=filename)

    assert result["status"] == "EXCEPTION", result
    assert result["reasons"], result
    assert result["posted"] is False, result
    return result


def setUpModule():
    AUDIT_FILE.write_text("", encoding="utf-8")


class TestInvoiceAttacks(unittest.TestCase):

    def test_01_prompt_injection(self):
        run_attack("attack01_prompt_injection.json")

    def test_02_amount_mismatch(self):
        run_attack("attack02_amount_mismatch.json")

    def test_03_invalid_po(self):
        run_attack("attack03_invalid_po.json")

    def test_04_duplicate_invoice(self):
        run_attack("attack04_duplicate_invoice.json")

    def test_05_huge_amount(self):
        run_attack("attack05_huge_amount.json")

    def test_06_invalid_dates(self):
        run_attack("attack06_invalid_dates.json")

    def test_07_invalid_gstin(self):
        run_attack("attack07_invalid_gstin.json")

    def test_08_vendor_mismatch(self):
        run_attack("attack08_vendor_mismatch.json")

    def test_09_empty_invoice(self):
        run_attack("attack09_empty_invoice.json")

    def test_10_line_item_mismatch(self):
        run_attack("attack10_line_item_mismatch.json")


if __name__ == "__main__":
    unittest.main()
