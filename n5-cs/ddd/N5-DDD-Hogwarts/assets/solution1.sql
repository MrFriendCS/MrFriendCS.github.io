/*
Title: N5 DDD Hogwarts Part 1
Author: Mr Friend
Date: 13 Jan 2025
*/

-- Task 1 - Display all house records
SELECT *
    FROM House;


-- Task 2 - Display all pupil records
SELECT *
    FROM Pupil;


-- Task 3 - Display name and colour
SELECT name, colour
    FROM House;


-- Task 4 - Display pupil names
SELECT firstName, lastName
    FROM Pupil;


-- Task 5 - Display S3 pupils
SELECT *
    FROM Pupil
    WHERE year = "S3";


-- Task 6 - Display S1 pupil names
SELECT firstName, lastName
    FROM Pupil
    WHERE year = "S1";


-- Task 7 - Display Hufflepuff record
SELECT *
    FROM House
    WHERE name = "Hufflepuff";


-- Task 8 - Full name and age, 16 or younger
SELECT firstName, lastName, age
    FROM Pupil
    WHERE age <= 16;


-- Task 9 - Full names of pupils who are 13
SELECT firstName, lastName
    FROM Pupil
    WHERE age = 13;


-- Task 10 - Name and year group of S1 / S2 pupils
SELECT firstName, lastName, year
    FROM Pupil
    WHERE year = "S1"
       OR year = "S2";
