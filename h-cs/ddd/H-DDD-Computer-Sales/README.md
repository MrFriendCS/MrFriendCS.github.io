# H DDD Computer Sales

Use appropriate aliases.

## Tasks

1. Display the locality of the employees without any duplication.

2. Create a query that returns the names of the manufacturers and the computer models.
Sort the results alphabetically for manufacturers and in reverse for the models.

3. Display the number of sales.

9. Create a query to return the highest sale.

10.  Create a query to count the Number of sales that are equal to the highest sale.

11. Create a query to return the minimum, average, and maximum prices of all sales.

12. Modify the query to round the average value to 2 decimal places.

13. Modify the query and give each of the returned columns an appropriate name.

14. Create a query that returns the name, CPU speed, and RAM of all the different computer
models.

15. Rename the CPU speed column as 'Speed (GHz)'.

16. Modify the query to return only the computers with 'Pi' in their names.

17. Create a query that counts the sales in the last six months of 2019.

18. Create a query that calculates the value of all the sales in 2019.
Use an appropriate alias.

19. Using the last query, calculate the value of all the sales June 2019.
Use an appropriate alias.

20. Create a query to calculate the VAT due to be paid to HMRC on all the sales in 2019.
VAT is 1/6 (a sixth) of the sale price. The calculation will need to use a decimal, not a percentage.

21. Create a query to display the Number of sales per day in June 2019, in date order.

22. Calculate the value of all the returns in 2019.


## Data Dictionary


### Table: Employee
| Attribute   | Key   | Req'd | Type   | Size | Validation |
| ---------   | :---: | :---: | ---    | :--: | ---------- |
| employeeID  | PK    | Y     | Text   | 10   | Range: >= 0 |
| firstName   |       | Y     | Text   | 15   | Length: >= 3 |
| lastName    |       | Y     | Text   | 20   | Length: >= 3 |
| houseNo     |       |       | Number |      | Range: > 0|
| street      |       |       | Text   |      | |
| town        |       |       | Text   |      | |
| county      |       |       | Text   |      | |
| postcode    |       |       | Text   |      | |
| phone       |       |       | Text   |      | Length: = 11 |
| daysPerWeek |       | Y     | Number |      | Range: >= 0.0 and <= 7.0 |


### Table: Manufacturer

| Attribute      | Key   | Req'd | Type    | Size | Validation |
| ---------      | :---: | :---: | ----    | :--: | ---------- |
| manufacturerID | PK    | Y     | Number  |      | Range: >= 1 |
| name           |       | Y     | Text    | 30   | |
| website        |       |       | Text    | 50   | |
| yearFounded    |       |       | Number  |      | Range: >= 1900 |
| trading        |       | Y     | Boolean |      | |


### Table: Model

| Attribute      | Key   | Req'd | Type    | Size | Validation |
| ---------      | :---: | :---: | ----    | :--: | ---------- |
| modelID        | PK    | Y     | Number  |      | Range: >= 1 |
| manufacturerID | FK    | Y     | Number  |      | Exists in Manufacturer table |
| name           |       | Y     | Text    | 20   | |
| cpuSpeed       |       |       | Number  |      | Range: > 0 |
| ram            |       |       | Number  |      | Range: > 0.0 |
| cores          |       |       | Number  |      | Range: >= 1 |
| wifi           |       |       | Boolean |      | Restricted choice: True, False |
| releaseDate    |       |       | Date    |      | |


### Table: Sale

| Attribute  | Key   | Req'd | Type   | Size | Validation |
| ---------  | :---: | :---: | ----   | :--: | ---------- |
| saleID     | PK    | Y     | Number |      | Range: >= 1 |
| modelID    | FK    | Y     | Number |      | Exists in Model table |
| saleDate   |       | Y     | Text   |      | |
| employeeID | FK    | Y     | Text   |      | Exists in Employee table |
| price      |       | Y     | Number |      | Range: >= 0.0 |
