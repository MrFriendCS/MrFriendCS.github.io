/*
Check that only one of each 'naughty' pupil exists.
*/

CREATE TEMP VIEW Naughty (forename, surname) AS
    SELECT firstName, lastName
    FROM Child
	WHERE nice = FALSE
	ORDER BY firstName, LastName;
	
SELECT firstName, lastName, COUNT(*)
    FROM Child, Naughty
	WHERE firstName = forename 
	  AND lastName = surname
	GROUP BY firstName, lastName
	ORDER BY COUNT(*) DESC;
