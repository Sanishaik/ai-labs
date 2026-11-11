import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

BASE_DIR = Path(__file__).resolve().parent

async def main():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(BASE_DIR / "server.py")],
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            response = await session.list_tools()

            print("MCP server connected successfully!")
            print("\nAvailable MCP tools:")

            for tool in response.tools:
                print("-", tool.name)

            result = await session.call_tool(
                "check_supplier",
                {"supplier": "Sharma Steels"},
            )

            print("\nSupplier check result:")
            print(result)

asyncio.run(main())
