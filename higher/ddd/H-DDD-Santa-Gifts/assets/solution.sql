/*
Title: H DDD Santa Gifts
Author: Mr Friend
Date: 12 Dec 2024
*/

-- Task 1 - Number of children
SELECT COUNT(*) AS Children
    FROM Child;


-- Task 2 - Number of Gifts
SELECT COUNT(*) AS Gifts
    FROM Gift;


-- Task 3 - 
SELECT SUM(cost) AS [Cost (£)]
    FROM Gift;


-- Task 4 - 
SELECT ROUND(SUM(cost) * 14.079458, 0) 
       AS [Cost (NOK)]
    FROM Gift;


-- Task 5 - 
SELECT ROUND(AVG(cost), 2) As Average
    FROM Gift;


-- Task 5 - 
SELECT lastName, COUNT(*) AS Children
    FROM Child
    GROUP BY lastName;


-- Task 6 - 
SELECT nice, COUNT(*) AS Children
    FROM Child
    GROUP BY nice;


-- Task 7 - 
SELECT lastName, nice, COUNT(*) AS Children
    FROM Child
    GROUP BY lastName, nice;


-- Task 8 - 



-- Task9 - 


-- Task 10 - 


