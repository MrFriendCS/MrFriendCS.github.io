/*
Title: N5 DDD Hogwarts Part 2
Author: Mr Friend
Date: 13 Jan 2025
*/


-- Task 1 - Guidance teacher: Slytherin / Gryffindor
SELECT guidanceTeacher
    FROM House
    WHERE name = "Slytherin"
       OR name = "Gryffindor";


-- Task 2 - S5 / S6 pupils
SELECT firstName, lastName, age
    FROM Pupil
    WHERE year = "S5"
       OR year = "S6";


-- Task 3 - Same surname and at least 14
SELECT *
    FROM Pupil
    WHERE lastName = "Friend"
      AND age >= 14;


-- Task 4 - Pupil records sorted by surname and forename
SELECT *
    FROM Pupil
    ORDER BY lastName ASC, 
             firstName ASC;


-- Task 5 - Name and id, sorted by age and surname
SELECT firstName, lastName, id
    FROM Pupil
    ORDER BY age DESC,
             lastName ASC;


-- Task 6 - S5 / S6 names and year, sorted
SELECT firstName, lastName, year
    FROM Pupil
    WHERE year = "S5"
       OR year = "S6"
    ORDER BY year ASC,
             lastName ASC,
             firstName ASC;


-- Task 7 - Houses sorted by colour
SELECT colour, emblem, name
    FROM House
    ORDER BY colour ASC;


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


-- Task 10 - Forename and house of pupils who are 14
SELECT firstName, name
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND age = 14;
