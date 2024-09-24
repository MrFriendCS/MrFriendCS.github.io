-- Don't touch lines 1 to 6
.open AuctionDatabase.db
.headers on
.mode column
PRAGMA foreign_keys = on;
-- Don't touch lines 1 to 6


/*
Title: N5 CS 2022 Task 2 Part C
Author: Mr Friend
Date: 25 Nov 2023
*/

.print
.print N5 CS 2022 Task 2 Part C

.print
.print Q2c(i)
    
UPDATE property
    SET askingPrice = 112000
    WHERE propertyRef = "DUN-101";

SELECT * FROM property
    WHERE propertyRef = "DUN-101";


.print
.print Q2c(ii) - Add seller
    
INSERT INTO seller
    VALUES ("Eve Grace", "128 Cameron Drive Edinburgh EH4 5DS", 1502, "EveGrace@yehoo.net", "0131 279100");

SELECT *
    FROM seller
    WHERE sellerID = 1502;


.print
.print Q2c(iii) - Workshop
    
SELECT email, telephoneNumber, postcode
    FROM seller, property
    WHERE seller.sellerID = property.sellerID
        AND numberOfBedrooms = 3
        AND askingPrice < 150000;


.print

    


/*
Not required to answer assignment questions.
Used to revert database back to start state.
*/

-- Q2c(ii) - Add seller
DELETE FROM seller
    WHERE sellerID = 1502;
