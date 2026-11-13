CREATE TABLE Table4 (
    productID INT NOT NULL,
    productName VARCHAR(12) NOT NULL,
    buyPricePence INT NOT NULL
        CHECK(buyPricePence >= 0),
    sellPricePence INT NOT NULL
        CHECK(sellPricePence >= 0),
    PRIMARY KEY (productID)
);

INSERT INTO Table4 VALUES (1,"Mars Bar",27,42);
INSERT INTO Table4 VALUES (2,"Snickers",31,25);
INSERT INTO Table4 VALUES (3,"Yorkie",32,45);
INSERT INTO Table4 VALUES (4,"Bounty",26,21);
