# N5 DDD Membership


File: [Membership.db](assets/Membership.db "Download file")


## Tasks


### Part 1

1. Create a query to display the club name and club ID of all clubs.

2. Display the first name, surname, and gender of all adult members.

3. Display the first name, surname, and gender of all adult members, with surnames in alphabetical order.

4. Display all information of clubs that offer personal trainers.  Order by the number of rooms for hire, highest first.

5. Show the town, date of birth, first name, and last name.  Order by town (alphabetical), then date of birth (youngest first)

6. Create a query to display the last name, address, and postcode of all males who must renew their membership in May.

7. Link the tables using the relationship created by `clubID`.  Display the first name, surname, and the type of club they attend.

8. Display the first name, surname, and the member number of each Puddles club member.  Order by forename and then surname.


### Part 2

``` sql
INSERT INTO
    VALUES
```

{:start="9"}
9. Insert a new club using these details:

``` sql
SP488, Vital Spark, Brockton, Gym, 2017-03-03, FALSE, 2
```

{:start="10"}
10. Create a query to show the details of the club that was added.


### Part 3

``` sql
UPDATE
    SET
    WHERE
```

{:start="11"}
11. Update every member who has December as a renewal date to November.

12. Display the member number, forename, and last name of all members who have a renewal date of November.


### Part 4

``` sql
DELETE FROM
    WHERE
```

{:start="13"}
13. Delete all members with a guest account.

14. Display the first name, surname, and memebership type of each member, with the membership type alphabetical.


## Data dictionary

### Entity: Club

| Attribute | Key   | Type    | Size  | Req'd | Validation |
| --------- | :---: | ----    | :---: | :---: | ---------- |
| clubID    | PK    | Text    | 6     | Y     |            |
| name      |       | Text    | 30    | Y     |            |
| location  |       | Text    | 30    | Y     |            |
| type      |       | Text    | 20    | Y     |            |
| opened    |       | Date    |       | N     |            |
| trainer   |       | Boolean |       | Y     |            |
| rooms     |       | Number  |       | Y     | Range: >= 0 |


### Entity: Member

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| memberNo  | PK    | Text   | 8     | Y     |            |
| clubID    | FK    | Text   | 6     | Y     | Exists in Club table |
| firstName |       | Text   | 20    | Y     |            |
| lastName  |       | Text   | 30    | Y     |            |
| address   |       | Text   | 30    | N     |            |
| town      |       | Text   | 20    | N     |            |
| postcode  |       | Text   | 8     | N     |            |
| dob       |       | Date   |       | Y     | Range: >= 1 Jan 1925 |
| renew     |       | Number |       | Y     | Range: >= 1 and <= 12 |
| gender    |       | Text   | 2     | N     | Restricted choice: F, M, ND |
| type      |       | Text   | 8     | Y     | Restricted choice: Adult, Child, Guest, Senior, Student |
