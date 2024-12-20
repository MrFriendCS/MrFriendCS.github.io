# N5 DDD School Houses - Part 3

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
| year      |       | Text   | 2     | Y     | Restricted choice: S1, S2, S3, S4, S5, S6 |
| age       |       | Number |       | Y     | Range: >= 11 and <= 18 |


### Tasks

1. Write a SQL statement to display everything in the pupil table.

2. Add a new pupil to the school.  The details are:

```
id: 301
lastName: Potter
firstName: Harry
house: Gryffindor
year: S1
age: 11
```

3. Add a another new pupil.  The details are:

```
id: 302
year: S1
age: 11
forename: Draco 
surname: Malfoy
house: Slytherin
```

4. Write the SQL to display the new pupil records.

5. Write a SQL statement to display everything in the house table.

6. There is a new house called `Berneray` house with `Prof MacNeil` as the guidance teacher. Its emblem is a `Sheep` and the house colour is `Green and Black`.  Use the next available `id` to add it to the house table.

7. Display the new house record.

8. Berneray's house colour should be `Green and White`.  Modify the record to make this change.

9. Display the updated record.

10. From now on, Prof Sprout wishes to be known as `Prof Carrot` and has changed her house cemblem to a `Rabbit`.  Write a single statement to make these changes.

11. Display the updated record.

12. Sally Holby's age has been incorrectly recorded.  Using her pupil id, change her age to 15.

13. Colin Fifth should really be Colin Forth, also he's in S1.  Using his pupil id, update his record.

12. Display all of your details from the pupil and house table.

13. Change your record and move to a different house.

14. Display the updated record.

7. Write a statement to update the record for Mary Cawdron to Mary Lawrie.

8. Write a statement to update the record for Nora Coil to Clyde.

9. Write a SQL statement to remove Ernie Dawson from the Pupil table.

10. Berneray house was a short lived idea. Write a SQL statement to remove this house from the database.

1. Write a statement to delete Barry Wales from the Pupil table.

2. Delete Ben Barry from the Pupil table.

3. Write a statement that shows `firstName`, `lastName` and `guidanceTeacher` for all pupils.

4. Shows first name, surname, age and guidance teacher for pupils in the year group S3, ordered by age increasing, and surname alphabetically.

5. Show forename, surname and year for all pupils in Forth, order by surname ascending.

6. Display the names and guidance teacher for S5 pupils who are male.  Sort the results by age, oldest to youngest, and surname alphabetically.
