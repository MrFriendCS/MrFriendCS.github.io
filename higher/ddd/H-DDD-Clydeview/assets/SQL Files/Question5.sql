CREATE TABLE Question5 (
    productName VARCHAR(20) NOT NULL,
    productID VARCHAR(50) NOT NULL,
    priceUK FLOAT NOT NULL
        CHECK(priceUK >= 0.00),
    PRIMARY KEY (productID)
);

INSERT INTO Question5 VALUES ("Basic Keyboard","001",7.00);
INSERT INTO Question5 VALUES ("Network Card","002",13.50);
INSERT INTO Question5 VALUES ("Optical Mouse","017",7.50);
INSERT INTO Question5 VALUES ("Monitor","034",30.00);
INSERT INTO Question5 VALUES ("3D Graphics Card","097",30.00);
INSERT INTO Question5 VALUES ("Flat Screen Monitor","102",75.00);
