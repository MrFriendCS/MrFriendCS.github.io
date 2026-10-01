# N5 CS 2020 Task 1 Part B


File: [AnyTimeFlowers.db](assets/AnyTimeFlowers.db "Download file")


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

***1b*** Using the data dictionary, complete the relational database by:

* identifying two fields where the validation shown below has yet to be applied
* adding the validation to the two identified fields

Print evidence to show that you have added the validation to the database to match the data dictionary requirements.

(**2 marks**)


***1c (i)*** A customer would like to change their order from ‘rose’ to ‘tulip’.
The price of the order will change from £34 to £17. The orderID is CHQ3848.

Implement **one** SQL statement that will make the required changes to the order.

(**4 marks**)

Print evidence of the SQL statement and the FlowerOrder table, clearly showing that the changes have been implemented.


***1c (ii)*** A new customer provides their name and telephone number.

Implement an SQL statement that will add their details to the database.

```
    Name: Richard Glass
    Telephone number: 07654029336
	
Assign them customerID — 2986
```

Print evidence of the SQL statement and the Customer table, clearly showing that the changes have been implemented.

(**2 marks**)
