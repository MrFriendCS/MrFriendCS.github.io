-- Don't change lines 1 to 6
.open maintenance.db
.headers on
.mode column
PRAGMA foreign_keys = on;
-- Don't touch lines 1 to 6

/*
Title: N5 CS 2023 Task 2C
Author: Mr Friend
Date: 25 Nov 2023
*/

.print
.print Q2c - Staff Table - Before
    
.schema Staff

CREATE TABLE newStaff(
    forename VARCHAR(30),
    surname VARCHAR(60),
    department VARCHAR(10) CHECK(department IN ("admin", "sales", "management")),
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (email)
);

INSERT INTO newStaff
    SELECT *
        FROM Staff;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

DROP TABLE Staff;

ALTER TABLE newStaff
    RENAME TO Staff;

-- Referential integrity: On
PRAGMA foreign_keys = on;

.print
.print Q2c - Staff Table - After
.schema Staff


.print
.print Q2d(i) - Change staff details

UPDATE Staff
    SET department = "management"
    WHERE email = "eliv123@email.net";

SELECT *
    FROM Staff
    WHERE email = "eliv123@email.net";


.print
.print Q2d(ii) - 7th July 2022 Problems

SELECT forename, surname, description
    FROM Staff, Problem
    WHERE Staff.email = Problem.email
        AND dateRaised = "2022-07-07"
        AND completed = FALSE
    ORDER BY rating ASC;

.print
.print Q2e(i) - Explain delete problem ID 106
-- Could be more than one record deleted

SELECT *
    FROM Problem
    WHERE rating = 1
        AND email = "fbr530@email.net";


.print
.print Q2e(ii) - Improve delete problem ID 106
-- Use primary key

DELETE FROM Problem
    WHERE problemID = 106;


.print


    

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

INSERT INTO newStaff
    SELECT *
        FROM Staff;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

DROP TABLE Staff;

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
