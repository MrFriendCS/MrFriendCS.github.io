-- H CS 2020 Task 1 Part C - Extension


-- Q1d(i)
CREATE TEMP VIEW ExpensiveJob AS
    SELECT MAX(cost) AS expensive
        FROM Job;

SELECT forename,
       surname,
       address,
       Car.regNo
    FROM Job,
         Car,
         Customer,
         ExpensiveJob
    WHERE cost = expensive
      AND Job.RegNo = Car.regNo
      AND Car.customerID = Customer.customerID;


-- Q1d(ii)
CREATE TEMP VIEW CheapestJob AS
    SELECT MIN(cost) AS cheapest
        FROM Job;

SELECT make,
       model
    FROM Car,
         Job,
         CheapestJob
    WHERE cost < cheapest + 20 
      AND Job.regNo = Car.regNo;


-- Q1d(iii)
CREATE TEMP VIEW GarageJobs AS
    SELECT garageName,
           COUNT(*) AS jobs
        FROM Garage,
             Job
        WHERE Garage.garageID = Job.garageID
        GROUP BY garageName;

SELECT garageName
    FROM GarageJobs
    WHERE jobs < 15;


-- Q1d(iv)
CREATE TEMP VIEW GarageName AS
    SELECT garageName,
           COUNT(Customer.customerID) AS customerCount
        FROM Garage,
             Job,
             Car,
             Customer
        WHERE Garage.garageID = Job.garageID
          AND Job.RegNo = Car.regNo
          AND Car.customerID = Customer.customerID
        GROUP BY garageName;

SELECT MAX(customerCount) AS [Most customers in a garage]
    FROM GarageName;

