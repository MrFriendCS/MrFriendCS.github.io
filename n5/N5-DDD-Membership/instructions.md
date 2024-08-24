# N5 DDD Membership

## Tasks

1. Create a query to display the club name and club ID of all clubs.

2. Display the first name, surname, and gender of all adult members.

3. Display the first name, surname, and gender of all adult members, with surnames in alphabetical order.

4. Display all information of clubs that offer personal trainers.  Order by the number of rooms for hire, highest first.

5. Show the town, date of birth, first name, and last name.  Order by town (alphabetical), then date of birth (youngest first)

6. Create a query to display the last name, address, and postcode of all males who must renew their membership in May.

7. Link the tables using the relationship created by `club_id`.  Display the first name, surname, and the type of club they attend.

8. Display the first name, surname, and the member number of each Puddles club member.  Order by forename and then surname.

9. Insert a new club using the keywords:

``` sql
INSERT INTO
    VALUES
```

New club details:
    
``` sql
SP488, Vital Spark, Brockton, Gym, 2017-03-03, FALSE, 2
```
 
10. Create a query to show the details of the club that was added.

11. Update every member who has December as a renewal date to November.  Keywords needed:

``` sql
UPDATE
    SET
    WHERE
```

12. Display the member number, forename, and last name of all members who have a renewal date of November.

13. Delete all members with a guest account.  Keywords needed:

``` sql
DELETE FROM
    WHERE
```

14. Display the first name, surname, and memebership type of each member, with the membership type alphabetical.


## Data dictionary

### Table: club

| Attribute   | Key   | Type    | Size  | Req'd | Validation |
| ---------   | :---: | ----    | :---: | :---: | ---------- |
| club_id     | PK    | text    | 6     | Y     |            |
| club_name   |       | text    | 30    | Y     |            |
| location    |       | text    | 30    | Y     |            |
| club_type   |       | text    | 20    | Y     |            |
| date_opened |       | date    |       | N     |            |
| trainer     |       | boolean |       | Y     |            |
| rooms       |       | number  |       | Y     | range: >= 0 |

### Table: member

| Attribute   | Key   | Type   | Size  | Req'd | Validation |
| ---------   | :---: | ----   | :---: | :---: | ---------- |
| member_no   | PK    | text   | 8     | Y     |            |
| club_id     | FK    | text   | 6     | Y     | Exists in Club table |
| first_name  |       | text   | 20    | Y     |            |
| last_name   |       | text   | 30    | Y     |            |
| address     |       | text   | 30    | N     |            |
| town        |       | text   | 20    | N     |            |
| postcode    |       | text   | 8     | N     |            |
| dob         |       | date   |       | Y     | range: >= 1 Jan 1920 |
| renewal     |       | number |       | Y     | range: >= 1 and <= 12 |
| gender      |       | text   | 2     | N     | restricted choice: F, M, ND |
| member_type |       | text   | 8     | Y     | restricted choice: Adult, Child, Guest, Senior, Student  |
