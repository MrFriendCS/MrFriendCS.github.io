-- Title: N5 CS 2022 Task 2 Part C
-- Author: Mr Friend
-- Date: 28 Sep 2024


-- Q2c(i)  - Change property price
UPDATE property
    SET askingPrice = 112000
    WHERE propertyRef = "DUN-101";

-- Q2c(i)  - Evidence
SELECT * FROM property
    WHERE propertyRef = "DUN-101";


-- Q2c(ii) - Add seller
INSERT INTO seller
    VALUES ("Eve Grace", "128 Cameron Drive Edinburgh EH4 5DS", 1502, "EveGrace@yehoo.net", "0131 279100");

-- Q2c(ii) - Evidence
SELECT *
    FROM seller
    WHERE sellerID = 1502;


-- Q2c(iii) - Workshop  
SELECT email, telephoneNumber, postcode
    FROM seller, property
    WHERE seller.sellerID = property.sellerID
        AND numberOfBedrooms = 3
        AND askingPrice < 150000;