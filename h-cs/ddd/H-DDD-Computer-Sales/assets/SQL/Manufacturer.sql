CREATE TABLE Manufacturer (
    manufacturerID INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    website VARCHAR(50),
    yearFounded INT
        CHECK (yearFounded >= 1900),
    trading BOOL NOT NULL,
    PRIMARY KEY (manufacturerID)
);

INSERT INTO Manufacturer VALUES ('1','Raspberry Pi','https://raspberrypi.org',2008,1);
INSERT INTO Manufacturer VALUES ('2','Apple','https://apple.com',1976,1);
INSERT INTO Manufacturer VALUES ('3','Commodore','https://www.commodore.ca',1954,0);
