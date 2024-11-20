-- H DDD - Task 13

-- Q1
SELECT Firstname, Surname, postcode, monthOfRenewal
    FROM Member
    WHERE Surname LIKE "D%";


-- Q2
SELECT membershipNumber, Surname, Address, Town, Postcode
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
SELECT membershipNumber, Town, Postcode
    FROM Member
    WHERE Postcode LIKE "%a_2%";


-- Q6
SELECT Firstname, Surname, typeOfMembership
    FROM Member
    WHERE Surname LIKE "%i__e%";


-- Q7
SELECT membershipNumber, dateOfBirth, typeOfMembership
    FROM Member
    WHERE typeOfMembership = "Adult" 
      AND dateOfBirth LIKE "%-10-%";


-- Q8
SELECT plantName, Variety
    FROM Plant
    WHERE Variety LIKE "%x%"
    ORDER BY plantName;


-- Q9
SELECT Category, plantName, code, price
    FROM Plant
    WHERE code LIKE "__";


-- Q10
SELECT plantName, code, Height
    FROM Plant
    WHERE code LIKE "%P%"
      AND plantName LIKE "%a_t%";


-- Q11
SELECT plantName, referenceID, price
    FROM Plant
    WHERE plantName LIKE "%a%a"
	ORDER BY price DESC, referenceID ASC;


-- Q12
SELECT code, referenceID, Category
    FROM Plant
    WHERE referenceID LIKE "_3_" 
      AND code LIKE "%r%"
	ORDER BY Category ASC;


-- Q13
SELECT plantName, Unit, Price
    FROM Plant
    WHERE plantName LIKE "%a__n%"
    ORDER BY Unit DESC, Price ASC;


-- Q14
SELECT referenceID, plantName, Variety, Height
    FROM Plant
    WHERE plantName LIKE "_e%" 
      AND Variety LIKE "C%e";
