# H DDD Computed Values Part 2

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


## Table: Table1

| Name     | Key | Type   | Size | Req'd | Validation |
| ----     | --- | ----   | ---- | ----- | ---------- |
| pupilID  | PK  | Number |      | Y     |  |
| forename |     | Text   | 12   | Y     |  |
| surname  |     | Text   | 12   | Y     |  |
| test1    |     | Number |      | Y     | Range: >= 0 and <=10 |
| test2    |     | Number |      | Y     | Range: >= 0 and <=10 |
| test3    |     | Number |      | Y     | Range: >= 0 and <=10 |
| test4    |     | Number |      | Y     | Range: >= 0 and <=10 |

The table called Table1 stores the test results of several pupils.

1.  Update the records using a SQL query to add 1 to each of the test 3 results.


## Table: Table2

| Name        | Key | Type   | Size | Req'd | Validation |
| ----        | --- | ----   | ---- | ----- | ---------- |
| staffID     | PK  | Number |      | Y     | | 
| forename    |     | Text   | 12   | Y     | | 
| surname     |     | Text   | 12   | Y     | | 
| hourlyRate  |     | Number |      | Y     | Range: >= 0 | 
| hoursWorked |     | Number |      | Y     | Range: >= 0 | 

The table called Table2 stores the hours worked and hourly rate of some staff members.

Members of staff who earn less than £7 per hour are due to receive a 10% pay rise.

{:start="2"}
2.  Use a SQL query to amend the required details of the relevant records.

 

## Table: Table3

| Name      | Key | Type   | Size | Req'd | Validation |
| ----      | --- | ----   | ---- | ----- | ---------- |
| studentID | PK  | Number |      | Y     | |
| forename  |     | Text   | 50   | Y     | |
| surname   |     | Text   | 50   | Y     | |
| test1     |     | Number |      | Y     | Range: >= 0 and <=20 |
| test2     |     | Number |      | Y     | Range: >= 0 and <=20 |
| test3     |     | Number |      | Y     | Range: >= 0 and <=20 |
| test4     |     | Number |      | Y     | Range: >= 0 and <=20 |
| test5     |     | Number |      | Y     | Range: >= 0 and <=20 |

The table called Table3 stores the details of students and the marks they achieved in monthly tests (each test was out of 16 marks).

Both students whose surname starts with the letter `S` have found errors in their test results for test 2 and test 4.

{:start="3"}
3.  Use a single SQL query to changed the required records. 
Increase each of their test 2 results by 2 marks and each of their test 4 results by 1 mark.



## Table: Table4

| Name         | Key | Type   | Size | Req'd | Validation |
| ----         | --- | ----   | ---- | ----- | ---------- |
| product      | PK  | Number |      | Y     | |
| productName  |     | Text   | 12   | Y     | |
| buyingPrice  |     | Number | 50   | Y     | Range: >= 0 |
| sellingPrice |     | Number |      | Y     | Range: >= 0 |

The table called Table4 stores details of items for sale in the school tuckshop.

The buying price of the product with a product name ending in `e`, has been reduced by 2 pence.
Also, the selling price is being updated to make a profit of 40% of the revised buying price.

{:start="4"}
4.  Use two SQL queries to alter the buying price and selling price of the relevant product records.
 

## Table: Table5

| Name        | Key | Type   | Size | Req'd | Validation |
| ----        | --- | ----   | ---- | ----- | ---------- |
| productName |     | Text   | 20   | Y     | |
| productID   | PK  | Text   | 50   | Y     | |
| priceUK     |     | Number |      | Y     | Range: >= 0.00 |

The table called Table5 stores details of products and their prices.

Some of the product names in this table contain the letter `a` followed by another letter which in turn, is followed by a space.
The price of these products is to be increased by 12%.

{:start="5"}
5.  Use a SQL query to amend the relevant records.


## Table6

| Name          | Key | Type   | Size | Req'd | Validation |
| ----          | --- | ----   | ---- | ----- | ---------- |
| fishType      | PK  | Text   | 12   | Y     | |
| pricePerKilo  |     | Number |      | Y     | Range: >= 0.00 |
| numberOfKilos |     | Number |      | Y     | Range: >= 0.0 |

The table called Table6 stores details of fish sales for a fish wholesaler.

Every week, the wholesaler reduces the price of some of the fish.
This week, the second letter of each type of fish reduced is the letter `o` and each type of reduced fish has at least 4 letters.

{:start="6"}
6.  Use a single SQL query to reduce the price of these fish by 10% but at the same time, double the number of kilos of fish.
