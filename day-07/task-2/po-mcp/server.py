import csv
import logging
from datetime import date
from pathlib import Path

from mcp.server.fastmcp import FastMCP

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data" / "po_list.csv"
LOG_FILE = BASE_DIR / "logs" / "server.log"

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

mcp = FastMCP("po-tools")


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


if __name__ == "__main__":
    mcp.run()
