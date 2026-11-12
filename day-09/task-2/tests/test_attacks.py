import sys
import json
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

from invoice_validator import validate_invoice, AUDIT_FILE

INVOICE_FILE = BASE / "invoices" / "attack_invoices.json"

with open(INVOICE_FILE, "r", encoding="utf-8") as file:
    ATTACKS = json.load(file)


def run_attack(attack_number):
    attack = ATTACKS[attack_number - 1]
    invoice = attack["invoice"]

    if isinstance(invoice, dict):
        invoice_json = json.dumps(invoice)
    else:
        invoice_json = invoice

    source = f"attack{attack_number:02d}_{attack['type']}"

    result = validate_invoice(invoice_json, source=source)

    assert result["status"] == "EXCEPTION", (
        f"Attack {attack_number} was not rejected: {result}"
    )
    assert result["reasons"], (
        f"Attack {attack_number} has no rejection reason."
    )
    assert result["posted"] is False, (
        f"Attack {attack_number} was posted."
    )


def setUpModule():
    AUDIT_FILE.write_text("", encoding="utf-8")


class TestInvoiceAttacks(unittest.TestCase):

    def test_01_prompt_injection(self):
        run_attack(1)

    def test_02_amount_mismatch(self):
        run_attack(2)

    def test_03_invalid_po(self):
        run_attack(3)

    def test_04_duplicate_invoice(self):
        run_attack(4)

    def test_05_huge_amount(self):
        run_attack(5)

    def test_06_invalid_dates(self):
        run_attack(6)

    def test_07_invalid_gstin(self):
        run_attack(7)

    def test_08_vendor_mismatch(self):
        run_attack(8)

    def test_09_empty_invoice(self):
        run_attack(9)

    def test_10_line_item_mismatch(self):
        run_attack(10)


if __name__ == "__main__":
    unittest.main()
