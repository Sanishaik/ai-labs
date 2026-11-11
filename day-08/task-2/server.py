import csv
import json
import logging
from pathlib import Path

from mcp.server.fastmcp import FastMCP

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

SUPPLIERS_FILE = DATA_DIR / "suppliers.csv"
PO_FILE = BASE_DIR / "po_created.json"
MANAGER_FILE = BASE_DIR / "manager_queue.json"
LOG_FILE = LOG_DIR / "agent.log"

LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

mcp = FastMCP("purchase-requisition-agent")


def load_suppliers():
    with SUPPLIERS_FILE.open("r", newline="", encoding="utf-8") as file:
        return {
            row["supplier"].strip(): row["rating"].strip().lower()
            for row in csv.DictReader(file)
        }


def save_record(file_path, record):
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as file:
            records = json.load(file)
    else:
        records = []

    records.append(record)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


@mcp.tool()
def check_supplier(supplier: str) -> dict:
    """Check a supplier's rating using the supplier CSV file."""
    rating = load_suppliers().get(supplier)

    if rating is None:
        result = {"supplier": supplier, "rating": "unknown"}
    else:
        result = {"supplier": supplier, "rating": rating}

    logging.info("Supplier check: %s", result)
    return result


@mcp.tool()
def create_po(requisition_id: str, supplier: str, amount: float) -> dict:
    """Create a simulated purchase order in a local JSON file only."""
    if amount <= 0:
        raise ValueError("Purchase order amount must be greater than zero.")

    record = {
        "requisition_id": requisition_id,
        "supplier": supplier,
        "amount": amount,
        "status": "PO_CREATED",
    }

    save_record(PO_FILE, record)
    logging.info(
        "PO created for %s. Reason: supplier is good and amount is within approval limit.",
        requisition_id,
    )
    return record


@mcp.tool()
def route_to_manager(
    requisition_id: str,
    supplier: str,
    amount: float,
    reason: str,
) -> dict:
    """Send a requisition to the Procurement Manager review queue."""
    record = {
        "requisition_id": requisition_id,
        "supplier": supplier,
        "amount": amount,
        "status": "MANAGER_REVIEW",
        "reason": reason,
    }

    save_record(MANAGER_FILE, record)
    logging.info("Manager escalation for %s. Reason: %s", requisition_id, reason)
    return record


if __name__ == "__main__":
    mcp.run()
