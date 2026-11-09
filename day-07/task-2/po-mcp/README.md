# Purchase Order MCP Server

## Overview
A Python MCP server that connects Claude Code to purchase order data stored in a CSV file.

## Features
- Retrieve a purchase order by PO number.
- Find overdue purchase orders with pending quantities.
- Validate date input.
- Handle invalid PO numbers with clear errors.
- Write activity logs to a file.

## MCP Tools

### get_po(po_number)
Returns details of one purchase order.

### list_late_pos(today)
Returns overdue purchase orders that still have pending quantities.

Date format: YYYY-MM-DD

## Technologies
- Python
- MCP Python SDK (FastMCP)
- CSV
- Claude Code

## Project Structure
- server.py: MCP server implementation
- data/po_list.csv: Purchase order data
- logs/: Server logs
- requirements.txt: Python dependencies

## Setup
Create a virtual environment and install dependencies using requirements.txt.

## Claude Code Integration
The server is registered as po-tools using the stdio transport.

Verify the connection with /mcp inside Claude Code.
