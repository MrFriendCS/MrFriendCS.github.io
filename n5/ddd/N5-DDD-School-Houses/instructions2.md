# N5 DDD School Houses Part 2


## Entity Relationship Diagram (ERD)

![ERD](assets/erd.png "ERD-HousePupil")


## Data Dictionary

### Entity: House

| Attribute       | Key   | Type | Size  | Req'd | Validation |
| ---------       | :---: | ---- | :---: | :---: | ---------- |
| name            | PK    | Text | 15    | Y     |            |
| guidanceTeacher |       | Text | 30    | N     |            |
| colour          |       | Text | 15    | Y     |            |


### Entity: Pupil

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| id        | PK    | Text   | 10    | Y     |            |
| lastName  |       | Text   | 30    | Y     |            |
| firstName |       | Text   | 20    | Y     |            |
| gender    |       | Text   | 10    | N     | Restricted choice: Female, Male, Not disclosed |
| house     | FK    | Text   | 15    | Y     | Exists as name in House table |
| year      |       | Text   | 5     | Y     | Restricted choice: S1, S2, S3, S4, S5, S6 |
| age       |       | Number |       | Y     | Range: >= 11 and <= 18 |


### Tasks

1. Add a new record to the House table. There is a new house called `Paisley` house with `Mrs Hunter` as the guidance teacher. Its colour is `black`.

2. Add a new record to the Pupil table.  The details are:

```
id: 08-8774112
lastName: Smith
firstName: Rachel
gender: Female
house: Forth
year: S3
age: 13
```

3. Add a new pupil.  The details are:

```
id: 20-2111447
firstName: James
surname: Clark
gender: Male
house: Clyde
age: 11
year: S1
```

4. Add another pupil.  The details are:

```
ID: 05-1328078
Surname: Taylor
Forename: Amy
House: Kelvin
Year: S5
Age: 17
```

5. From now on, Mr N. Craven wishes to be known as DJ Nicky Cray and has changed his house colour to crimson.  Write a statement to make this change in the House table.

6. Write a statement to update the record for Suellen Wrigley to Kelvin.

7. Write a statement to update the record for Mary Cawdron to Mary Lawrie.

8. Write a statement to update the record for Nora Coil to Clyde.

9. Write a SQL statement to remove Ernie Dawson from the Pupil table.

10. Paisley house was a short lived idea. Write a SQL statement to delete this house from the database.
