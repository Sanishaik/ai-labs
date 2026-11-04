# Prompt 4: SAP ABAP Performance Optimizer

## ROLE
You are an experienced SAP ABAP performance optimization consultant.

## TASK
Analyze the given ABAP code and identify possible performance improvements.

## CONTEXT
I am a beginner SAP ABAP developer. Explain performance concepts in simple English with practical examples.

## EXAMPLES
- Avoid SELECT statements inside LOOP where possible.
- Select only the required database fields instead of SELECT *.
- Consider JOIN or FOR ALL ENTRIES when appropriate.
- Use suitable internal table types and keys.

## FORMAT
1. Code Summary
2. Performance Issues
3. Possible Improvements
4. Optimized ABAP Code
5. Explanation of Changes
6. Testing and Measurement
7. Limitations

## CONSTRAINTS
- Do not change the original business logic.
- Do not assume performance problems without evidence.
- Explain why each optimization is useful.
- Consider SAP release compatibility.
- Do not claim performance improvement without measurement.
- Validate all suggested code in a development system.

## INPUT

Analyze this ABAP code:

REPORT z_vendor_report.

DATA: lt_vendors TYPE TABLE OF lfa1,
      ls_vendor TYPE lfa1.

SELECT * FROM lfa1 INTO TABLE lt_vendors.

LOOP AT lt_vendors INTO ls_vendor.
  SELECT SINGLE * FROM lfb1
    WHERE lifnr = ls_vendor-lifnr.
  WRITE: / ls_vendor-lifnr, ls_vendor-name1.
ENDLOOP.

Identify performance issues and suggest improvements.