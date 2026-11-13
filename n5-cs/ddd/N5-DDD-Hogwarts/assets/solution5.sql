/*
Title: N5 DDD Hogwarts Part 5
Author: Mr Friend
Date: 7 Jan 2025
*/

-- Task 1 - Change pupil record
UPDATE Pupil
    SET age = 15
    WHERE id = 93;


-- Task 2 - Display updated record
SELECT *
    FROM Pupil
    WHERE id = 93;


-- Task 3 -  Change pupil record
UPDATE Pupil
    SET lastName = "Forth",
        year  = "S1"
    WHERE id = 205;


-- Task 4 - Display updated record
SELECT *
    FROM Pupil
    WHERE id = 205;


-- Task 5 - Display 'own' details
SELECT *
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
      AND firstName ="John"
      AND lastName = "Smith";


-- Task 6 - Change house - id will be different
UPDATE Pupil
    SET houseID = 1
    WHERE id = 132;


-- Task 7 - Display updated record - id will be different
SELECT *
    FROM Pupil
    WHERE id = 132;


-- Task 8 - Remove Berneray house record
DELETE FROM House
    WHERE id = 5;

-- or

DELETE FROM House
    WHERE name = "Berneray";


-- Task 9 - Find John Bull
SELECT *
    FROM Pupil
    WHERE firstName ="John"
      AND lastName = "Bull";


-- Task 10 - Remove Bull
DELETE FROM Pupil
    WHERE id = 278;
