---
name: explain-cds
description: Explains SAP ABAP CDS Views to beginners in simple English, step by step. Covers concepts, syntax, annotations, associations, and small practical examples. Use when the user asks what CDS views are, how to read or write ABAP CDS DDL, or how annotations or associations work.
---

# Explain ABAP CDS Views (Beginner Friendly)

When this skill is active, teach ABAP CDS views in simple English. Use short sentences and plain words. Introduce one idea at a time. Define any jargon the first time you use it. After each idea, show a small code example. If you are not sure about a detail of the SAP system, say so instead of guessing.

## Step 1: What is a CDS view?

CDS stands for **Core Data Services**. A CDS view is a named, reusable query written in the ABAP CDS language. You define it once in the ABAP system. Then reports, apps, and OData services can read data through it.

Think of a CDS view as a **window** onto one or more database tables. It does not copy the data. It reads the tables when someone uses it.

## Step 2: Basic syntax

```abap
@EndUserText.label: 'Flight connections'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity ZI_FlightConnection
  as select from sflight
{
  key carrid as Airline,
  key connid as Connection,
  key fldate as FlightDate,
      seatsmax as SeatsMax,
      seatsocc as SeatsOccupied
}
```

What each part means:
- `define view entity <name>` gives the view its name.
- `as select from <table>` says where the data comes from.
- The curly braces `{ }` hold the list of columns you expose.
- `key` marks a column that identifies one row. Every view needs at least one key field.
- `as` gives a column a new, friendlier name (an alias).

## Step 3: Filtering and calculated fields

```abap
@EndUserText.label: 'Flights with free seats'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity ZI_FreeSeats
  as select from sflight
{
  key carrid as Airline,
  key connid as Connection,
  key fldate as FlightDate,
      seatsmax - seatsocc as FreeSeats
}
where seatsocc < seatsmax
```

- `where` keeps only the rows that match a condition. It goes after the `{ }` block.
- `seatsmax - seatsocc` is a **calculated field**. The view computes it on the fly. It is not stored anywhere.

## Step 4: Parameters (inputs to the view)

```abap
@EndUserText.label: 'Flights by airline'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity ZI_FlightsByAirline
  with parameters
    p_airline : abap.char(3)
  as select from sflight
{
  key carrid as Airline,
  key connid as Connection,
  key fldate as FlightDate
}
where carrid = $parameters.p_airline
```

Parameters let the caller pass a value in. Inside the view, you read a parameter with `$parameters.<name>`.

## Step 5: Joins (combining two tables)

```abap
@EndUserText.label: 'Flights with airline name'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity ZI_FlightWithAirline
  as select from sflight
  inner join scarr on scarr.carrid = sflight.carrid
{
  key sflight.carrid as Airline,
  key sflight.connid as Connection,
  scarr.carrname     as AirlineName
}
```

An `inner join` keeps only rows that match on both sides. A `left outer join` keeps every row from the left table, even when there is no match on the right.

## Step 6: Associations (links you follow when needed)

An **association** is a named link from one view to another. It works like a foreign key you can follow later. The join runs only when a consumer uses a field from the linked view. That is why associations are often faster than joins.

First, a small target view:

```abap
@EndUserText.label: 'Airline'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity ZI_Airline
  as select from scarr
{
  key carrid   as Airline,
      carrname as AirlineName
}
```

Then the flight view, which links to it:

```abap
@EndUserText.label: 'Flight with association'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity ZI_Flight
  as select from sflight
  association [1..1] to ZI_Airline as _Airline
    on $projection.carrid = _Airline.Airline
{
  key carrid,
  key connid,
  key fldate,
      _Airline
}
```

Key points:
- `association [1..1] to <target> as _Airline` defines the link. The name starts with an underscore by convention.
- `[1..1]` is the **cardinality**: each flight has exactly one airline. Other common values are `[0..1]` (zero or one) and `[*]` (many).
- `on $projection.carrid = _Airline.Airline` says how the two views match.
- Listing `_Airline` in the `{ }` block exposes the link to consumers.
- A consumer reads the target's fields with a **path expression**, such as `_Airline.AirlineName`.

## Step 7: Annotations (metadata with @)

Annotations start with `@`. They add information to the view or a field. They do not change the data. Other tools, such as SAP Fiori apps and OData services, read them.

Common examples:
- `@EndUserText.label: 'text'` gives a human-readable label.
- `@AccessControl.authorizationCheck: #NOT_REQUIRED` is required for view entities. Other values are `#CHECK` and `#NOT_ALLOWED`.
- `@OData.publish: true` exposes the view as an OData service.
- `@UI.lineItem: [{ position: 10 }]` placed above a column tells a Fiori list to show that column, in order.

Placement rule:
- Above `define view entity`: applies to the whole view.
- Above a column in the `{ }` block: applies to that column only.

```abap
define view entity ZI_FlightUI
  as select from sflight
{
  @UI.lineItem: [{ position: 10 }]
  key carrid as Airline,
  @UI.lineItem: [{ position: 20 }]
  key connid as Connection
}
```

## Step 8: Naming layers (optional convention)

SAP projects often use prefixes to show a view's role:
- `I_` or `ZI_`: basic/interface view, a clean reusable building block.
- `C_` or `ZC_`: consumption view, shaped for one app or service.

These are conventions, not rules. The syntax works with any name.

## Step 9: Common beginner mistakes

1. Forgetting `key` fields. Views need at least one.
2. Forgetting `@AccessControl.authorizationCheck` on a view entity.
3. Expecting an association to join every time. It joins only when a field from the target is used.
4. Using `where` before the `{ }` block. It belongs after it.
5. Mixing up `$parameters.` (inputs) with `$projection.` (inside association conditions).

## Step 10: Quick recap and next step

- A CDS view is a reusable, named query.
- Structure: `define view entity`, `as select from`, `{ columns }`, `where`.
- `key` identifies rows. `as` renames. Calculated fields compute values.
- Parameters pass inputs.
- Associations link views and join on demand.
- Annotations add metadata with `@`.

End by asking the learner which topic they want to practice next, or offer a short exercise: "Write a view that lists flights with more than 100 seats."
