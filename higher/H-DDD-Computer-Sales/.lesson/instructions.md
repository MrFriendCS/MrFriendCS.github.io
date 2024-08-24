# H DDD Computer Sales

## Tasks

1. Create a query to return the locality of the employees.

   1. Modify the query to rename the column heading as ‘Location’.

2. Modify the last query to group by locality and make the order alphabetical.

3. Create a query that returns the names of the computer models and the manufacturers.

   1. Modify the query to order the results alphabetically for manufacturers and in reverse for the models.

4. Modify the last query to use table aliases.  Use the first two letters of each table name used in the query, e.g. if the table name was ‘horse’ the table alias would be ‘ho’.

   1. Modify the query to use the table aliases in the `SELECT` statement.  Give the columns aliases as well: Model and Manufacturer.

5. Create a query to return the number of sales.

6. Create a query to return the highest sale.

7.  Create a query to count the number of sales that are equal to the highest sale.

8. Create a query to return the minimum, average, and maximum prices of all sales.

   1. Modify the query to round the average value to 2 decimal places.

   2. Modify the query and give each of the returned columns an appropriate name.

9. Create a query that returns the name, CPU speed, and RAM of all the different computer
models.

   1. Rename the CPU speed column as ‘Speed (GHz)’.

   2. Modify the query to return only the computers with ‘Pi’ in their names.

10. Create a query that counts the sales in the last six months of 2019.

11. Create a query that calculates the value of all the sales in 2019.  Use an appropriate alias.

12. Using the last query, calculate the value of all the sales June 2019.  Use an appropriate alias.

13. Create a query to calculate the VAT due to be paid to HMRC on all the sales in 2019.

VAT is 1/6 (a sixth) of the sale price. The calculation will need to use a decimal, not a percentage.

14. Create a query to display the number of sales per day in June 2019, in date order.

15. Calculate the value of all the returns in 2019.

## Data Dictionary

### Table: employee
| Attribute | Key | Req'd | Type | Validation |
| --- | :---: | :---: | --- | --- |
| employee_id | PK | Y | text | |
| first_name | | Y | text | |
| surname | | Y | text | |
| address_number | | | number | |
| address_1 | | | text | |
| address_2 | | | text | |
| locality | | | text | |
| region | | | text | |
| postal_code | | | text | |
| phone_number | | | text | |
| days_per_week | | Y | number | Range: >=0 and <= 7 |

### Table: manufacturer

| Attribute | Key | Req'd | Type | Validation |
| --- | :---: | :---: | --- | --- |
| manufacturer_id | PK | Y | integer | |
| name | | Y | text | |
| url | | | text | |
| year_founded | | | number | Range: >= 1900 |
| trading | | Y | text | Restricted choice: True, False |

### Table: model

| Attribute | Key | Req'd | Type | Validation |
| --- | :---: | :---: | --- | --- |
| model_id | PK | Y | number | |
| manufacturer_id | FK | Y | number | Exists in manufacturer table |
| name | | Y | text | |
| cpu_speed | | | number | Range: > 0 |
| ram | | | number | Range: > 0 |
| cores | | | number | Range: >= 1 |
| wifi | | | text | Restricted choice: True, False |
| release_date | | | text | |

### Table: returns

| Attribute | Key | Req'd | Type | Validation |
| --- | :---: | :---: | --- | --- |
| return_id | PK | Y | number | |
| sale_id | FK | Y | number | Exists in sales table |
| employee_id | FK | Y | text | Exists in employee table |
| date_returned | | Y | text | |
| reason | | Y | text | |

### Table: sales

| Attribute | Key | Req'd | Type | Validation |
| --- | :---: | :---: | --- | --- |
| sale_id | PK | Y | integer | |
| model_id | FK | Y | integer | Exists in model table |
| sale_date | | Y | text | |
| employee_id | FK | Y | text | Exists in employee table |
| price | | Y | number | Range: >= 0 |
