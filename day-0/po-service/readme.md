# SAP CAP – Purchase Order Management Service

## 1. Project Overview

The **Purchase Order Management Service** is a Node.js-based application developed using the SAP Cloud Application Programming Model (CAP).

The application manages vendor and purchase order information and provides OData V4 APIs to retrieve, filter, sort, and create purchase orders.

It also identifies late purchase orders based on their due dates and delivery quantities.

## 2. Technology Stack

- SAP Cloud Application Programming Model (CAP)
- Node.js
- CDS (Core Data Services)
- JavaScript
- OData V4
- SQLite (local development)
- SAP Business Application Studio (BAS)

## 3. Project Structure

```text
po-service/
│
├── app/
│
├── db/
│   ├── data/
│   │   ├── resoftwa.po-Vendors.csv
│   │   └── resoftwa.po-PurchaseOrders.csv
│   └── schema.cds
│
├── srv/
│   ├── po-service.cds
│   └── po-service.js
│
├── test/
│   └── po.http
│
├── po_list.csv
├── vendors.csv
├── package.json
├── package-lock.json
├── readme.md
└── .gitignore
```

## 4. Key Features

- Vendor management.
- Purchase order retrieval.
- Purchase order creation.
- Validation to prevent zero or negative order amounts.
- Automatic late purchase order identification.
- OData V4 filtering and sorting.
- Vendor details using `$expand`.

## 5. Business Logic

### Purchase Order Validation

Before creating a purchase order, the application validates the order amount.

- Amount greater than zero: Request accepted.
- Amount less than or equal to zero: Request rejected with HTTP 400.

### Late Purchase Order Identification

A purchase order is considered late when:

- Its due date is earlier than the current date.
- Its delivered quantity is less than its ordered quantity.

The `isLate` field identifies whether the purchase order meets these conditions.

## 6. OData Service

**Service Name:** POService

**Local Service URL:**

```text
http://localhost:4004/odata/v4/po/
```

### Available Entities

| Entity | Description |
|---|---|
| Vendors | Vendor information |
| PurchaseOrders | Purchase order information |

## 7. Running the Application

Open a terminal in the project directory.

Install dependencies if required:

```bash
npm install
```

Start the CAP development server:

```bash
npx cds watch
```

Open the service URL displayed in the terminal.

## 8. API Testing

The HTTP test file is available at:

```text
test/po.http
```

The following scenarios are covered:

1. Retrieve all purchase orders.
2. Retrieve late purchase orders using `$filter`.
3. Sort purchase orders by due date.
4. Retrieve vendor details using `$expand`.
5. Validate rejection of an invalid purchase order.
6. Create a valid purchase order.

## 9. Sample OData Requests

Retrieve all purchase orders:

```http
GET http://localhost:4004/odata/v4/po/PurchaseOrders
```

Retrieve late purchase orders:

```http
GET http://localhost:4004/odata/v4/po/PurchaseOrders?$filter=isLate eq true
```

Retrieve purchase orders with vendor details:

```http
GET http://localhost:4004/odata/v4/po/PurchaseOrders?$expand=vendor
```

## 10. Project Objective

The objective of this project is to gain practical experience in SAP CAP application development, data modeling, service implementation, business validations, and OData V4 API testing.

**Developed as part of the Resoftwa Future-Ready Tech Training Program.**
