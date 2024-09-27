/*
-- Don't change lines 1 to 5
.open prison.db
.headers on
.mode column
-- Don't change lines 1 to 5
*/

-- Task 1 -- Select everything -- Useful for inspecting the table
SELECT *
    FROM prisoner;


-- Task 2 -- Select specific fields
SELECT forename, surname, prison_id
    FROM prisoner;


-- Task 3 -- Select specific fields
SELECT hair, eyes, height
    FROM prisoner;


-- Task 4 -- Filter: Text (Select all fields)
SELECT *
    FROM prisoner
    WHERE hair = "Black";


-- Task 5 -- Filter: Date
SELECT prison_id, conviction, dob
    FROM prisoner
    WHERE dob >= "2000-01-01";


-- Task 6 -- Filter: Text
SELECT eyes, dob
    FROM prisoner
    WHERE conviction = "Cyberbullying";


-- Task 7 -- Filter: Complex + Boolean
SELECT *
    FROM prisoner
    WHERE conviction = "Kidnapping"
        AND open = TRUE;


-- Task 8 -- Filter: Complex
SELECT eyes, hair, prison_id
    FROM prisoner
    WHERE eyes = "Black"
        OR hair = "Black";


-- Task 9 -- Filter: Complex
SELECT eyes, hair, prison_id
    FROM prisoner
    WHERE eyes = "Black"
        AND hair = "Black";


-- Task 10 -- Filter: Complex with text and Boolean
SELECT forename, conviction, dob
    FROM prisoner
    WHERE surname = "MacNeil"
        AND open = FALSE;


-- Task 11 -- Filter: Complex
SELECT forename, surname, eyes
    FROM prisoner
    WHERE conviction = "Assault"
        AND hair = "Red";


-- Task 12 -- Filter: Complex with dates
SELECT dob, prison_id
    FROM prisoner
    WHERE dob >= "1999-01-01"
        AND dob <= "1999-12-31";


-- Task 13 -- Filter: Complex
SELECT *
    FROM prisoner
    WHERE hair = "None"
        AND eyes = "Amber";
