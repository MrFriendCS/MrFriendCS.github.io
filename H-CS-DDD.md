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

[Database](H-CS-Database.db)

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

[Back to Table of Contents](#toc)

## Wildcards

Wildcards use the `LIKE` keyword, and are used with `WHERE`.  There are two wildcards:

| Symbol | Name | Meaning|
| :--: | -- | -- |
| % | Percent | Zero, one, or more characters |
| _ | Underscore | A single character |

``` sql
SELECT *
FROM Pet
WHERE name LIKE "G%";
```

``` sql
SELECT *
FROM Pet
WHERE name LIKE "%n";
```

``` sql
SELECT *
FROM Pet
WHERE species LIKE "R%t";
```

``` sql
SELECT *
FROM Pet
WHERE name LIKE "R_t";
```

[Back to Table of Contents](#toc)

## Alias

To display search results with a different column heading instead of the field name the `AS` keyword is used.

``` sql
SELECT name AS Jag, cost AS Price
FROM Vaccine;
```

The alias can be used in the statement.

``` sql
SELECT name AS Jag, cost AS Price
FROM Vaccine
WHERE Price >= 30
ORDER BY Price DESC;
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
SELECT name, cost, cost * 1.2 [inc VAT]
FROM Vaccine;
```

[Back to Table of Contents](#toc)

## GROUP BY

The following example will return the `species` field from every record.

``` sql
SELECT species
FROM Pet;
```
The following example will group together `species` field from every record.

``` sql
SELECT species
FROM Pet
GROUP BY species;
```

[Back to Table of Contents](#toc)

## ORDER BY

``` sql
SELECT species
FROM Pet
GROUP BY species;
```

[Back to Table of Contents](#toc)

## Aggregate functions

Aggregate functions can be used with with `GROUP BY` clause.

### Minimum / Maximum

The `MIN` keyword is used to find the minimum value in a field, and `MAX` is used to find the maximum.  These work for both numeric and text values.

Find the `dob` of the oldest and youngest pet.

``` sql
SELECT MIN(dob), MAX(dob)
FROM Pet;
```

Find the `dob` of the oldest and youngest pet of each species.

**Note:** As a general rule, if fields and aggregate functions are both displayed then the fields need to be in the `GROUP BY` clause.  Otherwise the result is meaningless.

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

Which animals received the most expensive injection?

### Single query (sub-query)

``` sql
SELECT Pet.name, Vaccine.name, vax_date, cost
FROM Oldest, Pet, Vaccination, Vaccine
WHERE Pet.pet_id = Vaccination.pet_id
  AND Vaccination.vax_id = Vaccine.vax_id
  AND Pet.dob = 
      (SELECT MIN(doB)
       FROM Pet);
```

### Two queries

``` sql
CREATE TEMP VIEW Oldest (dob) AS
SELECT MIN(doB)
FROM Pet;
```

``` sql
SELECT Pet.name, Vaccine.name, vax_date, cost
FROM Oldest, Pet, Vaccination, Vaccine
WHERE Pet.pet_id = Vaccination.pet_id
  AND Vaccination.vax_id = Vaccine.vax_id
  AND Oldest.dob = Pet.dob;
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
