# N5 DDD School Houses - Part 2

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
| id        | PK    | Text   | 10    | Y     | |
| lastName  |       | Text   | 30    | Y     | |
| firstName |       | Text   | 20    | Y     | |
| house     | FK    | Number |       | Y     | Exists as id in House table |
| year      |       | Text   | 5     | Y     | Restricted choice: S1, S2, S3, S4, S5, S6 |
| age       |       | Number |       | Y     | Range: >= 11 and <= 18 |


### Tasks

1. Add a new pupil to the school.  The details are:

```
id: 301
lastName: Potter
firstName: Harry
house: Gryffindor
year: S1
age: 11
```

2. Add a another new pupil.  The details are:

```
id: 302
firstName: Draco 
surname: Malfoy
house: Slytherin
age: 11
year: S1
```

3. Write the SQL to display the new pupil records.

4. Add a new record to the House table. There is a new house called `Berneray` house with `Prof MacNeil` as the guidance teacher. Its emblem is a `Sheep` and the house colour is `Green and White`.  Use the next available `id`.

5. 

5. From now on, Mr N. Craven wishes to be known as DJ Nicky Cray and has changed his house colour to crimson.  Write a statement to make this change in the House table.

6. Write a statement to update the record for Suellen Wrigley to Kelvin.

7. Write a statement to update the record for Mary Cawdron to Mary Lawrie.

8. Write a statement to update the record for Nora Coil to Clyde.

9. Write a SQL statement to remove Ernie Dawson from the Pupil table.

10. Berneray house was a short lived idea. Write a SQL statement to delete this house from the database.
