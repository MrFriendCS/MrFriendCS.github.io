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
    FROM company;


-- Question 2 -- Select everything
SELECT *
    FROM game;


-- Question 3
SELECT company_name, country
    FROM company;


-- Question 4
SELECT title, genre
    FROM game;


-- Question 5 -- Filter: Number
SELECT *
    FROM game
    WHERE age <= 5;


-- Question 6
SELECT *
    FROM game
    WHERE copies_sold > 18000;


-- Question 7 -- Filter: Number
SELECT *
    FROM company
    WHERE founded > "1991-01-01";


-- Question 8 -- Filter: Complex
SELECT *
    FROM game
    WHERE genre = "Action"
       OR genre = "Adventure";


-- Question 9 -- Filter: Complex
SELECT *
    FROM game
    WHERE price < 20
      AND age >= 16;


-- Question 10
SELECT *
    FROM game
    WHERE company_name = "Elite"
      AND genre = "Action";


-- Question 11 -- Order results: Small to Big
SELECT *
    FROM company
    ORDER BY website ASC;


-- Question 12 -- Order results: Big to Small
SELECT *
    FROM game
    ORDER BY copies_sold DESC;


-- Question 13 -- Order results: Multiple fields
SELECT *
    FROM game
    ORDER BY company_name ASC,
             age ASC;
