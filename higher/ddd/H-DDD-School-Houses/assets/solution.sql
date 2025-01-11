/*
Title: H DDD School Houses
Author: Mr Friend
Date: 22 Dec 2024
*/

-- Task 1 - Number of pupils
SELECT COUNT(*) AS Pupils
    FROM Pupil;


-- Task 2 - Number of results
SELECT COUNT(*) AS Results
    FROM Result;


-- Task 3 - No Award
SELECT guidanceTeacher, firstName, lastName, year, grade
    FROM House, Pupil, Result
    WHERE House.id = Pupil.houseID
      AND Pupil.id = Result.pupilID
      AND grade = "No Award";


-- Task 4 - Subject: Studies
SELECT *
    FROM Subject
    WHERE name LIKE "%Studies";


-- Task 5 - Subject: the
SELECT *
    FROM Subject
    WHERE name LIKE "% the %";


-- Task 6 - Number of grades
SELECT grade, COUNT(*) AS Count
    FROM Result
    GROUP BY grade;


-- Task 7 - Pupils Most A grades
SELECT name, COUNT(*) AS [S4/S5 Pupils]
    FROM House, Pupil
    WHERE House.id = Pupil.houseID
      AND (year = "S4"
       OR year = "S5")
    GROUP BY  name
    ORDER BY [S4/S5 Pupils] DESC;


-- Task 8 - Pupils Most A grades

CREATE TEMP VIEW GradeA (pupilID, noOfAs) AS
    SELECT pupilID, COUNT(*) AS noOfAs
    FROM Result
    WHERE grade = "A"
    GROUP BY pupilID;

CREATE TEMP VIEW MaxAs (mostAs) AS
    SELECT MAX(noOfAs) AS mostAs
    FROM GradeA;

SELECT firstName, lastName, noOfAs
    FROM Pupil, GradeA, MaxAs
    WHERE Pupil.id = GradeA.pupilID
      AND GradeA.noOfAs = MaxAs.mostAs
    ORDER BY firstName ASC, 
             lastName ASC;


-- Task 9 - House with most No Awards

CREATE TEMP VIEW NoAward (houseID, noOfNAs) AS
    SELECT houseID, COUNT(*) AS noOfNAs
    FROM Pupil, Result
    WHERE pupil.id = Result.pupilID
      AND grade = "No Award"
    GROUP BY houseID;

CREATE TEMP VIEW MaxNAs (mostNAs) AS
    SELECT MAX(noOfNAs) AS mostNAs
    FROM NoAward;

SELECT name, guidanceTeacher, noOfNAs
    FROM House, NoAward, MaxNAs
    WHERE House.id = NoAward.houseID
      AND NoAward.noOfNAs = MaxNAs.mostNAs;


-- Extra

-- Task ? - Number of grades
SELECT guidanceTeacher, firstName, lastName, year, Subject.name
    FROM House, Pupil, Result, Subject
    WHERE House.id = Pupil.houseID 
      AND Pupil.id = Result.pupilID 
      AND Result.subjectID = Subject.id 
      AND grade = "A"
    ORDER BY guidanceTeacher ASC, 
             year DESC, 
             firstName ASC, 
             lastName ASC


-- Task ? - S4 and S5 pupils in each house
CREATE TEMP VIEW S4(houseID, amount) AS
    SELECT houseID, COUNT(*)
    FROM Pupil
    WHERE year = "S4"
    GROUP BY houseID;

CREATE TEMP VIEW S5(houseID, amount) AS
    SELECT houseID, COUNT(*)
    FROM Pupil
    WHERE year = "S5"
    GROUP BY houseID;
	
SELECT name, S4.amount AS S4, S5.amount AS S5
    FROM House, S4, S5
    WHERE House.id = S4.houseID
      AND House.id = S5.houseID;
