-- Don't change lines 1 to 6
.open video_games.db
.headers on
.mode column
PRAGMA foreign_keys = on;
-- Don't change lines 1 to 6

.print Question 1
-- Select everything
-- Useful for inspecting the table
SELECT *
    FROM company;


.print
.print Question 2

-- Select everything
-- Useful for inspecting the table
SELECT *
    FROM game;


.print
.print Question 3
SELECT company_name, country
    FROM company;


.print
.print Question 4
SELECT title, genre
    FROM game;


.print
.print Question 5
-- Filter: Number
SELECT *
    FROM game
    WHERE age <= 5;


.print
.print Question 6
SELECT *
    FROM game
    WHERE copies_sold > 18000;


.print
.print Question 7
-- Filter: Number
SELECT *
    FROM company
    WHERE founded > "1991-01-01";


.print
.print Question 8
-- Filter: Complex
SELECT *
    FROM game
    WHERE genre = "Action"
        OR genre = "Adventure";


.print
.print Question 9
-- Filter: Complex
SELECT *
    FROM game
    WHERE price < 20
        AND age >= 16;


.print
.print Question 10
SELECT *
    FROM game
    WHERE company_name = "Elite"
        AND genre = "Action";


.print
.print Question 11
-- Order results: Small to Big
SELECT *
    FROM company
    ORDER BY website ASC;


.print
.print Question 12
-- Order results: Big to Small
SELECT *
    FROM game
    ORDER BY copies_sold DESC;


.print
.print Question 13
-- Order results: Multiple fields
SELECT *
    FROM game
    ORDER BY company_name ASC,
         age ASC;
