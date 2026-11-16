-- Title: N5 CS 2023 Specimen Task 2 Part C - Reset
-- Author: Mr Friend
-- Date: 23 Nov 2023


/*
Not required to answer assignment questions.
Used to revert database back to start state.
*/

-- Q2c - Remove validation

-- Temporary table
CREATE TABLE newPlayer(
    registration INT NOT NULL
        CHECK (registration >= 100000 
             AND registration <= 999999),
    clubName VARCHAR(20) NOT NULL,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    mobileNo VARCHAR(12) NOT NULL 
        CHECK (LENGTH(mobileNo) = 12),
    dateOfBirth DATE NOT NULL,
    position VARCHAR(10) NOT NULL 
        CHECK (position IN ("Striker", "Midfielder",
                            "Defender", "Goalkeeper")),
    shirtNumber INT NOT NULL,
    FOREIGN KEY (clubName) 
        REFERENCES Club(clubName),
    PRIMARY KEY (registration)
);

-- Copy data
INSERT INTO newPlayer
    SELECT *
        FROM Player;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

-- Drop old table
DROP TABLE Player;

-- Rename temporary table
ALTER TABLE newPlayer
    RENAME TO Player;

-- Referential integrity: On
PRAGMA foreign_keys = on;


-- Q2d(i) - Move player back
UPDATE Player
    SET clubName = "Aviemore Aces",
        shirtNumber = 8
    WHERE registration = 814209;
