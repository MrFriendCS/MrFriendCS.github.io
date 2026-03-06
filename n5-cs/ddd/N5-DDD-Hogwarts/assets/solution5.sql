/*
Title: N5 DDD Hogwarts Part 4
Author: Mr Friend
Date: 7 Jan 2025
*/

-- Task 12 - Change pupil record
UPDATE Pupil
    SET age = 15
    WHERE id = 93;


-- Task 13 - Display updated record
SELECT *
    FROM Pupil
    WHERE id = 93;


-- Task 14 -  Change pupil record
UPDATE Pupil
    SET lastName = "Forth",
        year  = "S1"
    WHERE id = 205;


-- Task 15 - Display updated record
SELECT *
    FROM Pupil
    WHERE id = 205;


-- Task 16 - Display 'own' details
SELECT *
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
      AND firstName ="James"
      AND lastName = "Friend";


-- Task 17 - Change house - id will be different
UPDATE Pupil
    SET houseID = 1
    WHERE id = 132;


-- Task 18 - Display updated record - id will be different
SELECT *
    FROM Pupil
    WHERE id = 132;


-- Task 19 - Remove Berneray house record
DELETE FROM House
    WHERE id = 5;

-- or

DELETE FROM House
    WHERE name = "Berneray";


-- Task 20 - Find John Bull
SELECT *
    FROM Pupil
    WHERE firstName ="John"
      AND lastName = "Bull";


-- Task 21 - Remove Bull
DELETE FROM Pupil
    WHERE id = 278;
