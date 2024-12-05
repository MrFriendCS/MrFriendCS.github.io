/* -- Don't touch lines 1 to 6
.open santa.db
.headers ON
.mode column
PRAGMA foreign_keys = on;
-- Don't touch lines 1 to 6 */

-- Title: N5 DDD Santa Gifts
-- Author: Mr Friend
-- Date: 9 Dec 2023

-- Task 1 - Nice Children

SELECT first_name, last_name
    FROM child
    WHERE nice = TRUE;


-- Task 2 - Gift Table Data
-- Get a 'feel' for the data
SELECT *
    FROM gift
    WHERE item = "LEGO Technic Lamborghini";


-- Task 3 - Extra Gift

INSERT INTO gift
    VALUES(401,98,"PS5");


-- Task 4 - Naughty Child

UPDATE child
    SET nice = FALSE
    WHERE child_id = 172;


-- Task 5 - Naughty Gift

UPDATE gift
    SET item = "Lump of Coal"
    WHERE child_id = 172;


-- Task 6 - Specific Gift

SELECT child.child_id, first_name, last_name
    FROM child, gift
    WHERE child.child_id = gift.child_id
        AND item = "Chad Valley Wooden Pizza";


-- Task 7 - Same Surname Gifts

SELECT first_name, item
    FROM child, gift
    WHERE child.child_id = gift.child_id
        AND last_name = "Friend"
    ORDER BY first_name ASC;


-- Task 8 - My Santa Gift

SELECT first_name, item
    FROM child, gift
    WHERE child.child_id = gift.child_id
        AND child_id = 19;


-- Task 9 - Add My Gifts

-- Add gifts
INSERT INTO gift
    VALUES (402,19,"Bell 525 Relentless"),
           (403,19,"Continental GTC Mulliner W12");


-- Task 10 - Delivery List - Nice children

SELECT first_name, last_name, item
    FROM child, gift
    WHERE child.child_id = gift.child_id
        AND nice = TRUE
    ORDER BY last_name ASC,
        first_name ASC;


-- "Task 11 - On Santa's Delivery List"

UPDATE child
    SET nice = TRUE
    WHERE child_id = 19;

SELECT first_name, last_name, item
FROM child, gift
WHERE child.child_id = gift.child_id
    AND nice = TRUE
    AND child.child_id = 19;


/*
Revert database to original state
*/

-- Undo Task 3 - Extra Gift
DELETE FROM gift
    WHERE gift_id = 401;

-- Undo Task 4 - Naughty Child
UPDATE child
    SET nice = True
    WHERE child_id = 172;

-- Undo Task 5 - Naughty Gift
UPDATE gift
    SET item = "Gabby's Dollhouse Cat Friendship Cruise Ship Playset"
    WHERE child_id = 172;

-- Undo Task 8 - My gifts
DELETE FROM gift
    WHERE child_id = 19;

-- Undo Task 11 - Off the Delivery List
UPDATE child
    SET nice = FALSE
    WHERE child_id = 19;
