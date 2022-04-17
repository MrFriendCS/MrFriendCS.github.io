# N5 Computing Science
{:.no_toc}

[SDD](index.md)
[Higher](H-CS-SDD.md)

## Database Design and Development
{:.no_toc}

___Work in Progress___

All the code examples use SQLite.  They will work with [Replit](https://replit.com/) and [DB Browser for SQLite](https://sqlitebrowser.org/).

**Note:** These notes are focused on N5 Computing Science so some terms are used differently.

SQLite, and SQL, keywords are not case sensitive.  The following are all equally valid:

``` sql
SELECT / SeLeCt / select
```

In the examples, the keywords will be in uppercase.

SQLite, and SQL, is not whitespace sensitive.  This means a statement can be all on a single line or split over multiple lines.  In general, the examples have one keyword per line.

The statements are terminated with a semicolon, `;`.  Individual statements will run without a semicolon but multiple statement will not.

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

| pet_id | name | species| dob|
| -- | -- | -- | -- |
| 1 | Hans | Cat | 2015-09-22 |
| 2 | Minnnie | Gerbil | 2021-05-24 |
| 3	| Bo | Rabbit | 2011-10-13 |
| 4 | Joscelin | Gerbil | 2022-02-19 |

#### Vaccination
{:.no_toc}

| vax_id | pet_id | date| name| reaction |
| -- | -- | -- | -- | -- |
| 1 | 13 | 2019-09-03 | Distemper | True |
| 2 | 5 | 2019-06-23 | Canine hepatitis | False |
| 3 | 1 | 2015-01-17 | Cat Flu | False |
| 4 | 17 | 2011-10-05 | Cat Flu | False |

[Back to Table of Contents](#toc)

## Display information

It is possible to display simple messages using the `.print` command.

``` sql
.print A message
```

## Search

To search a database, a basic statement with two keywords `SELECT` and `FROM` is used.

The `SELECT` keyword lists the required field, or fields.  The `FROM` keyword states the table that the fields are in.

To display all the fields the `*` symbol is used.

``` sql
SELECT *
FROM Pet;
```

To select one, or more columns, their names are used.

``` sql
SELECT name, species
FROM Pet;
```

[Back to Table of Contents](#toc)

## Refine search

To limit the number of records returned, the `WHERE` keyword is used.

### Simple search

A simple search compares a field in record against a value.  If the comparison is `True` then the required fields of that record are displayed.

``` sql
SELECT *
FROM vaccination
WHERE reaction = "True";
```

[Back to Table of Contents](#toc)

### Complex search

A complex search compares two fields.

#### AND

If both comparisons are `True` then the required fields of that record are displayed.

``` sql
SELECT *
FROM vaccination
WHERE name = "Distemper"
  AND reaction = "True";
```

#### OR

If either comparison is `True` then the required fields of that record are displayed.

``` sql
SELECT *
FROM vaccination
WHERE name = "Distemper"
   OR reaction = "True";
```

[Back to Table of Contents](#toc)

## Order results

It is possible to order the output of a search using `ORDER BY` and stating the field, or fields.  Fields are sorted ascending, smallest to largest, by default.

``` sql
SELECT *
FROM Pet
ORDER BY species;
```

To change the sort order of a field to descending the keyword `DESC` used.  The keyword `ASC` can be used to explicitly sort ascending.

``` sql
SELECT *
FROM Pet
ORDER BY species DESC, name ASC;
```

[Back to Table of Contents](#toc)

## Insert

It is possible to insert a record, multiple records, or partial records into a table using `INSERT INTO` and `VALUES`.  All validation rules must be met for the new data to be added.

### Complete record

``` sql
INSERT INTO Pet
VALUES (26, "Tiger", "Cat", "2022-04-17");
```

### Complete records

``` sql
INSERT INTO Pet
VALUES (27, "Bill", "Ferret", "2022-05-01"),
       (28, "Ben", "Ferret", "2022-05-01");
```

### Partial record

If a partial record is added then the field names must be stated.  The values must be in the same order as the fields.

``` sql
INSERT INTO Pet ("species", "name", "pet_id")
VALUES ("Dog", "Winston", 29);
```

[Back to Table of Contents](#toc)

## Update

**Note:** It is possible to damage the data with an `UPDATE` statement.  It is advisable to practise with a `SELECT` statement first to see if the correct record, or records, will be changed.

``` sql
UPDATE Pet
SET dob = "2022-04-01"
WHERE pet_id = 29;
```

Caution: without the `WHERE` keyword the `dob` of all records would be updated!

[Back to Table of Contents](#toc)

## Delete

**Note:** It is possible to damage the data with a `DELETE FROM` statement.  It is advisable to practise with a `SELECT` statement first to see if the correct record, or records, will be deleted.

``` sql
DELETE FROM Pet
WHERE pet_id >= 26;
```

Caution: without the `WHERE` keyword all records would be deleted!

[Back to Table of Contents](#toc)

## Equi-join between tables

Tables are joined using the primary key of one table and the foreign key of the other table.

### Generic

``` sql
SELECT *
FROM table1, table2
WHERE table1.primary_key = table2.foreign_key;
```
### Example

``` sql
SELECT *
FROM Pet, Vaccination
WHERE Pet.pet_id = Vaccination.pet_id;
```

[Back to Table of Contents](#toc)

## Examples



[Back to Table of Contents](#toc)
