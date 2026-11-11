# Code Review: `abap_code.abap` (report `ZSS_PO_OPEN_LIST`)

Scope: read-only review. `abap_code.abap` was not modified. The code was not compiled, run, or checked against an SAP system. Statements below are based on reading the source and on general ABAP knowledge.

---

## 1. What the program does (beginner-friendly)

Think of this program as a small "search and show" tool for purchase orders (POs) in SAP.

1. **Selection screen.** When you run it, a form appears with four search boxes (in one framed block):
   - PO number (`s_ebeln`)
   - Vendor number (`s_lifnr`)
   - PO date (`s_bedat`)
   - Plant (`s_werks`)
2. **Start of selection.** The program creates an object of the local class `lcl_po_report` and calls its `get_data` method.
3. **Reading the data.** `get_data` reads the database tables:
   - `EKKO` (PO headers: number, date, vendor, currency)
   - `EKPO` (PO items: item number, material, text, plant, quantity, unit, net value). Joined to the header on the PO number.
   - `LFA1` (vendor master: vendor name). Joined as "optional", so a PO still appears if the vendor name is missing.
   - The rows are stored in the internal table `gt_po`, whose line layout is `ty_po`.
4. **Showing the result.**
   - If rows were found, `display_alv` opens a standard SAP ALV grid (a sortable, filterable table) with the title "Open Purchase Order List".
   - If no rows were found, a status-bar message says "No purchase order items found".

---

## 2. Obsolete statements

These are genuinely older forms. The code still compiles and runs, but newer ABAP has a cleaner replacement.

| Line | Statement | Why it is considered old | Modern replacement |
|---|---|---|---|
| 101 | `CREATE OBJECT go_po_report.` | Old object-creation syntax from before ABAP 7.40. | `go_po_report = NEW lcl_po_report( ).` |
| 83–87 | `CALL METHOD cl_salv_table=>factory IMPORTING ... CHANGING ...` | `CALL METHOD` is an older calling style. However, `factory` returns its result through an `IMPORTING` parameter (no `RETURNING`), so a functional call is **not** possible here. This is not a real replacement candidate. | Keep `CALL METHOD` for this call. |
| 73 | `INTO CORRESPONDING FIELDS OF TABLE @gt_po` | Not forbidden, but it makes the database layer match fields by name at runtime and is slower. It is not the recommended form when the field list is explicit. | `INTO TABLE @gt_po`. This works here because the SELECT list already matches `ty_po` in both order and type. |

Notes:
- The code contains **no** `MOVE`, `COMPUTE`, `WRITE TO`, `FORM/PERFORM`, `CONCATENATE`, `TABLES`, `OCCURS`, `HEADER LINE`, or `SELECT ... ENDSELECT`. Those would be the clear obsolete statements. Their absence matters: this code is already written in fairly modern style.
- The `@` host-variable escape in the SELECT and `DATA(lx_salv)` inline declaration are modern syntax (ABAP 7.40 SP05+ and later). They should **not** be called obsolete.
- Whether `CREATE OBJECT` and `CALL METHOD` are flagged depends on your ATC / Code Inspector variant. Check your system's check variant before treating them as errors.

---

## 3. Modern statements and recommended improvements

Statements already modern and good:
- `SELECT ... FROM ... INNER JOIN ... LEFT OUTER JOIN ... WHERE ... IN @range` (Open SQL with host-variable escape `@`)
- `DATA(lx_salv)` inline declaration
- `TRY ... CATCH cx_salv_msg ... ENDTRY` for exception handling
- Method chaining: `go_salv->get_functions( )->set_all( abap_true )`
- Local class with `PUBLIC` / `PRIVATE` sections

Recommended improvements (not errors):

1. **Use `NEW` instead of `CREATE OBJECT`** (line 101):
   ```abap
   go_po_report = NEW lcl_po_report( ).
   ```
2. **ALV factory call (lines 83–87): keep as is.** Because `factory` has no `RETURNING` parameter, `CALL METHOD` is the correct form. Do not rewrite it as a functional call. Also check whether the ALV factory's exception class (`cx_salv_msg`) is the right one to catch. Some ALV methods raise other `cx_salv_*` exceptions; a superclass catch (`cx_salv_error`, if it exists in your release) would be more robust.
3. **Use `INTO TABLE @gt_po`** (line 73). Remove `CORRESPONDING FIELDS OF` because the SELECT list already matches `ty_po`. Keep the column order in sync with `ty_po` if you do this. A future field change would break silently, so a comment or a dedicated structure is worth adding.
4. **Remove the redundant `CLEAR gt_po`** (line 52). `SELECT ... INTO TABLE` replaces the target table, so the CLEAR does nothing useful.
5. **Show currency and unit in the ALV.** `NETWR` (value) and `MENGE` (quantity) are shown without their currency and unit reference. Set them after the columns are created:
   ```abap
   DATA(lo_cols) = go_salv->get_columns( ).
   CAST cl_salv_column_table( lo_cols->get_column( 'NETWR' ) )->set_currency_column( 'WAERS' ).
   CAST cl_salv_column_table( lo_cols->get_column( 'MENGE' ) )->set_unit_column( 'MEINS' ).
   ```
