# N5 CS 2018 Task 1 Part B


File: [Gardening.db](assets/Gardening.db "Download file")


## Data Dictionary


### Table: Staff

| Attribute  | Key   | Type   | Size  | Req'd | Validation |
| ---------  | :---: | ----   | :---: | :---: | ---------- |
| staffID    | PK    | text   | 5     | Y     | length = 5 |
| forename   |       | text   | 20    | Y     |            |
| surname    |       | text   | 20    | Y     |            |
| address    |       | text   | 50    | Y     |            |
| topSkill   |       | text   | 5     | Y     | restricted choice: lawn, hedge, weeds |
| custRating |       | number |       | N     | Range >= 1 and <= 10 |


### Table: Job

| Attribute    | Key   | Type   | Size  | Req'd | Validation |
| ---------    | :---: | ----   | :---: | :---: | ---------- |
| jobID        | PK    | number |       | Y     |            |
| jobDate      |       | date   |       | Y     |            |
| jobTime      |       | time   |       | Y     | range: >= 09:00 and <= 18:00 |
| custName     |       | text   | 40    | Y     |            |
| custAddress  |       | text   | 50    | Y     |            |
| custPostcode |       | text   | 8     | Y     |            |
| phoneNo      |       | text   | 11    | N     |            |
| task         |       | text   | 12    | Y     | restricted choice: Lawn Mowed, Hedge Cut, Weeds Pulled |
| staffID      | FK    | text   | 5     | Y     | existing staffID from Staff table |


___1c___ Using the data dictionary complete the relational database by:

* creating a new table to store the job details
* adding all validation to the job entity
* creating a relationship between the two tables

(__5 marks__) 


___1d___ Staff member DS021 has moved house recently.

Implement an SQL statement that will change the address of this member of staff to:

* 99 Willow Way, Falkirk, FA87 6FE

Print evidence of your SQL statement and the Staff table (clearly showing the new address) once the SQL statement has been implemented.

(__2 marks__)
