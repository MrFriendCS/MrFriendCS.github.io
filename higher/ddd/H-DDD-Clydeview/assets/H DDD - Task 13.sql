-- H DDD - Task 13

-- Q1
SELECT Firstname, Surname, monthOfRenewal
    FROM Member
    WHERE Surname LIKE "D%";


-- Q2
SELECT membershipNumber, Surname, address, Town, postcode
    FROM Member
    WHERE Surname LIKE "%oo%"
    ORDER BY Surname ASC;


-- Q3
SELECT Firstname, Town
    FROM Member
    WHERE Firstname LIKE "%o%"
      AND Town LIKE "B%n";


-- Q4
SELECT Firstname, Surname
    FROM Member
    WHERE Surname LIKE "L___";


-- Q5
SELECT membershipNumber, Town, postcode
    FROM Member
    WHERE postcode LIKE "%a_2%";


