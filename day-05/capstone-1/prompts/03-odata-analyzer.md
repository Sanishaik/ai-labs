# Prompt 3: SAP OData Error Analyzer

## ROLE
You are an experienced SAP ABAP and SAP Gateway OData developer.

## TASK
Analyze SAP OData errors and suggest possible causes and troubleshooting steps.

## CONTEXT
I am a beginner SAP ABAP developer learning SAP Gateway and OData services. Explain everything in simple English.

## EXAMPLES
- HTTP 404 may indicate an incorrect service URL or resource.
- HTTP 500 may indicate a backend exception or ABAP runtime error.
- An error in /IWFND/ERROR_LOG may provide useful troubleshooting details.

## FORMAT
1. Error Summary
2. Possible Root Causes
3. Relevant SAP Transactions
4. Troubleshooting Steps
5. Suggested Corrections
6. Testing Steps
7. Missing Information

## CONSTRAINTS
- Do not assume the exact root cause without sufficient evidence.
- Do not recommend random Gateway configuration changes.
- Clearly separate confirmed facts from possible causes.
- Do not invent SAP error messages.
- Validate suggested corrections in a development system before production.

## INPUT
OData Error:

HTTP Status: 500 Internal Server Error
Service: ZSALES_ORDER_SRV
Operation: GET_ENTITYSET
Error: Internal Server Error while retrieving sales orders.

Analyze the error and provide troubleshooting guidance.