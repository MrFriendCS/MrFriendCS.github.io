-- Title: N5 CS 2019 Task 1 Part B - Reset
-- Author: Mr Friend
-- Date: 28 Sep 2024


/*
Not required to answer assignment questions.
Used to revert database back to start state.
*/

-- Q1b - Remove validation

-- Create new table
CREATE TABLE newVlogger(
    vloggerID INT NOT NULL UNIQUE,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    username VARCHAR(6) NOT NULL,
    expertise VARCHAR(15) NOT NULL,
    PRIMARY KEY (vloggerID)
);

-- Copy data
INSERT INTO newVlogger
    SELECT *
        FROM Vlogger;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

-- Delete old table
DROP TABLE Vlogger;

-- Rename new table
ALTER TABLE newVlogger
    RENAME TO Vlogger;

-- Referential integrity: On
PRAGMA foreign_keys = on;
