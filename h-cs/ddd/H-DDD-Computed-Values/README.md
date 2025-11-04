# H DDD Computed Values Task 4

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

1.	Use a SQL query to list the full name of each pupil together with
 the pupil's total mark for all 4 tests.
2.	Use a SQL query to list the first name of each pupil with their 
4 test marks and the average mark for the 4 tests.  
These details should be arranged so that the pupil with the highest 
average mark is listed first.


## Table: Table2

| Name        | Key | Type   | Size | Req'd | Validation |
| ----        | --- | ----   | ---- | ----- | ---------- |
| staffID     | PK  | Number |      | Y     | | 
| forename    |     | Text   | 12   | Y     | | 
| surname     |     | Text   | 12   | Y     | | 
| hourlyRate  |     | Number |      | Y     | Range: >= 0 | 
| hoursWorked |     | Number |      | Y     | Range: >= 0 | 

The table called Table2 stores the hours worked and hourly rate of some staff members.

{:start="3"}
3.	Use a SQL query to list the full name of each member of staff together
 with their total wage.
4.	Use a SQL query to list the full name of all members of staff whose wage is over £200.
 
The table called Table3 stores the details of students and the marks they achieved in monthly tests 
(each test was out of 16 marks).


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

{:start="5"}
5.	Use a SQL query to list each test mark as a percentage.
NB: To generate the percentages, divide each mark by 16 and multiply by 100.
6.	Use a SQL query to list the full name of each student together with the
student's total mark as a percentage.  These details should be listed from smallest percentage to largest; 
students with the same percentage should be listed in alphabetical order of surname.


## Table: Table4

| Name         | Key | Type   | Size | Req'd | Validation |
| ----         | --- | ----   | ---- | ----- | ---------- |
| product      | PK  | Number |      | Y     | |
| productName  |     | Text   | 12   | Y     | |
| buyingPrice  |     | Number | 50   | Y     | Range: >= 0 |
| sellingPrice |     | Number |      | Y     | Range: >= 0 |

The table called Table4 stores details of items for sale in the school tuckshop.

{:start="7"}
7.	Use a SQL query to list the name of each item, its buying price, selling price and the profit or loss for that item.
8.	Use a SQL query to list the name of each loss-making item with the amount of its loss.  
The items should be arranged so that the item with the smallest loss is listed first.

NB: Profit = Sale price – Cost Price
 

## Table: Table5

| Name        | Key | Type   | Size | Req'd | Validation |
| ----        | --- | ----   | ---- | ----- | ---------- |
| productName |     | Text   | 20   | Y     | |
| productID   | PK  | Text   | 50   | Y     | |
| priceUK     |     | Number |      | Y     | Range: >= 0.00 |

The table called Table5 stores details of products and their prices.

{:start="9"}
9.	Use a SQL query to list the products name, UK price and the equivalent prices in Euros.
10.	Use a SQL query to list the ID of any products that cost most than $40 dollars. 
The query should show the UK prices as well as the equivalent prices in US Dollars.  
The products should be listed with the cheapest displayed first; products that cost the same should be listed with the highest productID shown first.

Notes:

- £1 buys €1.13
- £1 buys $1.39
- use the round() function to round the results to 2 decimal places


## Table6

| Name          | Key | Type   | Size | Req'd | Validation |
| ----          | --- | ----   | ---- | ----- | ---------- |
| fishType      | PK  | Text   | 12   | Y     | |
| pricePerKilo  |     | Number |      | Y     | Range: >= 0.00 |
| numberOfKilos |     | Number |      | Y     | Range: >= 0.0 |

The table called Table6 stores details of fish sales for a fish wholesaler.

{:start="11"}
11.	Use a SQL query to list the full details of each type of fish together
 with the total cost of each sale.
12.	Use a SQL query to list the name of type of fish that has sales between
 £20 and £50.  The results should be listed with the dearest sales displayed first.
