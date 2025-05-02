-- Title: N5 CS 2023 Task 2C
-- Author: Mr Friend
-- Date: 28 Sep 2024


-- Q2d(i) - Change staff details
UPDATE Staff
    SET department = "management"
    WHERE email = "eliv123@email.net";

-- Evidence
SELECT *
    FROM Staff
    WHERE email = "eliv123@email.net";


-- Q2d(ii) - 7th July 2022 Problems
SELECT forename, surname, description
    FROM Staff, Problem
    WHERE Staff.email = Problem.email
      AND dateRaised = "2022-07-07"
      AND completed = FALSE
    ORDER BY rating ASC;


-- Q2e(i) - Explain delete problem ID 106
-- Could be more than one record deleted
SELECT *
    FROM Problem
    WHERE rating = 1
      AND email = "fbr530@email.net";


-- Q2e(ii) - Improve delete problem ID 106
-- Use primary key
DELETE FROM Problem
    WHERE problemID = 106;
