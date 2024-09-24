-- Task 7

.print
.print Q1
SELECT forename, surname
    FROM Customer
    WHERE surname = "Rice";

.print
.print Q2
SELECT forename, surname, town
    FROM Customer
    WHERE town = "Inverkip";

.print
.print Q3
SELECT surname, package, town
    FROM Customer
    WHERE package = "Large";

.print
.print Q4
SELECT surname, town, street
    FROM Customer
    WHERE town = "Port Glasgow";

.print
.print Q5
SELECT forename, surname, town
    FROM Customer
    ORDER BY surname ASC;

.print
.print Q6
SELECT forename, surname, paymentDueDate
    FROM Customer
    ORDER BY paymentDueDate DESC;

.print
.print Q7
SELECT forename, surname, customerNo
    FROM Customer
    WHERE customerNo > 110
    ORDER BY forename ASC;

.print
.print Q8
SELECT forename, surname, town
    FROM Customer
    WHERE town = "Kilmacolm"
    ORDER BY surname ASC;

.print