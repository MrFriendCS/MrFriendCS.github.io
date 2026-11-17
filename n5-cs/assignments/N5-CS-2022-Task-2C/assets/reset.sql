-- Title: N5 CS 2022 Task 2 Part C
-- Author: Mr Friend
-- Date: 28 Sep 2024


/*
Not required to answer assignment questions.
Used to revert database back to start state.
*/

-- Q2c(i)  - Revert property price
UPDATE property
    SET askingPrice = 105500
    WHERE propertyRef = "DUN-101";


-- Q2c(ii) - Remove seller
DELETE FROM seller
    WHERE sellerID = 1502;

