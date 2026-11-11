# Day 8 - Task 2: Purchase Requisition Agent

## Overview
A Python-based Purchase Requisition Agent that checks supplier ratings and applies a ₹25 lakh approval limit.

## Business Rules
1. Good supplier and amount up to ₹25 lakh: create a simulated PO.
2. New, poor, or unknown supplier: route to Procurement Manager.
3. Amount above ₹25 lakh: route to Procurement Manager.
4. Log every decision with its reason.

## MCP Tools
- check_supplier: Checks supplier ratings.
- create_po: Saves simulated purchase orders.
- route_to_manager: Sends exceptions for manager review.

## Project Structure
- data/suppliers.csv
- data/requisitions.json
- logs/agent.log
- server.py
- agent.py
- test_mcp.py
- po_created.json
- manager_queue.json

## Test Results
- PR1: PO_CREATED
- PR2: PO_CREATED
- PR3: PO_CREATED
- PR4: MANAGER_REVIEW
- PR5: MANAGER_REVIEW

Total: 5 requisitions processed successfully.
3 simulated purchase orders created.
2 requisitions routed for manager review.

## MCP Verification
Successfully connected to the MCP server and verified all three tools.

## How to Run
Run the agent:
python day-08/task-2/agent.py

Test the MCP server:
python day-08/task-2/test_mcp.py

## Safety Note
This is a training project. Purchase orders are simulated and saved in local JSON files. No real SAP purchasing transactions are performed.
