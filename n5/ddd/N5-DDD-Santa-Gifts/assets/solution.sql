/*
Title: N5 DDD Santa Gifts
Author: Mr Friend
Date: 12 Dec 2024
*/

-- Task 1 - All Child table data
SELECT *
    FROM Child;


-- Task 2 - Nice Children
SELECT firstName, lastName
    FROM Child
    WHERE nice = TRUE;


-- Task 3 - All Gift table data
SELECT *
    FROM Gift;


-- Task 4 - Gift Table Data
SELECT *
    FROM Gift
    WHERE item = "LEGO Technic Lamborghini";


-- Task 5 - Extra Gift
INSERT INTO Gift
    VALUES(401,98,"PS5",479.00);


-- Task 6 - Show new record
SELECT *
    FROM Gift
    WHERE giftID = 401;


-- Task 7 - Naughty Child
UPDATE Child
    SET nice = FALSE
    WHERE childID = 172;


-- Task 8 - Show updated record
SELECT *
    FROM Child
    WHERE childID = 172;


-- Task 9 - Naughty Gift
UPDATE Gift
    SET item = "Lump of Coal"
    WHERE childID = 172;


-- Task 10 - Show updated records(s)
SELECT *
    FROM Gift
    WHERE childID = 172;


-- Task 11 - Specific Gift
SELECT Child.childID, firstName, lastName
    FROM Child, Gift
    WHERE Child.childID = Gift.childID
      AND item = "Chad Valley Wooden Pizza"
    ORDER BY childID DESC;


-- Task 12 - Same Surname Gifts
SELECT childID, firstName
    FROM Child
    WHERE lastName = "Friend"
    ORDER BY firstName ASC;
	

-- Task 13 - Surname and gifts
SELECT childID, firstName, item
    FROM Child, Gift
    WHERE Child.childID = Gift.childID
      AND lastName = "Friend"
    ORDER BY firstName ASC;


-- Task 14 - Change own gifts (childID will be different)
UPDATE Gifts
    SET item = "Steak and chips",
        cost = 35.00
    WHERE childID = 19;


-- Task 15 - Add Own Gift (childID will be different)
INSERT INTO Gift
    VALUES (402,19,"Bell 525 Relentless", 20000000)


-- Task 16 - Show modified and new records (childID will be different)
SELECT childID, firstName, item
    FROM Child, Gift
    WHERE Child.childID = Gift.childID
      AND Child.childID = 19
	ORDER BY cost DESC;


-- Task 16 - Delivery List - Nice children
SELECT firstName, lastName, item
    FROM Child, Gift
    WHERE Child.childID = Gift.childID
      AND nice = TRUE
    ORDER BY lastName ASC,
             firstName ASC;


-- Task 17 - On Santa's Delivery List
UPDATE Child
    SET nice = TRUE
    WHERE childID = 19;

SELECT firstName, lastName, item
    FROM Child, Gift
    WHERE Child.childID = Gift.childID
      AND nice = TRUE
      AND Child.childID = 19;


/*
Revert database to original state
*/

-- Undo Task 3 - Extra Gift
DELETE FROM Gift
    WHERE giftID = 401;

-- Undo Task 4 - Naughty Child
UPDATE Child
    SET nice = True
    WHERE childID = 172;

-- Undo Task 5 - Naughty Gift
UPDATE Gift
    SET item = "Gabby's Dollhouse Cat Friendship Cruise Ship Playset"
    WHERE childID = 172;

-- Undo Task 8 - My gifts
DELETE FROM Gift
    WHERE childID = 19;

-- Undo Task 11 - Off the Delivery List
UPDATE Child
    SET nice = FALSE
    WHERE childID = 19;
