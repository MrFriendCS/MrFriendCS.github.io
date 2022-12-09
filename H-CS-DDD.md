# Higher Computing Science
{:.no_toc}

[Home](index.md)

## Database Design and Development
{:.no_toc}

___Work in Progress___

All the code examples use SQLite.  They will work with [Replit](https://replit.com/) and [DB Browser for SQLite](https://sqlitebrowser.org/).

**Note:** These notes are focused on Higher Computing Science so some terms are used differently.

## Table of Contents {#toc}
{:.no_toc}

* TOC will be displayed here
{:toc}

### Example Data

The example [database](H-CS-Database.db) contains the tables and records that the SQL examples will work with.  The file can be opened with [DB Browser for SQLite](https://sqlitebrowser.org/).

Four records from each table used in the examples are shown below.

#### Pet
{:.no_toc}

| pet_id | name | species | dob |
| -- | -- | -- | -- |
| 1 | Hans | Cat | 2015-09-22 |
| 2 | Minnnie | Gerbil | 2021-05-24 |
| 3	| Bo | Rabbit | 2011-10-13 |
| 4 | Joscelin | Gerbil | 2022-02-19 |

#### Vaccination
{:.no_toc}

| pet_id | vax_id | vax_date| reaction | paid |
| -- | -- | -- | -- | -- |
| 2 | 4 | 2021-11-06 | False | False |
| 20 | 9 | 2021-09-05 | False | False |
| 19 | 2 | 2021-07-06 | False | True |
| 9 | 8 | 2021-03-05 | False | False |

#### Vaccine
{:.no_toc}

| vax_id | name | cost |
| -- | -- | -- |
| 1 | Canine hepatitis | 27.55 |
| 2 | Cat Flu | 19.30 |
| 3 | Distemper | 34.75 |
| 4 | Feline Leukaemia Virus | 25.35 |

#### ER Diagram
{:.no_toc}

![H DDD Enitiy Relationship Diagram](H-CS-DDD.png "ER Diagram")

[Back to Table of Contents](#toc)

## Wildcards

Wildcards use the `LIKE` keyword, and are used with `WHERE`.  There are two wildcards:

| Symbol | Name | Meaning|
| :--: | -- | -- |
| % | Percent | Zero, one, or more characters |
| _ | Underscore | A single character |

Zero, one, or more characters, after the first character.

``` sql
SELECT *
FROM Pet
WHERE name LIKE "G%";
```
Zero, one, or more characters, before the last character.

``` sql
SELECT *
FROM Pet
WHERE name LIKE "%n";
```

Zero, one, or more characters in the middle.

``` sql
SELECT *
FROM Pet
WHERE species LIKE "R%t";
```

A single character in the middle.

``` sql
SELECT *
FROM Pet
WHERE species LIKE "R%t";
```

[Back to Table of Contents](#toc)

## Alias

To display search results with a different column heading instead of the field name the `AS` keyword is used.

``` sql
SELECT name AS Jag, cost
FROM Vaccine;
```

The alias can be used within the statement.

``` sql
SELECT name AS Jag, cost
FROM Vaccine
WHERE Jag LIKE "F%"
ORDER BY Jag DESC;
```

Aliases are not restricted to single words.  Due to the space, square brackets are used.

``` sql
SELECT pet_id, name, species, dob AS [Date of Birth]
FROM Pet
ORDER BY [Date of Birth] ASC;
```

[Back to Table of Contents](#toc)

## Computed values

``` sql
SELECT name, cost, cost * 1.2 AS [inc VAT]
FROM Vaccine
ORDER BY name ASC;
```

[Back to Table of Contents](#toc)

## GROUP BY {#group}

`GROUP BY` places results of a query into logical groups and removes duplicates.  [Aggregate functions](#functions) can be used with each group.

The following example will return the `species` field from every record.  Values will be repeated if they are repeated in the table.

``` sql
SELECT species
FROM Pet;
```
The following example will group together `species` field from every record.  Values will not be repeated, i.e. one row for each group.

``` sql
SELECT species
FROM Pet
GROUP BY species;
```

[Back to Table of Contents](#toc)

## ORDER BY

`ORDER BY`, if used, follows `GROUP BY`.

``` sql
SELECT species
FROM Pet
GROUP BY species
ORDER BY species;
```

[Back to Table of Contents](#toc)

## Aggregate functions {#functions}

Aggregate functions can be used with the `GROUP BY` [clause](#group).

**Note:** If fields and aggregate functions are both displayed then the fields must be in the `GROUP BY` clause, otherwise the result is meaningless.

### Minimum / Maximum

The `MIN` keyword is used to find the minimum value in a field, and `MAX` is used to find the maximum.  These work for both numeric and text values.

Find the `dob` of the oldest and youngest pet.

``` sql
SELECT MIN(dob), MAX(dob)
FROM Pet;
```

Find the `dob` of the oldest and youngest pet of each species.

``` sql
SELECT species, MIN(dob), MAX(dob)
FROM Pet
GROUP BY species;
```

### Average

``` sql
SELECT AVG(cost)
FROM Vaccine;
```

### Sum

``` sql
SELECT SUM(cost)
FROM Vaccination, Vaccine
WHERE Vaccination.vax_id = Vaccine.vax_id
  AND pet_id = 14;
```

### Count

Count the number of records in a table that meet the condition.

``` sql
SELECT COUNT(*)
FROM Pet
WHERE species = "Rabbit";
```

``` sql
SELECT species, COUNT(*)
FROM Pet
GROUP BY species;
```

[Back to Table of Contents](#toc)

## WHERE

It is possible to use the result from an aggregate function in a `WHERE` clause, but not directly.

### Using a result in another query

This will crate a temporary query (view) that will be deleted when the database is closed.

``` sql
CREATE TEMP VIEW Oldest (dob) AS
SELECT MIN(doB)
FROM Pet;
```

Use the stored result.

``` sql
SELECT Pet.name, Vaccine.name, vax_date, cost
FROM Oldest, Pet, Vaccination, Vaccine
WHERE Pet.pet_id = Vaccination.pet_id
  AND Vaccination.vax_id = Vaccine.vax_id
  AND Oldest.dob = Pet.dob;
```

### Subclause (Single query)

**Note** Using subclauses is beyond the scope of the Higher course and will not be assessed.

``` sql
SELECT Pet.name, Vaccine.name, vax_date, cost
FROM Oldest, Pet, Vaccination, Vaccine
WHERE Pet.pet_id = Vaccination.pet_id
  AND Vaccination.vax_id = Vaccine.vax_id
  AND Pet.dob = 
      (SELECT MIN(doB)
       FROM Pet);
```

[Back to Table of Contents](#toc)

## Examples

``` sql
SELECT species, COUNT(*) as jags
FROM Pet, Vaccination
WHERE Pet.pet_id = Vaccination.vax_id
  AND vax_date >= "2020-01-01"
  AND vax_date <= "2020-12-31"
GROUP BY species
ORDER BY jags DESC;
```

``` sql
SELECT Pet.pet_id, Pet.name, species, SUM(cost * 1.2) as [inc VAT]
FROM Pet, Vaccination, Vaccine
WHERE Pet.pet_id = Vaccination.vax_id
  AND Vaccination.vax_id = Vaccine.vax_id
  AND paid = "False"
GROUP BY Pet.pet_id
ORDER BY [inc VAT] DESC;
```

[Back to Table of Contents](#toc)
