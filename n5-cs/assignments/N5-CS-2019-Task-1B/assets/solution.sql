-- Title: N5 CS 2019 Task 1 Part B
-- Author: Mr Friend
-- Date: 28 Sep 2024


-- Q1b

-- Vlogger Table - Before
.schema Vlogger

-- Create new table
CREATE TABLE newVlogger(
    vloggerID INT NOT NULL UNIQUE,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    username VARCHAR(6) NOT NULL
        CHECK (LENGTH(username) = 6),
    expertise VARCHAR(15) NOT NULL
        CHECK (expertise IN ("Programming", "Gaming", "Baking", "Crafts", "Makeup", "Clothes")),
    PRIMARY KEY (vloggerID)
);

-- Copy data
INSERT INTO newVlogger
    SELECT *
        FROM Vlogger;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

-- Delet old table
DROP TABLE Vlogger;

-- Rename new table
ALTER TABLE newVlogger
    RENAME TO Vlogger;

-- Referential integrity: On
PRAGMA foreign_keys = on;

-- Vlogger Table - After
.schema Vlogger
