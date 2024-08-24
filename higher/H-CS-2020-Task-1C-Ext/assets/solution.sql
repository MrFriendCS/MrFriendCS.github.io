-- Don't change lines 1 to 5
.open carServices.db
.headers on
.mode column
-- Don't change lines 1 to 5


.print H CS 2020 Task 1 Part C - Extension


.print
.print Q1d(i)
CREATE TEMP VIEW expensive (most_expensive) AS
    SELECT MAX(cost)
    FROM Job;

SELECT forename, surname, address, Car.regNo
    FROM Job, Car, Customer, expensive
    WHERE cost = most_expensive
        AND Job.RegNo = Car.regNo
        AND Car.customerID = Customer.customerID;

.print
.print Q1d(ii)
CREATE TEMP VIEW cheapest (most_cheapest) AS
    SELECT MIN(cost)
    FROM Job;

SELECT make, model
    FROM Car, Job, cheapest
    WHERE cost < most_cheapest + 20 
        AND Job.regNo = Car.regNo;

.print
.print Q1d(iii)
CREATE TEMP VIEW garage_job AS
    SELECT garageName, COUNT(*) AS GarageJobs
        FROM Garage, Job
        WHERE Garage.garageID = Job.garageID
        GROUP BY garageName;

SELECT garageName
    FROM garage_job
    WHERE garageJob < 15;

.print
.print Q1d(iv)
CREATE TEMP VIEW garage_name AS
    SELECT garageName, COUNT(*) AS customerCount
        FROM Garage, Job, Car, Customer
        WHERE Garage.garageID = Job.garageID
            AND Job.RegNo = Car.regNo
            AND Car.customerID = Customer.customerID
        GROUP BY garageName;

SELECT MAX(customerCount) AS [Most customers in a garage]
    FROM garage_name;

.print
