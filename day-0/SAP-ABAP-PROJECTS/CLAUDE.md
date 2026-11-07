# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single SAP ABAP report, `ZPO_OPEN_LIST.abap` (Project 1 in `README.md`), that lists purchase order header/item data with an ALV grid. There is no build system, package manifest, linter, or test suite. Nothing here runs outside an SAP system.

- To run it, paste the source into an ABAP program in SE38/SE80 on an SAP system with the standard purchasing tables and execute it (F8). Debugging is done with breakpoints in the ABAP editor, as the screenshots in the README show.
- Validate changes by reading them and, if available, by syntax-checking in the ABAP editor (Ctrl+F2). There is no command-line check.

## Code structure (`ZPO_OPEN_LIST.abap`)

The file is organized into numbered sections. The order matters in ABAP: the class definition comes before the selection screen, and the implementation comes after both.

1. **Local class `lcl_po_report`**: `get_data` is public and `display_alv` is private. `get_data` runs the query and calls `display_alv` when rows are found. `display_alv` builds the grid with `CL_SALV_TABLE=>factory`, turns on all functions, optimizes columns, sets the list header, and displays it. Errors from `cx_salv_msg` are shown as an `E` message.
2. **Types**: `ty_po` is the row structure for the output table. Each field is typed from an `EKKO`, `EKPO`, or `LFA1` column.
3. **Globals**: `gt_po` is the result table. The `gv_*` fields exist only to type the selection-screen ranges.
4. **Selection screen**: block `b1` (framed, title `text-001`) with four `SELECT-OPTIONS` (`s_ebeln`, `s_lifnr`, `s_bedat`, `s_werks`).
5. **Class implementation**: the single data-access path is one `SELECT` joining `EKKO` (alias `a`) to `EKPO` (`b`) as an inner join, and `LFA1` (`c`) as a left outer join for the vendor name. Filters use `@`-escaped host variables. The result goes `INTO CORRESPONDING FIELDS OF TABLE`.
6. **`START-OF-SELECTION`**: creates the report object and calls `get_data`.

## Things to know before editing

- **Program name mismatch.** The `REPORT` statement says `ZSS_PO_OPEN_LIST`, while the file name and the README say `ZPO_OPEN_LIST`. Decide which name is correct before creating the program in SAP, because `REPORT` names must match the program name there.
- **`text-001` needs a text symbol** in the program's text elements, or the frame title will be empty.
- **`MAKT` is documented but not read.** The README lists `MAKT` (material descriptions) as a table used, but the query uses `EKPO-TXZ01` for the item text and does not join `MAKT`.
- **Old-style syntax in places**: `CREATE OBJECT` and `CALL METHOD` are used alongside the newer `@` host-variable syntax. Keep the style consistent with the code around the change.
- The `README.md` repository tree is out of date. It lists only `day-01/`, while the parent `ai-labs/` directory now has several `day-*` folders.
