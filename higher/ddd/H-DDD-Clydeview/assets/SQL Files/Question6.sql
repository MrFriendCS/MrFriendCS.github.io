CREATE TABLE Question6 (
    fishType VARCHAR(12) NOT NULL,
    pricePerKilo FLOAT NOT NULL
        CHECK(pricePerKilo >= 0.00),
    numberOfKilos FLOAT NOT NULL
        CHECK(numberOfKilos >= 0.0),
    PRIMARY KEY (fishType)
);

INSERT INTO Question6 VALUES ("Anchovies",15.00,2.5);
INSERT INTO Question6 VALUES ("Cod",12.00,3.0);
INSERT INTO Question6 VALUES ("Coley",7.00,1.0);
INSERT INTO Question6 VALUES ("Grey Mullet",5.50,2.5);
INSERT INTO Question6 VALUES ("Gurnard",5.75,3.0);
INSERT INTO Question6 VALUES ("Haddock",12.00,5.0);
INSERT INTO Question6 VALUES ("Halibut",16.45,3.5);
INSERT INTO Question6 VALUES ("Herring",4.50,2.0);
INSERT INTO Question6 VALUES ("Huss",9.80,1.5);
INSERT INTO Question6 VALUES ("Lemon Sole",14.49,4.0);
INSERT INTO Question6 VALUES ("Mackeral",6.79,5.0);
INSERT INTO Question6 VALUES ("Monkfish",16.00,2.5);
INSERT INTO Question6 VALUES ("Plaice",6.00,4.0);
INSERT INTO Question6 VALUES ("Red Mullet",12.00,1.0);
INSERT INTO Question6 VALUES ("Salmon",10.00,8.5);
INSERT INTO Question6 VALUES ("Sea Bass",9.75,6.0);
INSERT INTO Question6 VALUES ("Skate",9.95,3.0);
INSERT INTO Question6 VALUES ("Snapper",13.00,2.5);
INSERT INTO Question6 VALUES ("Sprats",4.00,0.5);
INSERT INTO Question6 VALUES ("Trout",8.95,3.0);
