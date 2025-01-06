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
	WHERE Pupil.house = House.id;