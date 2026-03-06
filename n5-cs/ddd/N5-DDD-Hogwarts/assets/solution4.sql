/*
Title: N5 DDD Hogwarts Part 4
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
