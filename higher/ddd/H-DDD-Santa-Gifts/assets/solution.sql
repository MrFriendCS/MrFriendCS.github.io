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



-- Task 9 - 
UPDATE Child
    SET nice = FALSE
    WHERE lastName = "Friend";


-- Task 10 - 
CREATE TEMP VIEW Naughty (childID) AS
    SELECT childID
    FROM Child
    WHERE lastName = "Friend";

UPDATE Gift
    SET item = "Lump of coal",
        cost = 0.50
    WHERE childID IN 
        (SELECT childID
             FROM Naughty);

