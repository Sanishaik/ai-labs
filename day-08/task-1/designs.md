# Day 8 – Task 1: Agent Designs

## 1. O2C Credit Check Agent

AGENT NAME:
O2C Credit Check Agent

GOAL:
Check customer credit before processing a sales order.

STARTS WHEN:
A new sales order is created.

SKILLS:
1. Get customer credit limit.
2. Check outstanding customer balance.
3. Calculate total credit exposure.
4. Compare exposure with the credit limit.
5. Prepare an approval recommendation.

AUTO WHEN:
Customer credit exposure is within the approved credit limit.

HUMAN WHEN:
Credit limit is exceeded or customer account is blocked.

ESCALATE TO:
Credit Manager.

LOG THESE:
Customer ID, sales order number, credit limit,
outstanding balance, order amount, decision, and reason.







## 2. Employee Leave Request Agent

AGENT NAME:
Employee Leave Request Agent

GOAL:
Check employee leave requests and process them according to company leave policies.

STARTS WHEN:
An employee submits a leave request.

SKILLS:
1. Get employee details.
2. Check available leave balance.
3. Validate leave dates and duration.
4. Check company leave policies.
5. Send the request to the manager for approval.

AUTO WHEN:
The leave request follows company policy and is eligible for automatic approval.

HUMAN WHEN:
Leave balance is insufficient, the leave is longer than permitted, or the request affects important project work.

ESCALATE TO:
Reporting Manager or HR Manager.

LOG THESE:
Employee ID, employee name, leave type, start date, end date, leave balance, approval status, and reason.


## 3. Purchase Requisition Agent

AGENT NAME:
Purchase Requisition Agent

GOAL:
Check purchase requisitions and decide whether to create a purchase order or send it for manager approval.

STARTS WHEN:
A new purchase requisition is submitted.

SKILLS:
1. Read purchase requisition details.
2. Check supplier information.
3. Verify supplier rating.
4. Check requisition amount.
5. Create a purchase order or route it to the manager.

AUTO WHEN:
Supplier is known and rated good, and requisition amount is not above ₹25 lakh.

HUMAN WHEN:
Supplier is new or poor, or requisition amount is above ₹25 lakh.

ESCALATE TO:
Procurement Manager.

LOG THESE:
Requisition ID, supplier name, supplier rating, amount, decision, and reason.


## Partner Review

**Reviewer:** Sindu  
**Date:** 11-Nov-2026

### Feedback

**1. O2C Credit Check Agent**

The design looks good. One thing I noticed is that the agent should check both the customer's pending balance and the new sales order amount before making a decision. If the credit limit is exceeded, it should send the request to the credit manager.

**2. Employee Leave Request Agent**

The agent covers the main leave process. I suggest that urgent leave requests should also be sent to the manager for review, even if the employee does not have enough leave balance. The agent should not reject such requests automatically.

**3. Purchase Requisition Agent**

The design is clear and easy to understand. Before creating a purchase order, the agent should check whether the supplier details and rating are updated. This can help avoid creating orders with incorrect supplier information.

### Risk Identified

The agent may make incorrect decisions if the information in the system is outdated or incomplete.

### Improvement Made

Added extra checks for customer credit exposure, urgent leave requests, and supplier information. Requests involving risks will be sent to the respective manager for approval.