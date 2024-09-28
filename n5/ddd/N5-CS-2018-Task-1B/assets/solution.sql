/*
.open Gardening.db
.headers on
.mode column
PRAGMA foreign_keys = on;
/*


/*
Title: N5 CS 2018 Task 1 Part B
Author: Mr Friend
Date: 25 Nov 2023
*/


-- Q1c - Create Job table
CREATE TABLE Job(
    jobID INT NOT NULL,
    jobDate DATE NOT NULL,
    jobTime TIME NOT NULL 
        CHECK(jobTime >= "09:00" 
          AND jobTime <= "18:00"),
    custName VARCHAR(40) NOT NULL,
    custAddress VARCHAR(50) NOT NULL,
    custPostcode VARCHAR(8) NOT NULL,
    phoneNo VARCHAR(11),
    task VARCHAR(12) NOT NULL 
        CHECK(task IN("Lawn Mowed", "Hedge Cut", "Weeds Pulled")),
    staffID VARCHAR(5) NOT NULL,
    FOREIGN KEY (staffID) 
        REFERENCES Staff(staffID),
    PRIMARY KEY (jobID)
);


-- Q1c - Job table evidence
SELECT sql
    FROM sqlite_schema
    WHERE tbl_name = "Job";


-- Q1d - Change address
UPDATE Staff
    SET address = "99 Willow Way, Falkirk, FA87 6FE"
    WHERE staffID = "DS021";


-- Q1d - Evidence
SELECT *
    FROM Staff
    WHERE staffID = "DS021";




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
