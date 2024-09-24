-- Don't change lines 1 to 5
.open carServices.db
.headers on
.mode column
-- Don't change lines 1 to 5


.print H CS 2020 Task 1 Part B


.print
.print Q1b(i)
SELECT garageName, SUM(cost) AS [Total Sales]
    FROM Garage, Job
    WHERE Garage.garageID = Job.garageID
        AND dateOut = "2020-01-19"
    GROUP BY garageName;


.print
.print Q1b(ii)
CREATE TEMP VIEW LongestStay (maxStay) AS
    SELECT MAX(JULIANDAY(dateOut) - JULIANDAY(dateIn))
    FROM Job;


SELECT maxStay AS [Number of days], regNo, garageName
    FROM LongestStay, Garage, Job
    WHERE Garage.garageID = Job.garageID
        AND JULIANDAY(dateOut) - JULIANDAY(dateIn) = maxStay;


.print