# N5 DDD School Houses

Database file: [SchoolHouses.db](assets/SchoolHouses.db "Download file")


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

8. Show the full name and `house` for pupils in S5.

9. Write a SQL statment to show the names and house for pupils younger than 13.

10. Show the name and age for all pupils who are 16 or younger.

11. Show the names of all pupils who are 13.

12.	Display the forename and `house` of pupils who are 14.

13.	Show the name and year group for pupils in S1 or S2.

14.	Write a statement to show the name of the guidance teachers of Slytherin and Gryffindor houses.

15.	Display the name and age of all S5 and S6 pupils.

16.	Show all the details of pupils who have the same surname as you, and are at least 14 years old.

17.	Write a statement to show all the pupil records, sorted by surname and then forename, both alphabetically.

18.	Show name and `id` of all pupils, sorted by age, oldest to youngest, and then surname alphbetically.

19.	Display the name and year of all S5 and S6 pupils sorted by year, lowest first, and then surname and forename alphbetically.

20.	Write the SQL to show the  `colour`, `emblem`, and name of all of the houses.  Sort the data by colour aplabetically.
