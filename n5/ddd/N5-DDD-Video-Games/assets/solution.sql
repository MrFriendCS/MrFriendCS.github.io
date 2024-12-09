/*
-- Don't change lines 1 to 6
.open VideoGames.db
.headers on
.mode column
PRAGMA foreign_keys = on;
-- Don't change lines 1 to 6
*/


/*
Title: N5-DDD-Video-Games
Author: Mr Friend
Date: 28 Sep 2024
*/


-- Question 1 -- Select everything
SELECT *
    FROM Company;


-- Question 2 -- Select everything
SELECT *
    FROM Game;


-- Question 3
SELECT name, country
    FROM Company;


-- Question 4
SELECT title, genre
    FROM Game;


-- Question 5 -- Filter: Number
SELECT *
    FROM Game
    WHERE age <= 5;


-- Question 6
SELECT *
    FROM Game
    WHERE copiesSold > 18000;


-- Question 7 -- Filter: Date
SELECT *
    FROM Company
    WHERE founded > "1991-01-01";


-- Question 8 -- Filter: Complex
SELECT *
    FROM Game
    WHERE genre = "Action"
       OR genre = "Adventure";


-- Question 9 -- Filter: Complex
SELECT *
    FROM Game
    WHERE price < 20
      AND age >= 16;


-- Question 10
SELECT *
    FROM Game
    WHERE title = "Elite"
      AND genre = "Action";


-- Question 11 -- Order results: Small to Big
SELECT *
    FROM Company
    ORDER BY website ASC;


-- Question 12 -- Order results: Big to Small
SELECT *
    FROM Game
    ORDER BY copiesSold DESC;


-- Question 13 -- Order results: Multiple fields
SELECT *
    FROM Game
    ORDER BY company ASC,
             age ASC;
