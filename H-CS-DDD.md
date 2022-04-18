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

The first 4 records of the data used in the examples is shown in the following tables:

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

| vax_id | pet_id | vax_date| reaction |
| -- | -- | -- | -- |
| 3 | 13 | 2019-09-03 | True |
| 1 | 5 | 2020-06-23 | False |
| 2 | 1 | 2015-12-17 | False |
| 2 | 17 | 2015-10-05 | False |

#### Vaccine
{:.no_toc}

| vax_id | name | cost |
| -- | -- | -- |
| 1 | Canine hepatitis | 27.55 |
| 2 | Cat Flu | 19.30 |
| 3 | Distemper | 34.75 |
| 4 | Feline Leukaemia Virus | 25.35 |



## wildcards


[Back to Table of Contents](#toc)

## Aggregate functions


### MIN


### MAX


### AVG


### SUM


### COUNT


[Back to Table of Contents](#toc)

## computed values, alias


[Back to Table of Contents](#toc)

## GROUP BY


[Back to Table of Contents](#toc)

## ORDER BY


[Back to Table of Contents](#toc)

## WHERE


[Back to Table of Contents](#toc)
