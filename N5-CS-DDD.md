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

#### Pet
{:.no_toc}

| pet_id | name | type | dob|
| -- | -- | -- | -- |
| 1 | Hans | Cat | 2015-09-22 |
| 2 | Minnnie | Gerbil | 2021-05-24 |
| 3	| Bo | Rabbit | 2011-10-13 |
| 4 | Joscelin | Gerbil | 2022-02-19 |

#### Vaccination
{:.no_toc}

| vax_id | pet_id | date| type | reaction |
| -- | -- | -- | -- | -- |
| 1 | 13 | 2019-09-03 | Distemper | True |
| 2 | 5 | 2019-06-23 | Canine hepatitis | False |
| 3 | 1 | 2015-01-17 | Cat Flu | False |
| 4 | 17 | 2011-10-05 | Cat Flu | False |
| 5 | 6 | 2016-12-20 | Feline parvovirus | False |

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
SELECT name, type
FROM pet;
```

## Where (comparison)

To limit the number of rows returned, the `WHERE` keyword is used.

``` sql
SELECT forename, surname
FROM customer
WHERE assistance = "True";
```

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
