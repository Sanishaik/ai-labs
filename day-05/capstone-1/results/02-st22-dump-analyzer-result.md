# SAP ST22 Dump Analysis: ZEMPLOYEE_REPORT

## 1. Error Summary

| Item | Value (from your input) |
|---|---|
| Runtime error | GETWA_NOT_ASSIGNED |
| Exception | CX_SY_REF_IS_INITIAL |
| Program | ZEMPLOYEE_REPORT |

**Fact:** The program stopped with a runtime error. Two different kinds of problems are named here.

**Note:** These two names normally point to different problems, one with field symbols and one with object references. Check in ST22 whether both appear in the same dump. The "Runtime Errors" and "Exception" fields are at the top of the dump. If they come from different dumps, analyze each one separately.

## 2. Meaning of the Runtime Error

**GETWA_NOT_ASSIGNED** (field symbols):
- A **field symbol** is like a named pointer to some data. It must be connected ("assigned") to a memory area before use.
- If you use a field symbol that has not been assigned, ABAP raises this error.
- A common cause is an `ASSIGN` statement that failed. ABAP does not stop at the failed `ASSIGN`. It only sets `sy-subrc` to a non-zero value. The program stops later, when the field symbol is used.

**CX_SY_REF_IS_INITIAL** (object references):
- An **object reference** is a variable that points to an object, such as a class instance.
- "Initial" means the reference is empty (null). It does not point to anything yet.
- If your code calls a method on an initial reference, or reads an attribute from it, ABAP raises this exception.

**Simple analogy:** A field symbol is like a sticky note that says "go to shelf 5." If nothing is on shelf 5, the note points nowhere. An initial reference is like an empty envelope. You cannot read a letter from an envelope that has no letter in it.

## 3. Possible Root Causes

*These are possibilities, not confirmed causes. Only the full dump can show which one applies.*

**For GETWA_NOT_ASSIGNED:**
- `ASSIGN` was used (for example, `ASSIGN ... TO <fs>`) and `sy-subrc` was not checked.
- `READ TABLE ... ASSIGNING <fs>` found no matching row, and the result was not checked.
- `ASSIGN COMPONENT` tried to access a field name that does not exist in the structure.
- A field symbol was used outside the block where it was assigned, for example after a `LOOP` ended.
- A data type mismatch made the `ASSIGN` fail.

**For CX_SY_REF_IS_INITIAL:**
- An object was never created (no `NEW`, `CREATE OBJECT`, or factory call) before it was used.
- A method returned an initial reference, and the caller did not check it.
- A conditional branch skipped the object creation, but the later code still used the object.
- A reference was cleared or reset earlier in the program.

## 4. Relevant Source Code Areas

I do not have the source code of ZEMPLOYEE_REPORT, so I cannot point to specific lines. Look in these places:

1. **Source Code Extract** in ST22: the lines around the error. The dump marks the failing statement with an arrow or highlight.
2. **Call Stack** in ST22: shows which form, method, or event called the failing code.
3. **Program/Include name** in the dump: tells you which include holds the error.
4. **Statements to search for in the code:**
   - `ASSIGN`, `ASSIGNING`, `ASSIGN COMPONENT`
   - `READ TABLE ... ASSIGNING`
   - `LOOP AT ... ASSIGNING`
   - `CREATE OBJECT`, `NEW`, or factory methods
   - Method calls using `->`, and attribute reads such as `obj->attribute`

## 5. Suggested Corrections

Follow these steps in a **development system**. Do not change production directly.

**Step 1: Find the exact failing line.**
Open ST22, go to the Source Code Extract, and note the line number and variable name.

**Step 2: Identify the variable.**
- If the variable starts with `<`, it is a field symbol. Look at the `ASSIGN` or `READ TABLE` statement that should have set it.
- If the variable is a normal name such as `lo_employee`, it is an object reference. Look at where it is created.

**Step 3: Add a check after the statement that fills the field symbol.** *(Illustrative pattern, not your code.)*

```abap
READ TABLE lt_employees ASSIGNING <ls_employee>
     WITH KEY pernr = lv_pernr.
IF sy-subrc <> 0.
  " Handle the 'not found' case, e.g. write a message and exit
  RETURN.
ENDIF.
```

**Step 4: Check that the field symbol is assigned before use.** *(Illustrative pattern.)*

```abap
IF <ls_employ