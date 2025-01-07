/*
Title: N5 DDD School Houses Part 1
Author: Mr Friend
Date: 7 Jan 2025
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


-- Task 8 - Display full name and house of S5 pupils
SELECT firstName, lastName, name
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND year = "S5";


-- Task 9 - Full name and house younger than 13
SELECT firstName, lastName, name
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND age < 13;


-- Task 10 - Full name and age, 16 or younger
SELECT firstName, lastName, age
    FROM Pupil
    WHERE age <= 16;


-- Task 11 - Full names of pupils who are 13
SELECT firstName, lastName
    FROM Pupil
    WHERE age = 13;


-- Task 12 - Forename and house of pupils who are 14
SELECT firstName, name
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND age = 14;


-- Task 13 - Name and year group of S1 / S2 pupils
SELECT firstName, lastName, year
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND (year = "S1"
        OR year = "S2");

-- Task 14 - 


-- Task 15 - 


-- Task 16 - 


-- Task 17 - 


-- Task 18 - 


-- Task 19 - 


-- Task 20 - 

