# N5 DDD School Houses Part 3


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

1. Write a statement to delete Barry Wales from the Pupil table.

2. Delete Ben Barry from the Pupil table.

3. Write a statement that shows `firstName`, `lastName` and `guidanceTeacher` for all pupils.

4. Shows first name, surname, age and guidance teacher for girls in the year group S3, ordered by age ascending, surname ascending.

5. Show forename, surname and year for all pupils in Forth, order by surname ascending.

6. Display the names and guidance teacher for S5 pupils who are male.  Sort the results by age, oldest to youngest, and surname alphabetically.
