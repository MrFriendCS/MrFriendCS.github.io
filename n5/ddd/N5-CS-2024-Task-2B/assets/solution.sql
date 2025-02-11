-- Title: 2024 Task 2 Part B
-- Author: Mr Friend
-- Date: 11 Feb 2025


-- 2(c)(i)
INSERT INTO Fossil
    VALUES (2061, "USA", 2023, "Garath", "DINO_68");


-- 2(c)(ii)
SELECT dinoName
    FROM Dinosaur, Fossil
    WHERE Dinosaur.dinoID = Fossil.dinoID
      AND year > 1980
      AND countryFound = "USA"
    ORDER BY year ASC;


-- 2(c)(iii)
UPDATE Dinosaur
    SET length = 8.0,
        diet = "Herbivorous"
    WHERE dinoName = "Aardonyx";


-- 2(d)
SELECT dinoName, countryFound, diet  -- country field doesn't exist
    FROM Dinosaur, Fossil
    WHERE Dinosaur.dinoID = Fossil.dinoID  -- equi-join missing
      AND year = 1930  -- only shows 1930 no 1930s
      AND length > 10;
