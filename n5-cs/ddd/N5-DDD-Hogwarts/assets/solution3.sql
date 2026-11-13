/*
Title: N5 DDD Hogwarts Part 3
Author: Mr Friend
Date: 6 Jan 2025
*/

-- Task 1 - All Pupil table data
SELECT *
    FROM Pupil;


-- Task 2 - All House table data
SELECT *
    FROM House;


-- Task 3 - forename, age, and house name
SELECT firstName, age, name
    FROM House, Pupil
    WHERE House.id = Pupil.houseID;


-- Task 4 - 
SELECT firstName, lastName, guidanceTeacher
    FROM House, Pupil
    WHERE House.id = Pupil.houseID;


-- Task 5 - 
SELECT firstName, lastName, year
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND name = "Slytherin"
    ORDER BY year DESC;

-- or

SELECT firstName, lastName, year
    FROM Pupil
    WHERE houseID = 4
    ORDER BY year DESC;


-- Task 6 - 
SELECT *
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND firstName = "John"
      AND lastName = "Smith";


-- Task 7 - 
SELECT *
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND lastName = "Smith"
      AND emblem = "Eagle";


-- Task 8 - 
SELECT firstName, lastName, year
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND name = "Hufflepuff"
    ORDER BY lastName ASC;

-- or

SELECT firstName, lastName, year
    FROM Pupil 
    WHERE houseID = 2
    ORDER BY lastName ASC;


-- Task 9 - 
SELECT firstName, lastName, year, guidanceTeacher
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
    ORDER BY year DESC,
             firstName ASC
             lastName ASC;


-- Task 10 - 
SELECT emblem, colour, firstName, year
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
    ORDER BY emblem ASC,
             year ASC;


-- Task 11 - 
SELECT firstName, lastName, age, guidanceTeacher
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND year = "S3"
    ORDER BY age DESC,
             lastName ASC,
             firstName ASC;
