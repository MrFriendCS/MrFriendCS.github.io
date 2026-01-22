# H CS 2020 - Task 1 Part B


[Car services database](assets/CarServices.db)


After further analysis, the developer creates the entity-relationship diagram shown below.

![Car services ERD](assets/ERD.png)

The design is then implemented.


___1b(i)___ Customers pay for completed jobs on the day they take their car out of the garage.

The company wants to list the total value of sales (in £s) for each of its five garages on 19 January 2020.

Implement the SQL statement that will produce an output with the headings:

| garageName | Total sales |
| ---------- | ----------- |
|            | |

(__4 marks__)

Print evidence of:

* the implemented SQL statement
* the output it produced

Ensure your name and candidate number is on all evidence.


___1b(ii)___ The company wants to identify the details of the car that spent the most number of days in any of its garages.

Implement two SQL statements that will find the highest number of days, the registration number and the name of the garage where the car was repaired.

| Number of days | regNo | garageName |
| -------------- | ----- | ---------- |
|                |       | |

(__4 marks__)

Print evidence of:

* the implemented SQL statements
* the output produced from each statement

Ensure your name and candidate number is on all evidence.


___1c___ The company wants to produce a list of all customers and the average cost of jobs carried out on their car(s). 

They use the following SQL statement.

``` sql
SELECT forename, surname, AVG(cost) AS [Average Job Cost]
    FROM Customer, Car, Job
	WHERE Customer.customerID = Car.customerID
        AND Car.regNo = Job.regNo
	GROUP BY forename, surname
	ORDER BY AVG(cost) DESC;
```

Part of the expected output is shown below.

| forename | surname | Average Job Cost |
| -------- | ------- | ---------------- |
| Colin    | Wilson  | £701.10 |
| Derek    | Tsang   | £657.41 |
| Mark     | Jones   | £464.84 |
| Angela   | Smith   | £434.49 |
| Jennifer | Hart    | £414.31 |
| Angela   | Smith   | £408.85 |
| Colin    | Wilson  | £249.99 |
| Mark     | Jones   | £240.72 |
| …        | …       | … |

A query to test the above SQL statement is provided with the database.

Test the SQL statement by running the query then answer the questions.
