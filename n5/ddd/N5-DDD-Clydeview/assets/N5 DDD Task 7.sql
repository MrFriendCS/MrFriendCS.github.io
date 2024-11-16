-- N5 DDD - Task 7

-- Q1
SELECT forename, surname
    FROM Customer
    WHERE surname = "Rice";

-- Q2
SELECT forename, surname, town
    FROM Customer
    WHERE town = "Inverkip";

-- Q3
SELECT surname, package, town
    FROM Customer
    WHERE package = "Large";

-- Q4
SELECT surname, town, street
    FROM Customer
    WHERE town = "Port Glasgow";

-- Q5
SELECT forename, surname, town
    FROM Customer
    ORDER BY surname ASC;

-- Q6
SELECT forename, surname, paymentDueDate
    FROM Customer
    ORDER BY paymentDueDate DESC;

-- Q7
SELECT forename, surname, customerNo
    FROM Customer
    WHERE customerNo > 110
    ORDER BY forename ASC;

-- Q8
SELECT forename, surname, town
    FROM Customer
    WHERE town = "Kilmacolm"
    ORDER BY surname ASC;
