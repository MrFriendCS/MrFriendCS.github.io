/*
Title: N5 DDD School Houses Part 2
Author: Mr Friend
Date: 6 Jan 2025
*/

-- Task 1 - All Pupil table data
SELECT *
    FROM Pupil;


-- Task 2 - All House table data
SELECT *
    FROM House;


-- Task 3 - All Pupil and House table data
SELECT *
    FROM Pupil, House
    WHERE Pupil.houseID = House.id;


-- Task 4 - forename, age, and house of all pupils
SELECT firstName, age, name
    FROM Pupil, House
    WHERE Pupil.houseID = House.id;


-- Task 5 - 
SELECT firstName, lastName, guidanceTeacher
    FROM Pupil, House
    WHERE Pupil.houseID = House.id;


-- Task 6 - 
SELECT firstName, lastName, year
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
      AND name = "Slytherin";


-- Task 7 - 
SELECT *
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
      AND firstName = "James"
      AND lastName = "Friend";


-- Task 8 - 
SELECT *
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
      AND lastName = "Friend"
      AND emblem = "Eagle";


-- Task 9 - 
SELECT firstName, lastName, year
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
      AND name = "Hufflepuff"
    ORDER BY lastName ASC;


-- Task 10 - 
SELECT firstName, lastName, year, guidanceTeacher
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
    ORDER BY year DESC,
             lastName ASC;


-- Task 11 - 
SELECT emblem, colour, firstName, year
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
    ORDER BY emblem ASC,
             year ASC;


-- Task 12 - 
SELECT firstName, lastName, age, guidanceTeacher
    FROM Pupil, House
    WHERE Pupil.houseID = House.id
      AND year = "S3"
    ORDER BY age DESC,
             lastName ASC,
             year ASC;
