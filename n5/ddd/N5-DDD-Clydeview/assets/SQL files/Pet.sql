CREATE TABLE Pet (
    petCode VARCHAR(5) NOT NULL 
        CHECK(LENGTH(petCode) = 5),
    petName VARCHAR(20),
    petType VARCHAR(8),
    dateOfBirth DATE,
    vaccination BOOL,
    ownerID INT NOT NULL,
    FOREIGN KEY (ownerID)
        REFERENCES Owner (ownerID),
    PRIMARY KEY (petCode)
);

INSERT INTO Pet VALUES ("P0123","Misty","cat","2012-01-23",TRUE,2356);
INSERT INTO Pet VALUES ("P0345","Rover","dog","2010-12-12",TRUE,3821);
INSERT INTO Pet VALUES ("P0887","Foggy","cat","2012-01-23",TRUE,1277);
INSERT INTO Pet VALUES ("P1559","Gladys","gerbil","2010-04-16",FALSE,1277);
INSERT INTO Pet VALUES ("P1985","Slinky","tortoise","2016-09-24",FALSE,3510);
INSERT INTO Pet VALUES ("P2233","Speedy","tortoise","2013-06-09",TRUE,1277);
