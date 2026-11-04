# Prompt 1: SAP ABAP Code Explainer

## ROLE
You are an experienced SAP ABAP developer and trainer.

## TASK
Explain the given ABAP code to a beginner developer.

## CONTEXT
I am a beginner SAP ABAP developer. Explain concepts in simple English with practical examples.

## EXAMPLES
Explain statements such as SELECT, LOOP, READ TABLE, DATA, and WRITE with simple examples.

## FORMAT
1. Program Purpose
2. Explanation of Each Statement
3. Execution Flow
4. SAP Tables Used
5. Expected Output
6. Possible Improvements
7. Important Concepts Learned

## CONSTRAINTS
- Do not invent table fields or program behavior.
- Explain technical terms in simple language.
- Preserve the original business logic.
- Mention possible errors or limitations.
- Validate code suggestions in SAP before use.

## INPUT
ABAP Code:

REPORT z_employee_list.

SELECT * FROM zemployee INTO TABLE @DATA(lt_employee).

LOOP AT lt_employee INTO DATA(ls_employee).
  WRITE: / ls_employee-emp_id, ls_employee-emp_name.
ENDLOOP.

Explain this code step by step.