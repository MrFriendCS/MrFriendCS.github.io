-- Title: N5 CS 2018 Task 1 Part B - Reset
-- Author: Mr Friend
-- Date: 25 Nov 2023


/*
Not required to answer assignment questions.
Used to revert database back to start state.
*/

-- Q1b - Remove Job table
DROP TABLE Job;


-- Q1d - Change it back
UPDATE Staff
    SET address = "12 Leaf Avenue, Bowness, FK86 6FG"
    WHERE staffID = "DS021";
