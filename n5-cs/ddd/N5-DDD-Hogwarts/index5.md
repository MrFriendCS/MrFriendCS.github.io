# N5 DDD Hogwarts - Part 5


Database file: [Hogwarts.db](assets/Hogwarts.db "Download file")


## Entity Relationship Diagram (ERD)

![ERD](assets/Diagrams/ERD-HousePupil.png)


## Data Dictionary

### Entity: House

| Attribute       | Key | Type   | Size | Req'd | Validation |
| ---------       | --- | ----   | ---- | :---: | ---------- |
| id              | PK  | Number |      | Y     | |
| name            |     | Text   | 20   | Y     | |
| guidanceTeacher |     | Text   | 30   | N     | |
| emblem          |     | Text   | 10   | Y     | |
| colour          |     | Text   | 20   | Y     | |


### Entity: Pupil

| Attribute | Key | Type   | Size | Req'd | Validation |
| --------- | --- | ----   | ---- | :---: | ---------- |
| id        | PK  | Number |      | Y     | |
| lastName  |     | Text   | 30   | Y     | |
| firstName |     | Text   | 20   | Y     | |
| houseID   | FK  | Number |      | Y     | Exists as `id` in House table |
| year      |     | Text   | 2    | Y     | Restricted choice: S1, S2, S3, S4, S5, S6 |
| age       |     | Number |      | Y     | Range: >= 11 and <= 18 |


### Tasks

1. Sally Holby's age has been incorrectly recorded.
Using her pupil id, change her age to 15.

2. Display the updated record.

3. Colin Fifth should really be Colin Forth, also he should be in S1.
Using his pupil id, update his record.

4. Display the updated record.

5. Display all of your details from the pupil and house table.

6. The sorting hat has made a mistake.
Using your pupil id, change your record and move to a different house.

7. Display the updated record.

8. Berneray house was a short lived idea.
Write a SQL statement to remove this house from the database.

9. Find the details of John Bull.

10. John Bull is a Muggle!  He should never have been enrolled, and has now been expelled.
Using his pupil id, remove him from the database.
