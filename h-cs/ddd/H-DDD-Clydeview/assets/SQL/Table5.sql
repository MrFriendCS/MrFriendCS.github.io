CREATE TABLE Table5 (
    productName VARCHAR(20) NOT NULL,
    productID VARCHAR(50) NOT NULL,
    priceUK FLOAT NOT NULL
        CHECK(priceUK >= 0.00),
    PRIMARY KEY (productID)
);

INSERT INTO Table5 VALUES ("Basic Keyboard","1",7);
INSERT INTO Table5 VALUES ("Network Card","2",13.5);
INSERT INTO Table5 VALUES ("Optical Mouse","17",7.5);
INSERT INTO Table5 VALUES ("Monitor","34",30);
INSERT INTO Table5 VALUES ("3D Graphics Card","97",30);
INSERT INTO Table5 VALUES ("Flat Screen Monitor","102",75);
