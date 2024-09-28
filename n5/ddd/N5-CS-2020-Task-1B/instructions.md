# N5 CS 2020 Task 1 Part B


File: [anyTimeFlowers.db](assets/anyTimeFlowers.db "Download file")


## Data Dictionary

### Table: Customer

| Attribute   | Key   | Type   | Size  | Req'd | Validation  |
| ---------   | :---: | ----   | :---: | :---: | ----------  |
| customerID  | PK    | number |       | Y     |             |
| forename    |       | text   | 40    | Y     |             |
| surname     |       | text   | 50    | Y     |             |
| address     |       | text   | 100   | N     |             |
| telephoneNo |       | text   | 11    | N     | Length = 11 |

### Table: FlowerOrder

| Attribute  | Key   | Type    | Size  | Req'd | Validation |
| ---------  | :---: | ----    | :---: | :---: | ---------- |
| orderID    | PK    | text    | 10    | Y     |            |
| dateDue    |       | date    |       | Y     |            |
| price      |       | number  |       | Y     | Range: >= 5.00 and <= 50.00 |
| flowerType |       | text    | 8     | Y     | Restricted choice: rose, lily, tulip, daffodil  |
| bunchSize  |       | tex   t | 6     | Y     | Restricted choice: small, medium, large |
| chocolates |       | Boolean |       | Y     |            |
| message    |       | text    | 200   | N     |            |
| customerID | FK    | number  |       | Y     | Existing customerID from Customer table |


## Tasks

___1b___ Using the data dictionary, complete the relational database by:

* identifying two fields where the validation shown below has yet to be applied
* adding the validation to the two identified fields

Print evidence to show that you have added the validation to the database to match the data dictionary requirements.  (__2 marks__)


___1c (i)___ A customer would like to change their order from ‘rose’ to ‘tulip’. The price of the order will change from £34 to £17. The orderID is CHQ3848.

Implement __one__ SQL statement that will make the required changes to the order. (__4 marks__)

Print evidence of the SQL statement and the FlowerOrder table, clearly showing that the changes have been implemented.


___1c (ii)___ A new customer provides their name and telephone number.

Implement an SQL statement that will add their details to the database.

```
    Name: Richard Glass
    Telephone number: 07654029336
	
Assign them customerID — 2986
```

Print evidence of the SQL statement and the Customer table, clearly showing that the changes have been implemented.  (__2 marks__)
