-- Title: N5 CS 2020 Task 1 Part B - Reset
-- Author: Mr Friend
-- Date: 28 Sep 2024

    
/*
Not required to answer assignment questions.
Used to revert database back to start state.
*/

-- Q1b - Remove validation

CREATE TABLE newCustomer(
    customerID INT NOT NULL,
    forename VARCHAR(40) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    address VARCHAR(100),
    telephoneNo VARCHAR(11),
    PRIMARY KEY (customerID)
);

INSERT INTO newCustomer
    SELECT *
        FROM Customer;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

DROP TABLE Customer;

ALTER TABLE newCustomer
    RENAME TO Customer;

-- Referential integrity: On
PRAGMA foreign_keys = on;

CREATE TABLE newFlowerOrder(
    orderID VARCHAR(10) NOT NULL,
    dateDue DATE NOT NULL,
    price REAL NOT NULL,
    flowerType VARCHAR(8) NOT NULL
        CHECK (flowerType IN ("rose", "lily", "tulip", "daffodil")),
    bunchSize VARCHAR(6) NOT NULL
        CHECK (bunchSize IN ("small", "medium", "large")),
    chocolates BOOL NOT NULL,
    message VARCHAR(200),
    customerID INT NOT NULL,
    FOREIGN KEY (customerID)
        REFERENCES Customer(customerID),
    PRIMARY KEY (orderID)
);

INSERT INTO newFlowerOrder
    SELECT *
        FROM FlowerOrder;

-- Referential integrity: Off
PRAGMA foreign_keys = off;

DROP TABLE FlowerOrder;

ALTER TABLE newFlowerOrder
    RENAME TO FlowerOrder;

-- Referential integrity: On
PRAGMA foreign_keys = on;


-- Q1c(i) - Change Order back
.print Change back
UPDATE FlowerOrder
    SET flowerType = "rose", price = 34
    WHERE orderID = "CHQ3848";


-- Q1c(ii) - Remove customer
DELETE FROM Customer
    WHERE customerID = 2986;
