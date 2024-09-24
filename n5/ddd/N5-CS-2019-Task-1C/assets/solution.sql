-- Don't touch lines 1 to 6
.open Vlogger.db
.headers on
.mode column
PRAGMA foreign_keys = on;
-- Don't touch lines 1 to 6


/*
Title: N5 CS 2019 Task 1 Part B & C
Author: Mr Friend
Date: 25 Nov 2023
*/

.print
.print N5 CS 2019 Task 1 Part B

.print
.print Q1b - Vlogger Table - Before

.schema Vlogger

CREATE TABLE newVlogger(
    vloggerID INT NOT NULL UNIQUE,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    username VARCHAR(6) NOT NULL CHECK(LENGTH(username) = 6),
    expertise VARCHAR(15) NOT NULL CHECK(expertise IN ("Programming", "Gaming", "Baking", "Crafts", "Makeup", "Clothes")),
    PRIMARY KEY (vloggerID)
);

INSERT INTO newVlogger
    SELECT *
        FROM Vlogger;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

DROP TABLE Vlogger;

ALTER TABLE newVlogger
    RENAME TO Vlogger;

-- Referential integrity: On
PRAGMA foreign_keys = on;

.print
.print Q1b - Vlogger Table - After

.schema Vlogger

.print
.print N5 CS 2019 Task 1 Part C

.print
.print Q1c(i) - Advertise best videos
SELECT username, videoName
    FROM Vlogger, Video
    WHERE Vlogger.vloggerID = Video.vloggerID
        AND rating > 3;


.print
.print Q1c(ii) - Delete 'Slime' video
DELETE FROM Video
    WHERE videoID = 3;

.print
.print Q1c(ii) - Evidence
SELECT *
    FROM Video;


.print


    

/*
Not required to answer assignment questions.
Used to revert database back to start state.
*/

-- Q1b - Remove validation

CREATE TABLE newVlogger(
    vloggerID INT NOT NULL UNIQUE,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    username VARCHAR(6) NOT NULL,
    expertise VARCHAR(15) NOT NULL,
    PRIMARY KEY (vloggerID)
);

INSERT INTO newVlogger
    SELECT *
        FROM Vlogger;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

DROP TABLE Vlogger;

ALTER TABLE newVlogger
    RENAME TO Vlogger;

-- Referential integrity: On
PRAGMA foreign_keys = on;

-- Q1c(ii) - Add 'Slime' movie
INSERT INTO Video
    VALUES (3,10,"Slime",45,"2020-05-15","Make slime",1);
