# N5 DDD Insert Queries


File: [Clydeview.db](../N5-DDD-Clydeview/assets/Clydeview.db "Download file")


## Database


### Table: Owner

| Field     | Key | Type   | Size | Req’d | Validation |
| -----     | --- | ----   | ---- | ----- | ---------- |
| ownerID   | PK  | Number |      | Y     | |
| forename  |     | Text   | 20   |       | |
| surname   |     | Text   | 30   |       | |
| address   |     | Text   | 50   |       | | 
| town      |     | Text   | 20   |       | |
| telephone |     | Text   | 13   |       | |


### Table: Pet

| Field       | Key | Type    | Size | Req’d | Validation |
| -----       | --- | ----    | ---- | ----- | ---------- |
| code        | PK  | Text    |      | Y     | |
| name        |     | Text    | 20   |       | |
| type        |     | Text    | 8    |       | Restricted choice: Cat, Dog, Budgie, Gerbil, Tortoise |
| dateOfBirth |     | Date    |      |       | |
| vaccination |     | Boolean |      |       | |
| ownerID     | FK  | Number  |      | Y     | ownerID exists in Owner table |


### Entity Relationship Diagram (ERD)

![ERD](assets/erd1.png)


## Tasks

Using SQL queries:

1. Add the details of Goldie the dog to the Pet table.

| Field         | Value |
| -----         | ----- |
| Pet code      | P4821 |
| Pet name      | Goldie |
| Pet type      | Dog |
| Date of birth | 2016-10-26 |
| Vaccinated?   | True |
| Owner ID      | 3821 |

2. Add the following details of a new owner and their pet to the database.

| Field    | Value |
| -----    | ----- |
| Owner ID | 3905 |
| Forename | Gary |
| Surname  | Hughes |
| Address  | 13 Juniper Place |
| Town     | Wemyss Bay |
| Phone    | 07998765432 |

| Field         | Value |
| -----         | ----- |
| Pet code      | P2751 |
| Pet name      | Usain |
| Pet type      | Tortoise |
| Date of birth | 2006-10-28 |
| Vaccinated?   | False |
| Owner ID      | 3905 |

3. Add the following details of a pet and their owner to the database.

| Field         | Value |
| -----         | ----- |
| Pet code      | P0438 |
| Pet name      | Arnie |
| Pet type      | Budgie |
| Date of Birth | 13 March 2017 |
| Vaccinated?   | No |

| Field     | Value |
| -----     | ----- |
| Owner ID  | 2664 |
| Forename  | Hannah |
| Surname   | Black |
| Address   | 47 High Road |
| Town      | Greenock |
| Telephone | 01475633633 |
