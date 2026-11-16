-- Title: N5 CS 2023 Specimen Task 2 Part C
-- Author: Mr Friend
-- Date: 23 Nov 2023


-- Q2c

-- Player table - Before
SELECT sql
    FROM sqlite_schema
    WHERE tbl_name = "Player";


-- Create temporary table
CREATE TABLE newPlayer(
    registration INT NOT NULL
        CHECK(registration >= 100000
          AND registration <= 999999),
    clubName VARCHAR(20) NOT NULL,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    mobileNo VARCHAR(12) NOT NULL 
        CHECK(LENGTH(mobileNo) = 12),
    dateOfBirth DATE NOT NULL,
    position VARCHAR(10) NOT NULL 
        CHECK(position IN ("Striker", 
            "Midfielder", "Defender", 
            "Goalkeeper")),
    shirtNumber INT NOT NULL 
        CHECK(shirtNumber >= 1 
          AND shirtNumber <= 25),
    FOREIGN KEY (clubName)
        REFERENCES Club(clubName),
    PRIMARY KEY (registration)
);

-- Copy values
INSERT INTO newPlayer
    SELECT *
        FROM Player;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

-- Delete original table
DROP TABLE Player;

-- Rename temporary table
ALTER TABLE newPlayer
    RENAME TO Player;

-- Referential integrity: On
PRAGMA foreign_keys = on;

-- Player table - After
SELECT sql
    FROM sqlite_schema
    WHERE tbl_name = "Player";


-- Q2d(i) - Change player details
UPDATE Player
    SET clubName = "Dundee North",
        shirtNumber = 24
    WHERE registration = 814209;

SELECT * from Player 
    WHERE registration = 814209;


--Q2d(ii) - Goalkeeping coaching day
SELECT Club.clubName, forename, surname
    FROM Club, Player
    WHERE Club.clubName = Player.clubName
        AND league = 1
        AND position = "Goalkeeper";


-- Q2e - Find invalid striker shirt number
SELECT forename, surname
FROM Player
WHERE (shirtNumber < 10
    OR shirtNumber > 15)
    AND position = "Striker";


--Q2f(i) - Add player

INSERT INTO Player
    VALUES (220745,"Unknown","Erin","Smith",
            "07993 874657","1999-05-31","Striker",23);
