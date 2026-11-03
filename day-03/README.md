# Day 3 – Prompt Engineering Lab

**Name:** Shaik Saniya  
**Topic:** Prompt Engineering Techniques  
**Focus:** Few-shot, Step-by-Step, Role-Based, and JSON Prompting

## Overview

On Day 3, I learned four important prompt-engineering techniques and practised using them for expense classification, invoice data extraction, business calculations, and JSON validation.

## Learning Objectives

- Understand Zero-shot and Few-shot prompting.
- Learn how to use step-by-step instructions.
- Understand role-based prompting.
- Generate structured JSON responses.
- Validate invoice data using Python.

## Tasks Completed

### Task 1 – Expense Classification
- Classified 20 expenses into six company categories.
- Compared Zero-shot and Few-shot prompting.
- Checked the accuracy of the results.

### Task 2 – Invoice Data Extraction
- Generated sample messy invoice data.
- Created an invoice answer key in JSON format.
- Practised writing prompts to extract invoice information.
- Improved prompts to achieve better extraction accuracy.

### Task 3 – Business Money Calculations
- Solved five business problems involving discounts, GST, and freight.
- Compared AI responses with and without step-by-step instructions.
- Verified the answers using Excel.

**Accuracy results:**
- Without step-by-step instructions: 0/5 correct.
- With step-by-step instructions: 5/5 correct.

### Task 4 – Python JSON Validator
Created and executed a Python program to validate invoice JSON files.

The validator checks:
- Required fields.
- Invoice date and due date formats.
- GSTIN length and format.
- Amount data type.
- JSON syntax.

**Execution results:**
- Valid invoice: PASS
- Missing required field: FAIL
- Invalid date: FAIL
- Invalid GSTIN: FAIL

**Validation Summary:** 1 passed, 3 failed.

### Task 5 – Lab Log and Learning Summary
- Prepared the Day 3 lab log.
- Documented completed tasks and accuracy results.
- Identified the most useful prompt-engineering technique.

## Files Included

| File | Description |
|---|---|
| `categories.csv` | Expense classification categories |
| `answer_key.json` | Expected invoice extraction results |
| `prompts.md` | Prompt examples and improvements |
| `validate.py` | Python JSON validation program |
| `valid_invoice.json` | Valid invoice test data |
| `broken_1_missing_field.json` | Invoice with a missing field |
| `broken_2_invalid_date.json` | Invoice with an invalid date |
| `broken_3_invalid_gstin.json` | Invoice with an invalid GSTIN |
| `task4_execution.png` | Python execution screenshot |
| `lab-log.md` | Day 3 learning and task summary |

## Key Learning

I learned that clear instructions and examples help AI produce better results. Step-by-step prompting helped me improve calculation accuracy from 0/5 to 5/5. I also gained practical experience in validating structured invoice data using Python.

## Conclusion

Day 3 helped me understand how to write better prompts, improve AI accuracy, work with JSON data, and use Python for basic data validation.

**Status:** Day 3 Prompt Engineering Lab Completed.
