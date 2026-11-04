# Technical Specification: Purchase Order Details Report

**Status:** Draft for review. Not validated in a SAP system.
**Source:** Functional Specification (FS) "Develop an SAP ABAP report to display purchase order details."

**Legend:**
- **[CONFIRMED]** = stated in the FS
- **[ASSUMPTION]** = my reasonable interpretation, which must be approved
- **[OPEN]** = missing information; see Section 11

---

## 1. Requirement Summary

Build an ABAP report where a user enters one purchase order (PO) number and sees the header and item details of that PO.

**Output fields requested:**
- Purchase Order Number
- Vendor Number
- Company Code
- Purchasing Organization
- Purchase Order Date
- Material Number
- Ordered Quantity

**[ASSUMPTION]** The FS says "a purchase order number" (singular), so the report searches for one PO at a time.

---

## 2. Business Requirement

| # | Requirement | Source |
|---|---|---|
| BR-1 | User enters a PO number | [CONFIRMED] |
| BR-2 | Report displays the seven fields listed above | [CONFIRMED] |
| BR-3 | Use suitable SAP standard tables | [CONFIRMED] |
| BR-4 | Provide a proposed technical design | [CONFIRMED] |
| BR-5 | Unclear items must be flagged, not assumed | [CONFIRMED] |

**Beginner note:** In SAP, a purchase order has two levels:
- **Header:** data that applies to the whole PO (vendor, company code, purchasing org, date).
- **Items:** one row per product or service on the PO (material, quantity).

A single PO can have many items, so the report output will have one row per item, with header data repeated on each row.

---

## 3. Proposed Technical Solution

**Approach:** A custom executable report (ABAP Report program) that reads standard SAP purchasing tables and displays the results in an ALV (Application List Viewer) grid.

**Why this approach:**
- Reading standard tables is the simplest, most stable way to get PO data.
- The FS asks for a report, so an executable program is the right object type.
- ALV gives users sorting, filtering, and export without extra coding.

**Standard alternative for reference:** Transaction **ME23N** (Display Purchase Order) already shows PO details. The custom report is needed only if the business wants a simpler, custom layout. **[OPEN]** Confirm whether ME23N is acceptable.

---

## 4. SAP Tables and Fields

### 4.1 EKKO: Purchasing Document Header

| Field | Description | Required Output Field |
|---|---|---|
| EBELN | Purchasing document number (PO number) | Purchase Order Number |
| LIFNR | Vendor account number | Vendor Number |
| BUKRS | Company code | Company Code |
| EKORG | Purchasing organization | Purchasing Organization |
| BEDAT | Purchasing document date | Purchase Order Date |

**Key:** EBELN

### 4.2 EKPO: Purchasing Document Item

| Field | Description | Required Output Field |
|---|---|---|
| EBELN | PO number (links to EKKO) | Purchase Order Number |
| EBELP | Item number | Used for item identification |
| MATNR | Material number | Material Number |
| MENGE | Purchase order quantity | Ordered Quantity |
| MEINS | Base unit of measure | Unit for the quantity **[ASSUMPTION]** |
| LOEKZ | Deletion indicator | Used for filtering **[ASSUMPTION]** |

**Key:** EBELN + EBELP

### 4.3 How the Tables Link

```
EKKO (Header)                EKPO (Items)
EBELN  ──────── links to ──── EBELN
                              EBELP  (item number)
```

**Important notes for beginners:**
- Vendor (LIFNR) and company code are header fields, so they live in EKKO, not EKPO.
- Ordered quantity and material are item fields, so they live in EKPO.
- **[ASSUMPTION]** The FS does not mention the unit of measure, but a quantity without a unit is hard to interpret. Including MEINS is recommended. **[OPEN]** Confirm.

**Optional, not in the FS:** LFA1 (vendor master) holds the vendor name. Not included because the FS does not ask for it.

---

## 5. ABAP Objects Required

| # | Object | Type | Purpose | Why It Is Needed |
|---|---|---|---|---|
| 1 | ZPO_DISPLAY_REPORT | Executable Program (SE38) | Main report | Holds the selection screen, data logic, and output |
| 2 | Data declarations | Internal tables and work areas | Store header and item data | Holds retrieved data in memory before display |
| 3 | CL_SALV_TABLE | Standard ALV class | Display output in a grid | Standard, modern way to show tabular data |
| 4 |