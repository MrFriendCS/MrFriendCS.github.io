# N5 DDD Insert Queries Part 2


File: [Clydeview.db](../N5-DDD-Clydeview/assets/Clydeview.db "Download file")


## Database


### Table: Product

| Field          | Key  | Type    | Size | Req’d | Validation |
| -----          | :--: | ----    | :--: | :---: | ---------- |
| name           |      | Text    | 30   |       | |
| code           | PK   | Text    | 4    | Y     | |
| stock          |      | Number  |      | Y     | Range: >= 0 and <= 50 |
| onOrder        |      | Boolean |      |       | |
| price          |      | Number  |      | Y     | Range: > 1.00 |
| manufacturerID | FK   | Number  |      | Y     | manufacturerID exists in Manufacturer table |


### Table: Manufacturer

| Field          | Key  | Type    | Size | Req’d | Validation |
| -----          | :--: | ----    | :--: | :---: | ---------- |
| manufacturerID | PK   | Number  |      | Y     | |
| name           |      | Text    | 30   |       | |
| address        |      | Text    | 50   |       | |
| telephone      |      | Text    | 13   |       | |


### Entity Relationship Diagram (ERD)

![ERD](assets/erd2.png)


## Tasks

Using SQL queries:

1. Add details of this new product to the database.

| Field           | Value |
| -----           | ----- |
| Product name    | Spirit Level |
| Product code    | SPL3 |
| Number in stock | 14 |
| On order?       | False |
| Price (£)       | 17.99 |
| Manufacturer ID | 531 |


{:start="2"}
2. Add the following manufacturer and product details to the database.

| Field             | Value |
| -----             | ----- |
| Manufacturer ID   | 327 |
| Manufacturer name | CVA Group |
| Address           | 35 Lomond Way Paisley |
| Telephone         | 01414141414 |


| Field           | Value |
| -----           | ----- |
| Product name    | Circular Saw |
| Product code    | CSW2 |
| Number in stock | 3 |
| On order?       | No |
| Price (£)       | 99.00 |
| Manufacturer ID | 327 |

{:start="3"}
3. Add the following product and manufacturer details to the database.

| Field           | Value |
| -----           | ----- |
| Product name    | 6 piece Chisel Set |
| Product code    | CSP6 |
| Number in stock | 8 |
| On order?       | Yes |
| Price (£)       | 43.51 |
| Manufacturer ID | 408 |

| Field             | Value |
| -----             | ----- |
| Manufacturer ID   | 408 |
| Manufacturer name | Cabinet Makers |
| Address           | 158 Hawthorn Road Carlisle |
| Telephone         | 03217329124 |
