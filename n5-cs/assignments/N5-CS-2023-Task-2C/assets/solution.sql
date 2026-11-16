-- Title: N5 CS 2023 Task 2C
-- Author: Mr Friend
-- Date: 28 Sep 2024


-- Q2c

-- Staff Table - Before
.schema Staff

-- Create new table
CREATE TABLE newStaff(
    forename VARCHAR(30),
    surname VARCHAR(60),
    department VARCHAR(10) CHECK(department IN ("admin", "sales", "management")),
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (email)
);


-- Copy data
INSERT INTO newStaff
    SELECT *
        FROM Staff;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

-- Delete old table
DROP TABLE Staff;

-- Rename new table
ALTER TABLE newStaff
    RENAME TO Staff;

-- Referential integrity: On
PRAGMA foreign_keys = on;


-- Q2c - Staff Table - After
.schema Staff


-- Q2d(i) - Change staff details
UPDATE Staff
    SET department = "management"
    WHERE email = "eliv123@email.net";

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
