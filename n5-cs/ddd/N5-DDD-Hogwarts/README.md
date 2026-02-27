# N5 DDD Hogwarts


Database file: [Hogwarts.db](assets/Hogwarts.db "Download file")


## Entity Relationship Diagram (ERD)

![ERD](assets/Diagrams/ERD-HousePupil.png)


## Data Dictionary

### Entity: House

| Attribute       | Key   | Type   | Size  | Req'd | Validation |
| ---------       | :---: | ----   | :---: | :---: | ---------- |
| id              | PK    | Number |       | Y     | |
| name            |       | Text   | 20    | Y     | |
| guidanceTeacher |       | Text   | 30    | N     | |
| emblem          |       | Text   | 10    | Y     | |
| colour          |       | Text   | 20    | Y     | |


### Entity: Pupil

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| id        | PK    | Number |       | Y     | |
| lastName  |       | Text   | 30    | Y     | |
| firstName |       | Text   | 20    | Y     | |
| houseID   | FK    | Number |       | Y     | Exists as id in House table |
| year      |       | Text   | 2     | Y     | Restricted choice: S1, S2, S3, S4, S5, S6 |
| age       |       | Number |       | Y     | Range: >= 11 and <= 18 |


### Tasks

1. Display all records from the `House` table.

2. Write the SQL to show everything in the `Pupil` table.

3. Show the `name` field and the `colour` field from the house table.

4. Display the full names, `firstName` and `lastName`, of all the pupils.

5. Write an SQL statement to show all the data for only the S3 pupils.

6. Display the full names of the S1 pupils.

7. Display the details of just `Hufflepuff` house.

8. Show the name and age for all pupils who are 16 or younger.

9. Show the names of all pupils who are 13.

10. Show the name and year group for pupils in S1 or S2.
