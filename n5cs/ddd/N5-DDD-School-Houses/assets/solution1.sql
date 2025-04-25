/*
Title: N5 DDD School Houses Part 1
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
    FROM Pupil
    WHERE year = "S1"
       OR year = "S2";

-- Task 14 - Guidance teacher: Slytherin / Gryffindor
SELECT guidanceTeacher
    FROM House
    WHERE name = "Slytherin"
       OR name = "Gryffindor";


-- Task 15 - S5 / S6 pupils
SELECT firstName, lastName, age
    FROM Pupil
    WHERE year = "S5"
       OR year = "S6";


-- Task 16 - Same surname and at least 14
SELECT *
    FROM Pupil
    WHERE lastName = "Friend"
      AND age >= 14;


-- Task 17 - Pupil records sorted by surname and forename
SELECT *
    FROM Pupil
    ORDER BY lastName ASC, 
             firstName ASC;

-- Task 18 - Name and id, sorted by age and surname
SELECT firstName, lastName, id
    FROM Pupil
    ORDER BY age DESC,
             lastName ASC;


-- Task 19 - S5 / S6 names and year, sorted
SELECT firstName, lastName, year
    FROM Pupil
    WHERE year = "S5"
       OR year = "S6"
    ORDER BY year ASC,
             lastName ASC,
             firstName ASC;


-- Task 20 - Houses sorted by colour
SELECT colour, emblem, name
    FROM House
    ORDER BY colour ASC;
