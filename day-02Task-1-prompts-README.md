# Day 2 - Prompt Engineering

## Task 1: Fix 5 More Prompts

### Prompt 1: Explain EKKO and EKPO

**Before:**
Explain EKKO and EKPO.

**After:**
**ROLE:** You are a senior SAP ABAP trainer.

**TASK:** Explain the EKKO and EKPO tables to a new joiner.

**CONTEXT:** The reader is new to SAP ABAP and learning purchase order data.

**EXAMPLES:** Use one purchase order containing two items.

**FORMAT:** Present a table showing each table's purpose and important fields, followed by a short example.

**CONSTRAINTS:** Use simple English and stay under 200 words.

**Blocks added:**
Role, Task, Context, Examples, Format, Constraints

---

### Prompt 2: Write Test Cases

**Before:**
Write test cases.

**After:**
**ROLE:** You are an SAP functional tester.

**TASK:** Write five test cases for purchase order approval.

**CONTEXT:** The test cases are for an SAP purchase order approval process.

**EXAMPLES:** Include approval and rejection scenarios.

**FORMAT:** Present a table with Test Case ID, Scenario, Steps, and Expected Result.

**CONSTRAINTS:** Provide exactly five test cases in simple English.

**Blocks added:**
Role, Task, Context, Examples, Format, Constraints

---

### Prompt 3: Write an Email

**Before:**
Write email.

**After:**
**ROLE:** You are a professional employee.

**TASK:** Write an email to my manager explaining that my transport request will be delayed by one day.

**CONTEXT:** The planned completion date cannot be met.

**EXAMPLES:** Politely apologize and promise an update.

**FORMAT:** Include a subject, email body, and closing.

**CONSTRAINTS:** Use a professional tone and stay under 100 words.

**Blocks added:**
Role, Task, Context, Examples, Format, Constraints

---

### Prompt 4: Explain ABAP Code

**Before:**
Explain this code.

**After:**
**ROLE:** You are a senior SAP ABAP developer.

**TASK:** Explain the ABAP code I provide step by step.

**CONTEXT:** The reader is an ABAP beginner.

**EXAMPLES:** Use a small example to explain a complex statement.

**FORMAT:** Present the explanation in numbered steps followed by a short summary.

**CONSTRAINTS:** Use simple English, identify potential errors, and ask me for the code if it is missing.

**Blocks added:**
Role, Task, Context, Examples, Format, Constraints

---

### Prompt 5: Give Test Data

**Before:**
Give test data.

**After:**
**ROLE:** You are an SAP ABAP test data specialist.

**TASK:** Create ten fictional vendor records for testing an SAP report.

**CONTEXT:** The records will be used to test vendor data processing.

**EXAMPLES:** Include fictional vendors from different cities.

**FORMAT:** Return a valid JSON array containing Vendor ID, Vendor Name, City, Country, and Payment Terms.

**CONSTRAINTS:** Provide exactly ten fictional records and do not use real personal information.

**Blocks added:**
Role, Task, Context, Examples, Format, Constraints

---

## Task 1 Summary

I rewrote five weak prompts using the six building blocks: Role, Task, Context, Examples, Format, and Constraints.

The improved prompts specify the AI's role, the task to complete, the background, an example, the required output format, and the rules to follow.

This makes the instructions clearer and helps produce more relevant, structured answers.