6. **Add a usage message to the selection screen** only if you need one. Not required.
7. **Use an explicit message class** instead of plain text in `MESSAGE '...' TYPE 'S'` (lines 77, 93). This supports translation and consistency. Optional.
8. **Keep text symbol `text-001`** maintained in the Text Elements (Goto → Text Elements → Selection Texts). Missing text symbols show as `???` on the screen. This cannot be verified from the source alone.
9. **Formatting nit:** line 90 has a space before `)` inside `set_list_header('...' )`. Cosmetic only.

---

## 4. Possible errors and performance issues

### 4.1 Logic error: "Open" list is not filtered for open items (most important)

The title says "Open Purchase Order List", but the SELECT has **no condition for open status**. It returns all PO items that match the selection, including:
- Items marked for deletion (`EKPO-LOEKZ = 'L'`)
- Items whose delivery is complete (`EKPO-ELIKZ = 'X'`)
- Items already closed or fully invoiced (`EKPO-ERECZ`/final-invoice indicators, depending on what "open" means for your business)

Users will see closed and deleted items under an "Open" title. What "open" means is a business decision. A typical starting point is:

```abap
AND b~loekz = @space      " not deleted
AND b~elikz = @space      " delivery not completed
```

Confirm the rule with the business owner before you add it.

### 4.2 Authorization is not checked (security / compliance)

PO data is sensitive. The program reads `EKKO`/`EKPO`/`LFA1` and displays them without any `AUTHORITY-CHECK`. In a real SAP system, users should be restricted by their PO display authorizations (for example, object `M_BEST_EKG` for purchasing group and `M_BEST_WRK` for plant, depending on your role design). Without a check, anyone who can run the report sees all PO data within the selection.

Recommended: add an `AUTHORITY-CHECK` for each relevant field before the SELECT, and skip or exclude records the user is not allowed to see. Confirm the exact object and field names with your security team. Do not copy the object names above into production without checking them.

### 4.3 No protection against very large selections (performance)

The selection screen has no mandatory input. If the user presses Execute with empty fields, the query reads **every** PO item in the system. This can be slow and may use a lot of memory.

Recommendations:
- Make at least one selection criterion mandatory (for example, `OBLIGATORY` on `s_werks` or `s_bedat`). The ABAP keyword `OBLIGATORY` goes on the SELECT-OPTIONS line.
- Or add a row limit, for example `UP TO 5000 ROWS`, with a warning message when the limit is reached.

### 4.4 Performance of the join and filters

- Filters on `EKKO-BEDAT`, `EKKO-LIFNR`, `EKKO-EBELN`, and `EKPO-WERKS` are reasonable starting points because they match common indexes. Check the actual indexes in your system with SE11/ST05 before tuning further.
- The `LEFT OUTER JOIN` on `LFA1` is a correct choice. Vendor names are looked up for each row, which is acceptable for a small result set. For very large results, read `LFA1` into a sorted or hashed table once instead.
- `INTO CORRESPONDING FIELDS OF` adds runtime mapping overhead (see §2). Small effect, but it is free to remove.
- No `ORDER BY` is given. That is fine for an ALV, which sorts on the client side.

### 4.5 Smaller robustness points

- **Exception handling is narrow.** Only `cx_salv_msg` is caught. Other ALV errors (for example, failures from `get_columns` or `get_display_settings`) would dump the program. Consider catching the broader ALV exception class if your release has one.
- **Message type `'E'` in the ALV method.** Once `MESSAGE ... TYPE 'E'` runs inside a method, the report ends at that point. That is acceptable for an error, but the message text comes from `lx_salv->get_text( )`, which is fine.
- **`MESSAGE 'No purchase order items found' TYPE 'S'`.** This shows the message on the next screen and the program then ends with no list, which is the correct behaviour. Some teams prefer `TYPE 'S' DISPLAY LIKE 'W'` so the message looks like a warning.
- **`gv_*` variables** exist only to type the select-options. This is a common and acceptable pattern.
- **Unused fields in `ty_po`?** All fields are used in the SELECT and the ALV. No unused fields found.

### 4.6 Things I could not verify from the source

- Whether `text-001` exists as a text symbol (§3, item 8).
- Whether the program compiles cleanly in your release. The code uses `@` host variables and inline `DATA()`, so it needs ABAP 7.40 SP05 or later.
- Whether the database indexes match the filters.

---

## 5. Summary

| Category | Finding | Severity |
|---|---|---|
| Logic | "Open" list does not filter open or non-deleted items | High |
| Security | No `AUTHORITY-CHECK` on PO data | High |
| Performance | No mandatory selection or row limit; can read everything | Medium |
| Obsolete syntax | `CREATE OBJECT` (line 101) | Low (style) |
| Obsolete syntax | `CALL METHOD` (lines 83–87) | Low (style); no functional alternative exists for `factory` |
| Obsolete syntax | `INTO CORRESPONDING FIELDS OF` (line 73) | Low (style / performance) |
| Presentation | Currency and unit not linked to amount and quantity columns | Low |
| Robustness | Narrow exception catch around ALV calls | Low |
| Hygiene | Redundant `CLEAR gt_po`; cosmetic spacing | Very low |

No statements were invented as obsolete. The code uses mostly modern Open SQL and ALV syntax. The clearly older parts are the three style items above.
