-- Title: N5 CS 2023 Task 2C - Reset
-- Author: Mr Friend
-- Date: 28 Sep 2024


/*
Not required to answer assignment questions.
Used to revert database back to start state.
*/

-- Q2c - Remove validation
CREATE TABLE newStaff(
    forename VARCHAR(30),
    surname VARCHAR(60),
    department VARCHAR(10),
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


-- Q2d - Change staff details
UPDATE Staff
    SET department = "sales"
    WHERE email = "eliv123@email.net";


-- Q2e - Delete problem ID 106
INSERT INTO Problem
    VALUES (106,"fbr530@email.net","2022-07-07","I can't access the Internet.",1,0);
