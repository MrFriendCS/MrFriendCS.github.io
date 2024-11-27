CREATE TABLE Pet (
    code VARCHAR(5) NOT NULL 
        CHECK(LENGTH(code) = 5),
    name VARCHAR(20),
    type VARCHAR(8)
        CHECK (type IN("Budgie", "Cat", "Dog", "Gerbil", "Tortoise")),
    dateOfBirth DATE,
    vaccination BOOL,
    ownerID INT NOT NULL,
    FOREIGN KEY (ownerID)
        REFERENCES Owner (ownerID),
    PRIMARY KEY (code)
);

INSERT INTO Pet VALUES ("P0123","Misty","Cat","2020-01-21",TRUE,2356);
INSERT INTO Pet VALUES ("P0345","Rover","Dog","2018-12-10",TRUE,3821);
INSERT INTO Pet VALUES ("P0887","Foggy","Cat","2020-01-21",TRUE,1277);
INSERT INTO Pet VALUES ("P1559","Gladys","Gerbil","2018-04-14",FALSE,1277);
INSERT INTO Pet VALUES ("P1985","Slinky","Tortoise","2024-09-22",FALSE,3510);
INSERT INTO Pet VALUES ("P2233","Speedy","Tortoise","2021-06-07",TRUE,1277);
