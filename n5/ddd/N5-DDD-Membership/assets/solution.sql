-- Don't change lines 1 to 5
.open membership.db
.headers on
.mode column
-- Don't change lines 1 to 5

.print
.print Return database to start state

UPDATE member
    SET renewal = 12
    WHERE renewal = 11;

DELETE FROM club
    WHERE club_id = "SP488";

INSERT INTO member
    VALUES ("AVC243", "SP487", "Wallace", "Blevins", "13 Euismod Avenue", "Lowhall", "C76 6FO", "1955-12-02", 8 , "M", "Guest");

.print

.print Task 1
SELECT club_id, club_name
    FROM club;


.print
.print Task 2
SELECT first_name, surname, gender
    FROM member
    WHERE member_type = "Adult";


.print
.print Task 3
SELECT first_name, surname, gender
    FROM member
    WHERE member_type = "Adult"
    ORDER BY surname;


.print
.print Task 4
SELECT *
    FROM club
    WHERE trainer = TRUE
    ORDER BY rooms DESC;


.print
.print Task 5
-- Order by two fields
SELECT town, dob, first_name, surname
    FROM member
    ORDER BY town ASC,
        dob DESC;


.print
.print Task 6
-- Filter: AND
SELECT surname, address, postcode
    FROM member
    WHERE gender = "M"
        AND renewal = 5;


.print
.print Task 7
-- Equi-join
SELECT first_name, surname, club_type
    FROM club, member
    WHERE club.club_id = member.club_id;


.print
.print Task 8
-- Equi-join and filter
SELECT first_name, surname, member_no
    FROM club, member
    WHERE club.club_id = member.club_id
        AND club_name = "Puddles"
    ORDER BY first_name ASC,
        surname ASC;


.print
.print Task 9 (Will return an error when run again)
-- No output, unless it fails
INSERT INTO club
    Values ("SP488", "Vital Spark", "Brockton", "Gym", "2017-03-03", FALSE, 2);

.print
.print Task 10
-- Check new member has been added
SELECT *
    FROM club
    WHERE club_id = "SP488";


.print
.print Task 11
UPDATE member
    SET renewal = 11
    WHERE renewal = 12;


.print
.print Task 12
SELECT member_no, first_name, surname
    FROM member
    WHERE renewal = 11;


.print
.print Task 13 - Delete
-- No output, unless it fails
DELETE FROM member
    WHERE member_type = "Guest";


.print
.print Task 14
-- Check that 'Guest' members all removed 
SELECT first_name, surname, member_type
    FROM member
    ORDER BY member_type;
