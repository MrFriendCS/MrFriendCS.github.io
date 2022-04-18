# Higher Computing Science
{:.no_toc}

[SDD](H-CS-SDD.md)
[N5](index.md)

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

Four records of the data used in the examples are shown in the following tables:

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

| vax_id | pet_id | vax_date| reaction | paid |
| -- | -- | -- | -- | -- |
| 4 | 2 | 2021-11-06 | False | False |
|9 | 20 | 2021-09-05 | False | False |
|2 | 19 | 2021-07-06 | False | True |
|8 | 9 | 2021-03-05 | False | False |

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
WHERE species LIKE "R%t";
```

``` sql
SELECT *
FROM Pet
WHERE name LIKE "R_t";
```

[Back to Table of Contents](#toc)

## Aggregate functions


### Minimum


### Maximum


### Average


### Sum


### Count


[Back to Table of Contents](#toc)

## computed values, alias


[Back to Table of Contents](#toc)

## GROUP BY


[Back to Table of Contents](#toc)

## ORDER BY


[Back to Table of Contents](#toc)

## WHERE



[Back to Table of Contents](#toc)

## Examples

``` sql
SELECT Pet.pet_id, Pet.name, species, SUM(cost * 1.2) as [inc VAT]
FROM Pet, Vaccination, Vaccine
WHERE Pet.pet_id = Vaccination.vax_id
  AND Vaccination.vax_id = Vaccine.vax_id
  AND paid = "False"
GROUP BY Pet.pet_id
ORDER BY [inc VAT] DESC;
```
