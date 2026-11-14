/*
Title: H DDD Computer sale
Author: Mr Friend
Date: 14 Nov 2026
*/


-- Q1
SELECT town
    FROM Employee
    GROUP BY town;


-- Q2
SELECT manufacturer.name,
       model.name
    FROM Model,
         Manufacturer
    WHERE model.manufacturerID = manufacturer.manufacturerID
    ORDER BY manufacturer.name ASC,
             model.name DESC;


-- Q3
SELECT COUNT(*) AS [Number of Sales]
    FROM Sale;


-- Q4
SELECT MAX(price) AS [Highest Sale]
    FROM Sale;


-- Q5
SELECT MIN(price) AS Minimum,
       ROUND(AVG(price), 2) AS Average,
       MAX(price) AS Maximum
    FROM Sale;

    
-- Q6
SELECT name,
       cpuSpeed AS [Speed (GHz)],
       ram AS RAM
    FROM Model;


-- Q7
SELECT name,
       cpuSpeed AS [Speed (GHz)],
       ram AS RAM
    FROM Model
    WHERE name LIKE "%Pi%";


-- Q8
SELECT SUM(price) AS [2019 Sales]
    FROM Sale
    WHERE saleDate >= "2019-01-01"
      AND saleDate <= "2019-12-31";


-- Q9
SELECT ROUND(SUM(price) * 0.2, 2) AS [2019 VAT]
    FROM Sale
    WHERE saleDate >= "2019-01-01"
      AND saleDate <= "2019-12-31";
      

-- Q10
SELECT COUNT(saleID) AS [Jul-Dec Sales]
    FROM sale
    WHERE saleDate >= "2019-07-01"
      AND saleDate <= "2019-12-31";


-- Q11
SELECT ROUND(AVG(price), 2) AS [Average June Sale Price]
    FROM Sale
    WHERE saleDate >= "2019-06-01"
      AND saleDate <= "2019-06-30";
      

-- Q12
SELECT saleDate, COUNT(saleID) AS [Number of Sales]
    FROM Sale
    WHERE saleDate >= "2019-06-01"
      AND saleDate <= "2019-06-30"
    GROUP BY saleDate
    ORDER BY saleDate ASC;


-- Q13
CREATE TEMP VIEW MaxPrice (maxPrice) AS
    SELECT MAX(price)
    FROM Sale;

SELECT COUNT(price) [Number of Max Prices]
    FROM Sale, MaxPrice
    WHERE price = maxPrice;
