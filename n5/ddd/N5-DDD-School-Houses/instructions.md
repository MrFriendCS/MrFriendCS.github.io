# N5 DDD School Houses

## Entity Relationship Diagram

![ERD](assets/erd.png "ERD")


## Data Dictionary

### Entity: House

| Attribute        | Key   | Typ  | Size  | Req'd | Validation |
| ---------        | :---: | ---- | :---: | :---: | ---------- |
| house            | PK    | text | 15    | Y     |            |
| guidance_teacher |       | text | 30    | N     |            |
| colour           |       | text | 15    | Y     |            |


### Entity: Pupil

| Attribute  | Key   | Type   | Size  | Req'd | Validation |
| ---------  | :---: | ----   | :---: | :---: | ---------- |
| id         | PK    | text   | 10    | Y     |            |
| last_name  |       | text   | 30    | Y     |            |
| first_name |       | text   | 20    | Y     |            |
| gender     |       | text   | 10    | N     |            |
| house      | FK    | text   | 15    | Y     | Exists in House table |
| year       |       | text   | 5     | Y     |            |
| age        |       | number |       | Y     |            |


## Tasks

After completing a task, cut and paste the SQL into a seperate file.  The first 2 files have already been created.

### Task 1

Write SQL statements for the following:

a)	Write SQL to show all records from the Pupil table

b)	Select all records from the House table

c)	Select the `house` field and the `colour` field from the House table

d)	Select `first_name` and `last_name` from the Pupil table


### Task 2

a)	Write SQL to show records from the Pupil table for pupils in S3

b)	Show `first_name` and `last_name` from the Pupil table for pupils in S1

c)	Show `first_name`, `last_name`, 'house' from the Pupil table for pupils in Clyde house

d)	Show the `guidance_teacher` from the House table where the house is Forth


### Task 3

a)	Write a statment to show 'first_name', 'last_name' and 'house' from the Pupil table for pupils aged less than 12

b)	Show 'first_name', 'last_name' and 'gender' from the Pupil table for pupils who are 16 or under

c)	Show 'first_name', 'last_name' from the Pupil table for pupils who are 13

d)	Show 'first_name' and 'house' from the Pupil table for pupils who are 14


### Task 4

a)	Show `first_name` and `last_name` from the Pupil table for pupils in Kelvin and S1

b)	Write a statement to show `first_name`, `last_name` and `house` from the Pupil table for pupils in Kelvin or Clyde

c)	Show `first_name` and `last_name` from the Pupil table for pupils in S4 or S5 

d)	show `first_name`, `last_name`, `house` and `year` from the Pupil table for pupils from S3 pupils who are in Forth house


### Task 5

a)	Write a statement to show everything from the Pupil table for pupils in Forth or Kelvin, sorted by year descending, and age ascending

b)	Show `first_name`, `last_name` and `age` from the Pupil table for boys in Clyde, sorted by surname ascending, and age ascending 

c)	Show everything from the Pupil table for girls in Kelvin, sorted by year ascending, and age ascending

d)	Show everything from the Pupil table for pupils in Forth and S3, sorted by surname ascending, and then first name ascending 


### Task 6

a)	Add a new record to the House table. There is a new house called ‘Paisley’ house with ‘Mrs Hunter” as the guidance teacher. Its colour is ‘black’

b)	Add a new record to the Pupil table.  The details are:

```
id: 08-8774112
last_name: Smith
first_name: Rachel
gender: female
house: Forth
year: S3
age: 13
```

c)	Add a new record to the Pupil table.  The details are:

```
id: 20-2111447
last_name: Clark
first_name: James
gender: male
house: Clyde
year: S1
age: 11
```

d)	Add a new record to the Pupil table.  The details are:

```
ID: 05-1328078
Surname: Taylor
Forename: Amy
Gender: female
House: Kelvin
Year: S5
Age: 17
```

### Task 7

a)	From now on, Mr N. Craven wishes to be known as DJ Nicky Cray and has changed his house colour to rainbow.  Write a statement to update the record in the House table

b)	Write a statement to update the record for Suellen Wrigley to Kelvin

c)	Write a statement to update the record for Mary Cawdron to Mary Lawrie

d)	Write a statement to update the record for Nora Coil to Clyde


### Task 8

a)	It was decided that the Paisley house was a terrible idea. Write a SQL statement to delete this house from the database

b)	Write a SQL statement to delete Ernie Dawson from the Pupil table

c)	Write a statement to delete Barry Wales from the Pupil table

d)	Delete Ben Barry from the Pupil table


### Task 9

a)	Write a statement that shows `first_name`, `last_name` and `guidance_teacher` for all pupils

b)	Shows first name, surname , age and guidance teacher for girls in the year group S3, ordered by age ascending, surname ascending

c)	Show forename, surname and year for all pupils in Forth, order by surname ascending

d)	Shows forename, surname and guidance teacher for Pupils in the year group S5 and gender male, ordered by age descending, surname ascending
