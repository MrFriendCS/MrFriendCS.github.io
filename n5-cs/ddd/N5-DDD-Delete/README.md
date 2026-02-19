# N5 DDD Delete Queries


File: [Clydeview.db](../N5-DDD-Clydeview/assets/Clydeview.db "Download file")


## Database


### Table: Owner

| Field     | Key  | Type   | Size | Req’d | Validation |
| -----     | :--: | ----   | :--: | :---: | ---------- |
| ownerID   | PK   | Number |      | Y     | |
| forename  |      | Text   | 20   |       | |
| surname   |      | Text   | 30   |       | |
| address   |      | Text   | 50   |       | | 
| town      |      | Text   | 20   |       | |
| telephone |      | Text   | 13   |       | |


### Table: Pet

| Field       | Key  | Type    | Size | Req’d | Validation |
| -----       | :--: | ----    | :--: | :---: | ---------- |
| code        | PK   | Text    |      | Y     | |
| name        |      | Text    | 20   |       | |
| type        |      | Text    | 8    |       | Restricted choice: Cat, Dog, Budgie, Gerbil, Tortoise |
| dateOfBirth |      | Date    |      |       | |
| vaccination |      | Boolean |      |       | |
| ownerID     | FK   | Number  |      | Y     | ownerID exists in Owner table |


### Entity Relationship Diagram (ERD)

![ERD](assets/erd1.png)


## Tasks

Using SQL queries:

1. Remove details of Slinky the tortoise from the database.

2. Remove the details of the owner with Owner ID 3510 from the database.

3. Remove the details of the pet called Usain from the database.

