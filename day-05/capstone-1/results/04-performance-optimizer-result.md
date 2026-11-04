# ABAP Performance Review: `Z_VENDOR_REPORT`

## 1. Code Summary

The program reads vendor master records from table **LFA1** and prints each vendor's number and name. For each vendor, it also runs a database read on **LFB1** (vendor company-code data).

The steps are:
1. Read **all** rows and **all** columns of LFA1 into an internal table.
2. Loop over that table.
3. For each vendor, run one `SELECT SINGLE` on LFB1.
4. Write the vendor number and name to the list.

**Important observation:** The result of the LFB1 select (`sy-subrc` and the fields it reads) is never used. The output depends only on `lifnr` and `name1` from LFA1. So the LFB1 read currently has no visible effect on the report output. Keep this in mind when you read the optimization section.

---

## 2. Performance Issues

| # | Issue | Where | Why it matters |
|---|---|---|---|
| 1 | **Database access inside a LOOP** (the "N+1 query" pattern) | `SELECT SINGLE ... FROM lfb1` inside `LOOP AT` | If there are 50,000 vendors, the program sends about 50,000 separate database requests. Each request has network and database overhead. This is usually the largest cost in this