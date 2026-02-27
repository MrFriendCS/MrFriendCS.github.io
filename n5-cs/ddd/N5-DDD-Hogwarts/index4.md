# N5 DDD Hogwarts - Part 4


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

{:start="3"}
3. Add a another new pupil.  The details are:

```
id: 302
year: S1
age: 11
forename: Draco 
surname: Malfoy
house: Slytherin
```

{:start="4"}
4. Write a single SQL statement to display the new records.

5. Write a SQL statement to display everything in the house table.

6. There is a new house called `Berneray` house.
Its emblem is a `Sheep` and the house colour is `Green and Black`.
Unfortunately, no one has volunteered to be the guidance teacher.
Use the next available `id` to add the available data to the house table.

7. Display the new house record.

8. Berneray's house colour should be `Green and White`.
Modify the record to make this change.

9. Display the updated record.

10. From now on, Prof Sprout wishes to be known as `Prof Carrot` and has changed her house emblem to a `Rabbit`.
Write a single statement to make these changes.

11. Display the updated record.
