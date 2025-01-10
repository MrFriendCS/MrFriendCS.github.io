/*
Title: N5 DDD School Houses Part 3
Author: Mr Friend
Date: 7 Jan 2025
*/

-- Task 1 - Display all Pupil table data
SELECT *
    FROM Pupil;


-- Task 2 - Add a pupil
INSERT INTO Pupil
    VALUES (301, "Potter", "Harry", 1, "S1", 11);


-- Task 3 - Add another pupil
INSERT INTO Pupil
    VALUES (302, "Malfoy", "Daco", 4, "S1", 11);


-- Task 4 - Display new pupils
SELECT *
    FROM Pupil
    WHERE id = 301 
       OR id = 302;


-- Task 5 - Display all House table data
SELECT *
    FROM House;


-- Task 6 - Add new house
INSERT INTO House (id, name, emblem, colour)
    VALUES (5, "Berneray", "Sheep", "Green and Black");

-- Task 7 - Display new house
SELECT *
    FROM House
    WHERE id = 5;


-- Task 8 - Change house
UPDATE House
    SET colour = "Green and White"
    WHERE id = 5;


-- Task 9 - Display updated house
SELECT *
    FROM House
    WHERE id = 5;


-- Task 10 - Change house record
UPDATE House
    SET guidanceTeacher = "Prof Carrot", 
        emblem = "Rabbit"
    WHERE id = 2;


-- Task 11 - Display updated record
SELECT *
    FROM House
    WHERE id = 2;


-- Task 12 - Change pupil record
UPDATE Pupil
    SET age = 15
    WHERE id = 93;

SELECT *
    FROM Pupil
    WHERE id = 93;


-- Task 13 -  Change pupil record
UPDATE Pupil
    SET lastName = "Forth",
        year  = "S1"
    WHERE id = 205;

SELECT *
    FROM Pupil
    WHERE id = 205;


-- Task 14 - Display 'own' details
SELECT *
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
      AND firstName ="James"
      AND lastName = "Friend";


-- Task 15 - Change house
UPDATE Pupil
    SET houseID = 1
    WHERE id = 132;


-- Task 16 - Display updated record
UPDATE Pupil
    SET houseID = 1
    WHERE id = 132;


-- Task 17 - Remove Berneray house record
DELETE FROM House
    WHERE id = 5;


-- Task 18 - Remove John Bull
DELETE FROM Pupil
    WHERE id = 278;
