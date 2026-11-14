/*
Title: H DDD Computer Sales
Author: Mr Friend
Date: 14 Nov 2026
*/


-- Q1
SELECT locality
    FROM employee
    GROUP BY locality;


-- Q2
SELECT manufacturer.name,
       model.name
    FROM model,
         manufacturer
    WHERE model.manufacturerID = manufacturer.manufacturerID
    ORDER BY manufacturer.name ASC,
             model.name DESC;


-- Q3
SELECT COUNT(*)
    FROM sales;


-- Q6
SELECT MAX(price)
    FROM sales;


-- Q7
SELECT COUNT(*)
    FROM sales
    WHERE price =
        (SELECT MAX(price)
        FROM sales);


-- Q8
SELECT MIN(price) AS Minimum,
       ROUND(AVG(price), 2) AS Average,
       MAX(price) AS Maximum
    FROM sales;


-- Q9
SELECT name,
       cpuSpeed AS "Speed (GHz)",
       ram
    FROM model
    WHERE name LIKE "%Pi%";


-- Q10
SELECT COUNT(saleID)
    FROM sales
    WHERE saleDate >= "2019-07-01";


-- Q11
SELECT SUM(price)
    FROM sales;


-- Q12
SELECT SUM(price)
    FROM sales
    WHERE saleDate >= "2019-06-01"
      AND saleDate <= "2019-06-30";


-- Q13
SELECT SUM(price) * 0.2
    FROM sales
    WHERE saleDate >= "2019-01-01"
      AND saleDate <= "2019-12-31";


-- Q14
SELECT saleDate, COUNT(saleDate)
    FROM sales
    WHERE saleDate >= "2019-06-01"
      AND saleDate <= "2019-06-30"
    ORDER BY saleDate;


-- Q15
SELECT SUM(price)
    FROM sales, returns
    WHERE sales.saleDate = returns.saleDate;
