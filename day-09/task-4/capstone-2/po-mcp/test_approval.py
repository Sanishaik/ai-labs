import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(command=sys.executable, args=["server.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(
                "approve_invoice",
                {
                    "invoice_number": "INV004",
                    "approver": "Demo Manager",
                    "decision": "APPROVED",
                    "comments": "Reviewed and approved for demo."
                }
            )
            for item in result.content:
                print(item.text)

if __name__ == "__main__":
    asyncio.run(main())
