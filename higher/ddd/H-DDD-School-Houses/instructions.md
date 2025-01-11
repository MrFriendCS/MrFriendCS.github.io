# H DDD - School Houses

Database file: [Santa.db](../../../n5/ddd/N5-DDD-School-Houses/assets/SchoolHouses.db "Download file")


## Entity Relationship Diagram (ERD)

![ERD](assets/Diagrams/ERD-HouseSubject.png)


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


### Entity: Result

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| pupilID   | PK    | Number |       | Y     | Exists as id in Pupil table |
| subjectID | PK    | Text   | 5     | Y     | Exists as id in Subject table |
| grade     |       | Text   | 10    | Y     | Restricted choice: A, B, C, D, No Award |


### Entity: Subject

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| id        | PK    | Text   | 5     | Y     | |
| name      |       | Text   | 30    | Y     | |


### Tasks

Ensure that all column names are meaningful.

1. Display the number of children.

2. Display the number of results.

3. Show the guidance teacher, pupil's name, year, and the grade of all pupils who received `No Award`.  The results are to be sorted alphabetically, first by the teacher and then the pupil names.

4. Display all the details of subjects that end with `Studies`.

5. Display all the details of subjects that contain the word `the`.

6. Display the number of each grade, i.e.

| Grade | Count |
| ----- | ----- |
| A     | 67 |
| B     | 111 |
| ...   | ... |

{:start="7"}
7. Display each house name, and the number of S4 and S5 pupils in each house.  Display the total number of pupils from largest to smallest (one result per house).

8. Which pupil(s) have the most `A` grades?  Display them alphabetically.

9. Which house has the most `No Award` grades?  Display the house name, guidance teacher, and the number of no awards.
