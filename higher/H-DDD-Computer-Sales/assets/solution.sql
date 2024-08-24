-- Don't touch lines 1 to 5
.open ComputerSales.db
.headers ON
.mode column
-- Don't touch lines 1 to 5


.print Q1
SELECT locality AS Location
FROM employee
ORDER BY locality;


.print
.print Q2
SELECT locality AS Location
FROM employee
GROUP BY locality
ORDER BY locality;

.print
.print Q3
SELECT model.name, manufacturer.name
FROM model, manufacturer
WHERE model.manufacturer_id = manufacturer.manufacturer_id
ORDER BY manufacturer.name ASC, model.name DESC;


.print
.print Q4
SELECT mo.name AS Model, ma.name AS Manufacturer
FROM model AS mo, manufacturer AS ma
WHERE mo.manufacturer_id = ma.manufacturer_id
ORDER BY ma.name ASC, mo.name DESC;


.print
.print Q5
SELECT COUNT(*)
FROM sales;


.print
.print Q6
SELECT MAX(price)
FROM sales;


.print
.print Q7
SELECT COUNT(*)
FROM sales
WHERE price =
    (SELECT MAX(price)
    FROM sales);


.print
.print Q8
SELECT MIN(price) AS Minimum, ROUND(AVG(price), 2) AS Average, MAX(price) AS Maximum
FROM sales;


.print
.print Q9
SELECT name, cpu_speed AS "Speed (GHz)", ram
FROM model
WHERE name LIKE "%Pi%";


.print
.print Q10
SELECT COUNT(sale_id)
FROM sales
WHERE sale_date >= "2019-07-01";


.print
.print Q11
SELECT SUM(price)
FROM sales;


.print
.print Q12
SELECT SUM(price)
FROM sales
WHERE sale_date >= "2019-06-01" AND sale_date <= "2019-06-30";


.print
.print Q13
SELECT SUM(price) * 0.2
FROM sales
WHERE sale_date >= "2019-01-01" AND sale_date <= "2019-12-31";


.print
.print Q14
SELECT sale_date, COUNT(sale_date)
FROM sales
WHERE sale_date >= "2019-06-01" AND sale_date <= "2019-06-30"
GROUP BY sale_date
ORDER BY sale_date;


.print
.print Q15
SELECT SUM(price)
FROM sales, returns
WHERE sales.sale_id = returns.sale_id;

