# N5 DDD Membership Part 2


File: [Membership.db](assets/Membership.db "Download file")


## Data dictionary


### Entity: Club

| Attribute | Key | Type    | Size | Req'd | Validation |
| --------- | --- | ----    | ---- | :---: | ---------- |
| clubID    | PK  | Text    | 6    | Y     | |
| name      |     | Text    | 30   | Y     | |
| location  |     | Text    | 30   | Y     | |
| type      |     | Text    | 20   | Y     | |
| opened    |     | Date    |      | N     | |
| trainer   |     | Boolean |      | Y     | |
| rooms     |     | Number  |      | Y     | Range: >= 0 |


### Entity: Member

| Attribute | Key | Type   | Size | Req'd | Validation |
| --------- | --- | ----   | ---- | :---: | ---------- |
| memberNo  | PK  | Text   | 8    | Y     | |
| clubID    | FK  | Text   | 6    | Y     | clubID exists in Club table |
| firstName |     | Text   | 20   | Y     | |
| lastName  |     | Text   | 30   | Y     | |
| address   |     | Text   | 30   | N     | |
| town      |     | Text   | 20   | N     | |
| postcode  |     | Text   | 8    | N     | |
| dob       |     | Date   |      | Y     | Range: >= 1 Jan 1925 |
| renewDate |     | Number |      | Y     | Range: >= 1 and <= 12 |
| gender    |     | Text   | 2    | N     | Restricted choice: F, M, ND |
| type      |     | Text   | 8    | Y     | Restricted choice: Adult, Child, Guest, Senior, Student |


## Tasks

1. Create a new club using these details:

```
Club name: Vital Spark
Type:      Gym
Rooms:     2
Trainer:   No
Location:  Brockton
Opened:    3rd March 2017
Club code: SP488
```

{:start="2"}
2. Create a query to show the details of the club that was added.

3. For every member with a renewal date of Decemeber, change it to November.

4. Display the member number, forename, and last name of all members who have a renewal date of November.

5. Delete all members with a guest account.

6. Display the first name, surname, and memebership type of each member, sorted by membership number in reverse alphabetical order..
