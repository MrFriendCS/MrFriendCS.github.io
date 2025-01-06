/*
Title: N5 DDD School Houses Part 3
Author: Mr Friend
Date: 6 Jan 2025
*/

-- Task 1 - All Pupil table data
SELECT *
    FROM Pupil;


-- Task 2 - Add a pupil
INSERT INTO Pupil
    VALUES (301, "Potter", "Harry", 1, "S1", 11);


-- Task 3 - Add another pupil
INSERT INTO Pupil
    VALUES (302, "Malfoy", "Daco", 1, "S1", 11);


-- Task 4 - Display new pupils
SELECT *
    FROM Pupil
    WHERE id = 301 
       OR id = 302;


-- Task 5 - All House table data
SELECT *
    FROM House;


-- Task 6 - Add new house
INSERT INTO House (id, name, emblem, colour)
    VALUES (5, "Berneray", "Sheep", "Green and Black");

-- Task 7 - Display new house
SELECT *
    FROM House
    WHERE id = 5;


-- Task 8 - Update house
UPDATE House
    SET colour = "Green and White"
    WHERE id = 5;


-- Task 9 - Display updated house
SELECT *
    FROM House
    WHERE id = 5;


-- Task 10 - Update house record
UPDATE House
    SET guidanceTeacher = "Prof Carrot", 
        emblem = "Rabbit"
    WHERE id = 2;


-- Task 11 - Display updated record
SELECT *
    FROM House
    WHERE id = 2;


-- Task 12 - Update pupil record
UPDATE Pupil
    SET age = 15
    WHERE id = 93;

SELECT *
    FROM Pupil
    WHERE id = 93;


-- Task 13 -  Update pupil record
UPDATE Pupil
    SET lastName = "Forth",
        year  = "S1"
    WHERE id = 205;

SELECT *
    FROM Pupil
    WHERE id = 205;


-- Task 14 - 



-- Task 15 - 



-- Task 16 - 



-- Task 17 - 



-- Task 18 - 


