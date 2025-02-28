# N5 CS 2023 Task 2C


File: [Maintenance.db](assets/Maintenance.db "Download file")


## Data Dictionary

### Entity: Staff

| Attribute  | Key   | Type | Size  | Req'd | Validation |
| ---------  | :---: | ---- | :---: | :---: | ---------- |
| forename   |       | text | 30    | N     |            |
| surname    |       | text | 60    | N     |            |
| department |       | text | 10    | N     | restricted choice: admin, sales and management |
| email      | PK    | text | 100   | Y     |            |

### Entity: Problem

| Attribute   | Key   | Type    | Size  | Req'd | Validation |
| ---------   | :---: | ----    | :---: | :---: | ---------- |
| problemID   | PK    | number  |       | Y     |            |
| email       | FK    | text    | 100   | Y     |            |
| dateRaised  |       | date    |       | Y     |            |
| description |       | text    | 255   | Y     |            |
| rating      |       | number  |       | Y     | range: >= 1 and <= 4 |
| completed   |       | boolean |       | Y     |            |


___2c___ Using the data dictionary above, complete the relational database by adding the required validation to the department field.

Print evidence of the implemented department field validation. 
 (__1 mark__)

Eva Livingstone has moved from sales to management.


___2d(i)___ Implement the SQL statement that will make the following change:

```
forename: Eva 
surname: Livingstone 
department: management 
email: eliv123@email.net 
```

Print evidence of the SQL statement and the Staff table, clearly showing that the change has been implemented.  (__2 marks__)


___2d(ii)___ The support team notice that a lot of issues were raised on 7th July 2022.

Implement an SQL statement to output the forename, surname and problem description for all problems raised on 7th July 2022 which remain incomplete. Sort the list based on the urgency of the problems (most urgent first).  (__5 marks__)

Print evidence of the SQL statement and the output.


___2e___ Fiona Bradley no longer wants problem ID106 recorded on the database, as a colleague has already reported the issue.

The following SQL statement was written to remove the entry but is not fit for purpose.

```sql
DELETE *
    FROM Problem
    WHERE rating = 1
        AND email = "fbr530@email.net";
```


___2e(i)___ Explain why this query is not fit for purpose.  (__1 mark__)


___2e(ii)___ Describe how this query could be improved to ensure it is fit for purpose.  (__1 mark__)
