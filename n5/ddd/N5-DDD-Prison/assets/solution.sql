/*
-- Don't change lines 1 to 5
.open prison.db
.headers on
.mode column
-- Don't change lines 1 to 5
*/

-- Task 1 -- Select everything -- Useful for inspecting the table
SELECT *
    FROM Prisoner;


-- Task 2 -- Select specific fields
SELECT forename, surname, prisonID
    FROM Prisoner;


-- Task 3 -- Select specific fields
SELECT hair, eyes, height
    FROM Prisoner;


-- Task 4 -- Filter: Text (Select all fields)
SELECT *
    FROM Prisoner
    WHERE hair = "Black";


-- Task 5 -- Filter: Date
SELECT prisonID, conviction, dob
    FROM Prisoner
    WHERE dob >= "2000-01-01";


-- Task 6 -- Filter: Text
SELECT eyes, dob
    FROM Prisoner
    WHERE conviction = "Cyberbullying";


-- Task 7 -- Filter: Complex + Boolean
SELECT *
    FROM Prisoner
    WHERE conviction = "Kidnapping"
      AND open = TRUE;


-- Task 8 -- Filter: Complex
SELECT eyes, hair, prisonID
    FROM Prisoner
    WHERE eyes = "Black"
       OR hair = "Black";


-- Task 9 -- Filter: Complex
SELECT eyes, hair, prisonID
    FROM Prisoner
    WHERE eyes = "Black"
      AND hair = "Black";


-- Task 10 -- Filter: Complex with text and Boolean
SELECT forename, conviction, dob
    FROM Prisoner
    WHERE surname = "MacNeil"
      AND open = FALSE;


-- Task 11 -- Filter: Complex
SELECT forename, surname, eyes
    FROM Prisoner
    WHERE conviction = "Assault"
      AND hair = "Red";


-- Task 12 -- Filter: Complex with dates
SELECT dob, prisonID
    FROM Prisoner
    WHERE dob >= "1999-01-01"
      AND dob <= "1999-12-31";


-- Task 13 -- Filter: Complex
SELECT *
    FROM Prisoner
    WHERE hair = "None"
      AND eyes = "Amber";
