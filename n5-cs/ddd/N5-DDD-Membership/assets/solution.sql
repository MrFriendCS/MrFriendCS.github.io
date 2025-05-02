/*
-- Don't change lines 1 to 5
.open membership.db
.headers on
.mode column
-- Don't change lines 1 to 5
*/


/*
Title: N5-DDD-Membership
Author: Mr Friend
Date: 28 Sep 2024
*/


-- Task 1
SELECT clubID, clubName
    FROM Club;


-- Task 2
SELECT firstName, LastName, gender
    FROM Member
    WHERE type = "Adult";


-- Task 3
SELECT firstName, LastName, gender
    FROM Member
    WHERE type = "Adult"
    ORDER BY LastName ASC;


-- Task 4
SELECT *
    FROM Club
    WHERE trainer = TRUE
    ORDER BY rooms DESC;


-- Task 5 -- Order by two fields
SELECT town, dob, firstName, LastName
    FROM Member
    ORDER BY town ASC,
             dob DESC;


-- Task 6 -- Filter: AND
SELECT LastName, address, postcode
    FROM Member
    WHERE gender = "M"
      AND renewal = 5;


-- Task 7 -- Equi-join
SELECT firstName, LastName, Club.type
    FROM Club, Member
    WHERE Club.clubID = Member.clubID;


-- Task 8 -- Equi-join and filter
SELECT firstName, LastName, memberNo
    FROM Club, Member
    WHERE Club.clubID = Member.clubID
      AND clubName = "Puddles"
    ORDER BY firstName ASC,
             LastName ASC;


-- Task 9 (Will return an error when run again) -- Not much to see
INSERT INTO Club
    Values ("SP488", "Vital Spark", "Brockton", "Gym", "2017-03-03", FALSE, 2);


-- Task 10 -- Check new Member has been added
SELECT *
    FROM Club
    WHERE clubID = "SP488";


-- Task 11
UPDATE Member
    SET renewal = 11
    WHERE renewal = 12;


-- Task 12
SELECT memberNo, firstName, LastName
    FROM Member
    WHERE renewal = 11;


-- Task 13 - Delete -- Not much to see
DELETE FROM Member
    WHERE type = "Guest";


-- Task 14 -- Check that 'Guest' members all removed 
SELECT firstName, LastName, type
    FROM Member
    ORDER BY type ASC;


/*
Return db to start state.
*/

UPDATE Member
    SET renewal = 12
    WHERE renewal = 11;

DELETE FROM Club
    WHERE clubID = "SP488";

INSERT INTO Member
    VALUES ("AVC243", "SP487", "Wallace", "Blevins", "13 Euismod Avenue", "Lowhall", "C76 6FO", "1955-12-02", 8 , "M", "Guest");
	