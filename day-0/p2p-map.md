# P2P Process Map for an AI Agent

## Overview

**P2P (Procure-to-Pay)** is an end-to-end SAP business process that starts with requesting goods or services and ends with paying the vendor.

This document maps five key P2P steps, their SAP transaction codes, main tables, responsible users, and one potential task for an AI agent at each step.

## P2P Process Flow

Purchase Requisition → Purchase Order → Goods Receipt → Invoice Verification → Vendor Payment

## Step 1: Purchase Requisition

- **T-code:** `ME51N`
- **Main Table:** `EBAN`
- **User:** Requester / Purchasing Department
- **Purpose:** Create a request to purchase goods or services.
- **AI Agent Job:** Review purchase requisitions for missing information, identify duplicate requests, and flag unusual quantities before submission.

## Step 2: Purchase Order

- **T-code:** `ME21N`
- **Main Tables:** `EKKO` (Purchase Order Header), `EKPO` (Purchase Order Items)
- **User:** Purchasing Officer / Buyer
- **Purpose:** Create a formal purchase order for a vendor.
- **AI Agent Job:** Compare purchase requisition details with vendor quotations and flag differences in price, quantity, delivery date, or payment terms for buyer review.

## Step 3: Goods Receipt

- **T-code:** `MIGO`
- **Main Tables:** `MKPF` and `MSEG` in many ECC systems; `MATDOC` is the central material document table in SAP S/4HANA.
- **User:** Warehouse Clerk / Goods Receiver
- **Purpose:** Record goods received against a purchase order.
- **AI Agent Job:** Compare the received quantity with the purchase order quantity and flag shortages, excess deliveries, or potential duplicate receipts.

## Step 4: Invoice Verification

- **T-code:** `MIRO`
- **Main Tables:** `RBKP` (Invoice Header), `RSEG` (Invoice Items)
- **User:** Accounts Payable Accountant
- **Purpose:** Verify a vendor invoice against the purchase order and goods receipt.
- **AI Agent Job:** Assist with three-way matching of the purchase order, goods receipt, and invoice, and flag price or quantity mismatches for review.

## Step 5: Vendor Payment

- **T-code:** `F110` (Automatic Payment Program)
- **Main Tables:** `REGUH` and `REGUP` for payment-run data; accounting documents may also be relevant.
- **User:** Accounts Payable Accountant / Finance Team
- **Purpose:** Process payments to vendors according to payment terms and due dates.
- **AI Agent Job:** Identify invoices approaching or past their due dates, prepare a proposed payment-priority list, and flag possible duplicate payments for finance-team review.

## AI Agent Safety and Controls

An AI agent supporting the P2P process should:

- Read only the SAP data it is authorized to access.
- Follow SAP role-based authorizations and company policies.
- Flag exceptions and explain why they need attention.
- Request human approval before creating or changing business documents or initiating payments.
- Never independently release payments or bypass approval controls.

## Summary Table

| P2P Step | T-code | Main Table(s) | Responsible User | AI Agent Job |
|---|---|---|---|---|
| Purchase Requisition | `ME51N` | `EBAN` | Requester / Purchasing Department | Detect incomplete or duplicate requests |
| Purchase Order | `ME21N` | `EKKO`, `EKPO` | Purchasing Officer / Buyer | Flag quotation and order discrepancies |
| Goods Receipt | `MIGO` | `MKPF`, `MSEG` / `MATDOC` | Warehouse Clerk | Flag quantity discrepancies |
| Invoice Verification | `MIRO` | `RBKP`, `RSEG` | Accounts Payable Accountant | Assist with three-way matching |
| Vendor Payment | `F110` | `REGUH`, `REGUP` | Accounts Payable / Finance Team | Flag overdue invoices and potential duplicate payments |

## Conclusion

Mapping the P2P process helps identify practical opportunities for AI agents in SAP. An agent can assist with data validation, discrepancy detection, invoice matching, and payment prioritization while keeping financial approvals and sensitive actions under human control.
