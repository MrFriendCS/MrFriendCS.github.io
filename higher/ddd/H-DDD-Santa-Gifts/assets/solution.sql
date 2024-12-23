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
    ORDER BY firstName ASC;


-- Task 4 - Lego gifts
SELECT item
    FROM Gift
    WHERE item LIKE "%LEGO%"
	GROUP BY item;


-- Task 5 - Cost of all goods
SELECT SUM(cost) AS [Cost (£)]
    FROM Gift;


-- Task 6 - Cost in Kroner
SELECT ROUND(SUM(cost) * 14.079458, 0) 
       AS [Cost (NOK)]
    FROM Gift;


-- Task 7 - Check estimated cost
SELECT ROUND(AVG(cost), 2) As Average
    FROM Gift;


-- Task 8 - Surnames with count
SELECT lastName, COUNT(*) AS Children
    FROM Child
    GROUP BY lastName;


-- Task 9 - Naughty / Nice with count
SELECT nice, COUNT(*) AS Children
    FROM Child
    GROUP BY nice;


-- Task 10 - Suranems and naughty / nice with count
SELECT lastName, nice, COUNT(*) AS Children
    FROM Child
    GROUP BY lastName, nice;


-- Task 11 - 5% decrease in gift Cost
UPDATE Gift
    SET cost = ROUND((cost * 0.95),2);


-- Task 12 - 5% decrease in gift Cost
SELECT *
    FROM Gift;


-- Task 12 - Most gifts

CREATE TEMP VIEW NiceKids (childID, giftCount) AS
    SELECT Child.childID, COUNT(*)
    FROM Child, Gift
    WHERE Child.childID = Gift.childID
      AND nice = TRUE
    GROUP BY Child.childID;

CREATE TEMP VIEW MaxGift (maxGift) AS
SELECT MAX(giftCount)
    FROM NiceKids;

SELECT firstName, lastName, maxGift AS Gifts
    FROM Child, NiceKids, MaxGift
    WHERE Child.childID = NiceKids.childID
      AND NiceKids.giftCount = maxGift
    ORDER BY firstName ASC, 
             lastName ASC;


-- Task 14 - Everyone gets a gift?

CREATE TEMP VIEW Present (childID) AS
    SELECT childID
    FROM Gift
    GROUP BY childID;

SELECT COUNT(*) AS Recipients
    FROM Present;


-- Task 15 - Naughty children!
UPDATE Child
    SET nice = FALSE
    WHERE lastName = "MacNeil";


-- Task 16 - Coal for naughty children
UPDATE Gift
    SET item = "Lump of coal",
        cost = 0.50
    WHERE childID IN 
        (SELECT childID
             FROM Child
             WHERE lastName = "MacNeil");


-- Task  - Show changes
SELECT *
    FROM Child, Gift
    WHERE Child.childID = Gift.childID
      AND lastName = "MacNeil"
    ORDER BY firstName ASC, 
             childID ASC;

-- Task 16 - Most coal

CREATE TEMP VIEW CoalKids (childID, coalCount) AS
    SELECT Child.childID, COUNT(*)
    FROM Child, Gift
    WHERE Child.childID = Gift.childID
	  AND item LIKE "%coal%"
	GROUP BY Child.childID;

CREATE TEMP VIEW MaxCoal (maxCoal) AS
	SELECT MAX(coalCount)
    FROM CoalKids;

SELECT firstName, lastName, maxCoal AS Lumps
    FROM Child, CoalKids, MaxCoal
    WHERE Child.childID = CoalKids.childID
      AND CoalKids.coalCount = maxCoal
    ORDER BY firstName ASC, 
             lastName ASC;


-- Task 17 - Swap for most expensive for cheaper gifts

CREATE TEMP VIEW Cost (maxCost) AS
    SELECT MAX(cost)
    FROM Gift;

UPDATE Gift
    SET item = "Squishmallows Squish-a-Longs - 14 Pack", 
        cost = 18.00
    WHERE cost IN
        (SELECT maxCost
             FROM Cost);


-- Task 19 - Show changes
SELECT *
    FROM Gift
    WHERE item = "Squishmallows Squish-a-Longs - 14 Pack";
