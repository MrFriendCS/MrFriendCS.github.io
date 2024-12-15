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


-- Task 3 - Mac or Mc
SELECT firstName, lastName
    FROM Child
    WHERE lastName LIKE "Mac%" 
       OR lastName LIKE "Mc%"
    ORDER BY firstName;


-- Task 4 - Cost of all goods
SELECT SUM(cost) AS [Cost (£)]
    FROM Gift;


-- Task 5 - Cost in Kroner
SELECT ROUND(SUM(cost) * 14.079458, 0) 
       AS [Cost (NOK)]
    FROM Gift;


-- Task 6 - Check estimated cost
SELECT ROUND(AVG(cost), 2) As Average
    FROM Gift;


-- Task 7 - Surnames with count
SELECT lastName, COUNT(*) AS Children
    FROM Child
    GROUP BY lastName;


-- Task 8 - Naughty / Nice with count
SELECT nice, COUNT(*) AS Children
    FROM Child
    GROUP BY nice;


-- Task 9 - Suranems and naughty / nice with count
SELECT lastName, nice, COUNT(*) AS Children
    FROM Child
    GROUP BY lastName, nice;


-- Task 10 - 



-- Task 9 - 
UPDATE Child
    SET nice = FALSE
    WHERE lastName = "Friend";


-- Task 10 - 
UPDATE Gift
    SET item = "Lump of coal",
        cost = 0.50
    WHERE childID IN 
        (SELECT childID
             FROM Child
             WHERE nice = FALSE);

