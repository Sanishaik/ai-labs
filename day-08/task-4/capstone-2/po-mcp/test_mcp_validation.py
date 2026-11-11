import asyncio
import json
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

BASE_DIR = Path(__file__).resolve().parent.parent
INVOICE_DIR = BASE_DIR / "invoices"
RESULT_DIR = BASE_DIR / "results"


async def main():
    RESULT_DIR.mkdir(parents=True, exist_ok=True)

    params = StdioServerParameters(
        command=sys.executable,
        args=["server.py"],
    )

    clean_invoices = []
    exceptions = []

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("MCP connection successful!")

            for file in sorted(INVOICE_DIR.glob("invoice*.json")):
                invoice = json.loads(file.read_text(encoding="utf-8"))

                response = await session.call_tool(
                    "validate_invoice",
                    {"invoice_json": json.dumps(invoice)},
                )

                if response.isError:
                    raise RuntimeError(
                        f"MCP validation failed for {file.name}"
                    )

                result = json.loads(response.content[0].text)

                if result["status"] == "CLEAN":
                    clean_invoices.append(result)
                else:
                    exceptions.append(result)

                print(
                    f"{result['invoice_number']}: {result['status']}"
                )

    summary = {
        "total_invoices": len(clean_invoices) + len(exceptions),
        "clean_count": len(clean_invoices),
        "exception_count": len(exceptions),
        "clean_invoices": clean_invoices,
    }

    (RESULT_DIR / "clean_invoice_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    (RESULT_DIR / "exceptions.json").write_text(
        json.dumps(exceptions, indent=2),
        encoding="utf-8",
    )

    print("\nResults saved successfully.")
    print("Clean summary:", RESULT_DIR / "clean_invoice_summary.json")
    print("Exceptions:", RESULT_DIR / "exceptions.json")


if __name__ == "__main__":
    asyncio.run(main())
