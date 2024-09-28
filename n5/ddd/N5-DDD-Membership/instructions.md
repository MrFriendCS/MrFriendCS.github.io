# N5 DDD Membership


File: [Membership.db](assets/Membership.db "Download file")


## Tasks

1. Create a query to display the club name and club ID of all clubs.

2. Display the first name, surname, and gender of all adult members.

3. Display the first name, surname, and gender of all adult members, with surnames in alphabetical order.

4. Display all information of clubs that offer personal trainers.  Order by the number of rooms for hire, highest first.

5. Show the town, date of birth, first name, and last name.  Order by town (alphabetical), then date of birth (youngest first)

6. Create a query to display the last name, address, and postcode of all males who must renew their membership in May.

7. Link the tables using the relationship created by `club_id`.  Display the first name, surname, and the type of club they attend.

8. Display the first name, surname, and the member number of each Puddles club member.  Order by forename and then surname.


``` sql
INSERT INTO
    VALUES
```

9. Insert a new club using these details:
    
``` sql
SP488, Vital Spark, Brockton, Gym, 2017-03-03, FALSE, 2
```
 
10. Create a query to show the details of the club that was added.


``` sql
UPDATE
    SET
    WHERE
```

11. Update every member who has December as a renewal date to November.

12. Display the member number, forename, and last name of all members who have a renewal date of November.


``` sql
DELETE FROM
    WHERE
```

13. Delete all members with a guest account.

14. Display the first name, surname, and memebership type of each member, with the membership type alphabetical.


## Data dictionary

### Table: club

| Attribute | Key   | Type    | Size  | Req'd | Validation |
| --------- | :---: | ----    | :---: | :---: | ---------- |
| id        | PK    | VARCHAR | 6     | Y     |            |
| name      |       | VARCHAR | 30    | Y     |            |
| location  |       | VARCHAR | 30    | Y     |            |
| type      |       | VARCHAR | 20    | Y     |            |
| opened    |       | DATE    |       | N     |            |
| trainer   |       | BOOLEAN |       | Y     |            |
| rooms     |       | INT     |       | Y     | range: >= 0 |

### Table: member

| Attribute  | Key   | Type    | Size  | Req'd | Validation |
| ---------  | :---: | ----    | :---: | :---: | ---------- |
| member_no  | PK    | VARCHAR | 8     | Y     |            |
| club_id    | FK    | VARCHAR | 6     | Y     | Exists in Club table |
| first_name |       | VARCHAR | 20    | Y     |            |
| last_name  |       | VARCHAR | 30    | Y     |            |
| address    |       | VARCHAR | 30    | N     |            |
| town       |       | VARCHAR | 20    | N     |            |
| postcode   |       | VARCHAR | 8     | N     |            |
| dob        |       | DATE    |       | Y     | range: >= 1 Jan 1925 |
| renew      |       | INT     |       | Y     | range: >= 1 and <= 12 |
| gender     |       | VARCHAR | 2     | N     | restricted choice: F, M, ND |
| type       |       | VARCHAR | 8     | Y     | restricted choice: Adult, Child, Guest, Senior, Student  |
