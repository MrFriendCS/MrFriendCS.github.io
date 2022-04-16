# N5 Computing Science
{:.no_toc}

[SDD](index.md)
[Higher](H-CS-SDD.md)

## Database Design and Development
{:.no_toc}

___Work in Progress___

All the code examples use SQLite.  They will work with [Replit](https://replit.com/) and [DB Browser for SQLite](https://sqlitebrowser.org/).

**Note:** These notes are focused on N5 Computing Science so some terms are used differently.

**Note:**  SQLite, and SQL, keywords are case insensitive.  The following are all equally valid:

``` sql
SELECT
```
``` sql
SeLeCt
```

``` sql
select
```

In the examples, the keywords will be in uppercase.

## Table of Contents {#toc}
{:.no_toc}

* TOC will be displayed here
{:toc}

### Attribute types (Data types)

SQLite has fewer data types than SQL.  SQLite has:

* Text
* Integer
* Real

The `text` datatype can be used for:

* Date: "2022-08-15"
* Boolean: "True", "False"

### Example Data

The data used in the examples is from the following tables:

#### Customer
{:.no_toc}

| customer_id | forename| surname | assistance |
| -- | -- | -- | -- |
| c1 | Alan | Mitchell | False |
| c2 | Beth | Nicolson | True |
| c3 | Carl | Osswald | True |
| c4 | Dina | Peters | False |

#### Ticket
{:.no_toc}

| ticket_id | customer_id| date| xxx |
| -- | -- | -- | -- |
| t1 | p1 |  |  |
| t2 | p2 |  |  |
| t3 | p1 |  |  |
| t4 | p3 |  |  |
| t5 | p4 |  |  |

## Display information

It is possible to display simple messages using the `.print` command.

``` sql
.print A message
```

## Select

A basic select statement uses two keywords `SELECT` and `FROM`.   

```
SELECT column(s)
FROM table(s)
```

To select everything in a table the `*` symbol is used.

``` sql
SELECT *
FROM customer;
```

To select one, or more columns, their names are used.

``` sql
SELECT forename, surname
FROM customer;
```


## from

## where



[Back to Table of Contents](#toc)

## AND, OR, <, >, =



[Back to Table of Contents](#toc)

## Order by with a maximum of two fields



[Back to Table of Contents](#toc)

## Insert

This command will insert a row, or multiple rows, into a table.  All validation rules must be met for the row to be added.

``` sql
INSERT INTO 
```

[Back to Table of Contents](#toc)

## Update



[Back to Table of Contents](#toc)

## Delete



[Back to Table of Contents](#toc)

## Equi-join between tables

Tables are joined using the Primary Key of each table, where the primary keys are equal.

``` sql
SELECT *
WHERE table1.primary_key = table2.primary_key
```

[Back to Table of Contents](#toc)
