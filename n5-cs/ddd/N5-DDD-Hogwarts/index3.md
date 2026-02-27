# N5 DDD Hogwarts - Part 3


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
| houseID   | FK  | Number |      | Y     | Exists as id in House table |
| year      |     | Text   | 2    | Y     | Restricted choice: S1, S2, S3, S4, S5, S6 |
| age       |     | Number |      | Y     | Range: >= 11 and <= 18 |


### Tasks

1. Write a SQL statement to display everything in the pupil table.

2. Display everything in the house table.

3. Display the forename, age, and house name of all pupils.

4. Write a statement that shows the full name, forename and surname, and the name of the guidance teacher for all pupils.

5. Display the forename, surname, and year group for all pupils in Slytherin house.
Pupils should be in year groups, with senior pupils first.

6. Using both tables, display all of your details.

7. Display the details of all pupils with the same surname as you whose house emblem is an eagle.

8. Show forename, surname and year for all pupils in Hufflepuff, order by surname ascending.

9. Show the surname, forename, year group, and guidance teacher of each pupil.
Sort by year group, oldest to youngest.
Names should be alphabetical: forename, then surname.

10. Show the emblem, house colour, forename, and year group.
Sort the results by emblem alphabetically, and year group from youngest to oldest.

11. Display the forename, surname, age, and guidance teacher for pupils in S3, sort by age decreasing, surname alphabetically, then forename alphabetically.
