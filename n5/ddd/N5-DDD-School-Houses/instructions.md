# N5 DDD School Houses

## Entity Relationship Diagram

![ERD](assets/erd.png "ERD-HousePupil")


## Data Dictionary

### Entity: House

| Attribute       | Key   | Typ  | Size  | Req'd | Validation |
| ---------       | :---: | ---- | :---: | :---: | ---------- |
| name           | PK    | Text | 15    | Y     |            |
| guidanceTeacher |       | Text | 30    | N     |            |
| colour          |       | Text | 15    | Y     |            |


### Entity: Pupil

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| id        | PK    | Text   | 10    | Y     |            |
| lastName  |       | Text   | 30    | Y     |            |
| firstName |       | Text   | 20    | Y     |            |
| gender    |       | Text   | 10    | N     |            |
| house     | FK    | Text   | 15    | Y     | Exists as name in House table |
| year      |       | Text   | 5     | Y     |            |
| age       |       | Number |       | Y     |            |


### Tasks

1. Write the SQL to show all records from the `Pupil` table.

2. Display all records from the `House` table.

3. Show the `house` field and the `colour` field from the House table.

4. Display the full names, `firstName` and `lastName`, of all pupils from the Pupil table.

5. Write the SQL to show all the pupil data for only the S3 pupils.

6. For the full names of the S1 pupils.

7. Show `firstName`, `lastName`, `house` for pupils in Clyde house.

8. Using the `House` table, show all the details of the `Forth` house.

9. Write a statment to show `firstName`, `lastName` and `house` from the Pupil table for pupils aged less than 12.

10. Show `firstName`, `lastName` and `gender` from the Pupil table for pupils who are 16 or under.

11. Show `firstName`, `lastName` from the Pupil table for pupils who are 13.

12.	Show `firstName` and `house` from the Pupil table for pupils who are 14.

13.	Show `firstName` and `lastName` from the Pupil table for pupils in Kelvin and S1.

14.	Write a statement to show `firstName`, `lastName` and `house` from the Pupil table for pupils in Kelvin or Clyde.

15.	Show `firstName` and `lastName` from the Pupil table for pupils in S4 or S5.

16.	show `firstName`, `lastName`, `house` and `year` from the Pupil table for pupils from S3 pupils who are in Forth house.

17.	Write a statement to show everything from the Pupil table for pupils in Forth or Kelvin, sorted by year descending, and age ascending.

18.	Show `firstName`, `lastName` and `age` from the Pupil table for boys in Clyde, sorted by surname ascending, and age ascending .

19.	Show everything from the Pupil table for girls in Kelvin, sorted by year ascending, and age ascending.

20.	Show everything from the Pupil table for pupils in Forth and S3, sorted by surname ascending, and then first name ascending .

21.	Add a new record to the House table. There is a new house called `Paisley` house with `Mrs Hunter` as the guidance teacher. Its colour is `black`.

22.	Add a new record to the Pupil table.  The details are:

```
id: 08-8774112
last_name: Smith
first_name: Rachel
gender: female
house: Forth
year: S3
age: 13
```

23.	Add a new record to the Pupil table.  The details are:

```
id: 20-2111447
last_name: Clark
first_name: James
gender: male
house: Clyde
year: S1
age: 11
```

24.	Add a new record to the Pupil table.  The details are:

```
ID: 05-1328078
Surname: Taylor
Forename: Amy
Gender: female
House: Kelvin
Year: S5
Age: 17
```

25.	From now on, Mr N. Craven wishes to be known as DJ Nicky Cray and has changed his house colour to rainbow.  Write a statement to update the record in the House table.

26.	Write a statement to update the record for Suellen Wrigley to Kelvin.

27.	Write a statement to update the record for Mary Cawdron to Mary Lawrie.

28.	Write a statement to update the record for Nora Coil to Clyde.

29.	It was decided that the Paisley house was a terrible idea. Write a SQL statement to delete this house from the database.

30.	Write a SQL statement to delete Ernie Dawson from the Pupil table.

31.	Write a statement to delete Barry Wales from the Pupil table.

32.	Delete Ben Barry from the Pupil table.

33.	Write a statement that shows `firstName`, `lastName` and `guidanceTeacher` for all pupils.

34.	Shows first name, surname , age and guidance teacher for girls in the year group S3, ordered by age ascending, surname ascending.

35.	Show forename, surname and year for all pupils in Forth, order by surname ascending.

36.	Shows forename, surname and guidance teacher for Pupils in the year group S5 and gender male, ordered by age descending, surname ascending.
