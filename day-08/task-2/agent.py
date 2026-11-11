import json
import logging
from pathlib import Path

from server import check_supplier, create_po, route_to_manager

BASE_DIR = Path(__file__).resolve().parent
REQUISITIONS_FILE = BASE_DIR / "data" / "requisitions.json"

APPROVAL_LIMIT = 2500000

logging.basicConfig(
    filename=BASE_DIR / "logs" / "agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def process_requisition(requisition):
    requisition_id = requisition["id"]
    supplier = requisition["supplier"]
    amount = requisition["amount"]

    supplier_result = check_supplier(supplier)
    rating = supplier_result["rating"]

    if rating != "good":
        reason = f"Supplier rating is '{rating}', not good."
        result = route_to_manager(
            requisition_id, supplier, amount, reason
        )

    elif amount > APPROVAL_LIMIT:
        reason = "Requisition amount exceeds the ₹25 lakh approval limit."
        result = route_to_manager(
            requisition_id, supplier, amount, reason
        )

    else:
        result = create_po(requisition_id, supplier, amount)
        reason = "Supplier is good and amount is within the ₹25 lakh limit."

    logging.info(
        "Decision for %s: %s. Reason: %s",
        requisition_id,
        result["status"],
        reason,
    )

    return {
        "requisition_id": requisition_id,
        "supplier": supplier,
        "amount": amount,
        "decision": result["status"],
        "reason": reason,
    }


def main():
    with REQUISITIONS_FILE.open("r", encoding="utf-8") as file:
        requisitions = json.load(file)

    decisions = []

    for requisition in requisitions:
        decision = process_requisition(requisition)
        decisions.append(decision)
        print(json.dumps(decision, indent=4))

    print("\nAll requisitions processed.")
    print(f"Total processed: {len(decisions)}")


if __name__ == "__main__":
    main()
