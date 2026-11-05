# DAY 06 – TASK 1
## Claude Code: Project Analysis, Plan Mode and Risk Identification

**Name:** Shaik Saniya  
**Training:** Resoftwa – Future-Ready Tech Training Program  
**Task:** Repeat the class activity on Phase 1 ABAP code using `/init`, Plan Mode, code explanation and risk identification.

---

## 1. Objective

The objective of this task was to learn how Claude Code analyzes existing projects, explains code structure, identifies possible risks and creates project-specific instructions using the `/init` command.

I completed this activity on two existing projects:

1. Phase 1 – SAP ABAP Project
2. CAP – Purchase Order Service Project

## 2. Project 1 – Phase 1 SAP ABAP Project

**Project location:**
`SAP-ABAP-Projects/`

**Main ABAP file:** `ZPO_OPEN_LIST.abap`

### Activities performed

1. Opened the Phase 1 SAP ABAP project in Claude Code.
2. Executed the `/init` command.
3. Claude analyzed the project and generated `CLAUDE.md`.
4. Switched to Plan Mode using `Shift + Tab`.
5. Asked Claude to explain the ABAP program, describe its execution flow and identify possible risks without modifying the source code.

**Generated file:** `SAP-ABAP-Projects/CLAUDE.md`

## 3. ABAP Program Explanation

The `ZPO_OPEN_LIST.abap` program displays purchase order header and item information using an ALV grid.

### SAP tables used

| Table | Purpose |
|---|---|
| EKKO | Purchase order header information |
| EKPO | Purchase order item information |
| LFA1 | Vendor information |

### Program execution flow

1. The user enters selection criteria such as purchase order number, vendor, date and plant.
2. `START-OF-SELECTION` creates the report object.
3. The `get_data` method retrieves purchase order information.
4. The program joins EKKO, EKPO and LFA1.
5. The retrieved records are stored in an internal table.
6. If records are available, `CL_SALV_TABLE` displays the ALV output.
7. If no records are found, an appropriate message is displayed.

## 4. Risks Identified by Claude

| No. | Risk | Explanation |
|---|---|---|
| 1 | Program name mismatch | The file is `ZPO_OPEN_LIST.abap`, but the REPORT statement uses `ZSS_PO_OPEN_LIST`. |
| 2 | Missing text symbol | `text-001` must be maintained in the program text elements. |
| 3 | Open PO description | The program does not filter only open purchase orders. |
| 4 | Performance | Retrieving large amounts of purchase order data may affect performance. |
| 5 | Authorization | The program does not contain an authorization check. |
| 6 | Error handling | The SALV error handling should be reviewed. |
| 7 | Documentation mismatch | The README mentions MAKT, but the program does not join MAKT. |

## 5. Recommendations

Claude suggested the following improvements:

- Correct the program name mismatch.
- Define the criteria for open purchase orders.
- Add suitable authorization checks.
- Restrict unnecessary data retrieval.
- Maintain the required text symbols.
- Improve ALV column headings and display settings.
- Update the README documentation.

**Note:** This was a read-only analysis. No ABAP source code was modified.

## 6. Project 2 – CAP Purchase Order Service

**Project location:** `day-0/po-service/`

This project is a SAP CAP Node.js application for managing purchase orders and vendor information.

### Main project files

| File | Purpose |
|---|---|
| `db/schema.cds` | Defines the data model and entities. |
| `srv/po-service.cds` | Defines the OData service. |
| `srv/po-service.js` | Contains business logic and event handlers. |
| `db/data/` | Contains vendor and purchase order sample data. |
| `test/po.http` | Contains HTTP requests for testing. |
| `package.json` | Contains project dependencies and scripts. |
| `readme.md` | Project documentation. |

## 7. Executed /init in the CAP Project

I opened the CAP PO Service project in Claude Code and executed `/init`.

Claude analyzed the project structure and generated another `CLAUDE.md` file.

**Generated file:** `day-0/po-service/CLAUDE.md`

The file describes:

- Project architecture and folder structure.
- Data model and service definitions.
- Purchase order and vendor entities.
- Business logic in the JavaScript handler.
- Commands to install dependencies and run the application.
- Important project observations and possible issues.

## 8. Important CAP Project Observations

1. The application rejects purchase order amounts less than or equal to zero during CREATE.
2. The `isLate` field is calculated during READ.
3. The `isLate` field is virtual and cannot be directly used in database filtering with `$filter`.
4. The root-level `po_list.csv` and `vendors.csv` files are not automatically loaded as CAP seed data from their current location.
5. The README example using `$filter=isLate eq true` needs to be reviewed because `isLate` is virtual.

## 9. Files Generated

Two project-specific instruction files were generated.

| No. | File | Project |
|---|---|---|
| 1 | `CLAUDE.md` | Phase 1 SAP ABAP Project |
| 2 | `CLAUDE.md` | CAP PO Service Project |

### Folder structure

```text
ai-labs/
│
├── SAP-ABAP-Projects/
│   └── CLAUDE.md
│
├── day-0/
│   └── po-service/
│       └── CLAUDE.md
│
└── day-06/
    └── README.md
```

## 10. GitHub Submission

Both project-specific `CLAUDE.md` files were committed and pushed successfully to the GitHub repository.

**Repository:** https://github.com/Sanishaik/ai-labs  
**Branch:** `main`

Previous commit messages:

- `Add CLAUDE.md for Phase 1 SAP ABAP project`
- `Add CLAUDE.md for CAP PO service project`

## 11. Screenshots

The following screenshots are used as proof of task completion:

1. **Screenshot 1 – Phase 1 ABAP Project:** ABAP project opened in Claude Code.
2. **Screenshot 2 – /init Execution:** Successful `/init` execution and ABAP project's `CLAUDE.md`.
3. **Screenshot 3A – Plan Mode Program Explanation:** Claude explaining the ABAP program and execution flow.
4. **Screenshot 3B – Plan Mode Risk Identification:** Claude identifying risks and suggesting improvements.
5. **Screenshot 4 – CAP PO Service Project:** CAP project and its generated `CLAUDE.md`.
6. **Screenshot 5 – GitHub Submission:** Both `CLAUDE.md` files or successful Git push output.

## 12. What I Learned

Through this task, I learned:

- How to use `/init` to analyze an existing project and create `CLAUDE.md`.
- How to use Plan Mode to understand code without modifying it.
- How to understand the execution flow of an ABAP report.
- How to identify possible coding, performance and authorization risks.
- How Claude Code can analyze both SAP ABAP and CAP projects.
- Why AI-generated suggestions should be reviewed before applying them.

## 13. Conclusion

I successfully completed Day 06 Task 1 by executing `/init` on two existing projects and using Plan Mode to analyze the Phase 1 ABAP program.

I understood the ABAP program flow, identified potential risks and generated two project-specific `CLAUDE.md` files.

**Task Status:** Completed