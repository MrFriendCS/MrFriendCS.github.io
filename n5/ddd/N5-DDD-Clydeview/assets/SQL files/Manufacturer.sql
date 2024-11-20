CREATE TABLE Manufacturer (
    manufacturerID INT NOT NULL,
    name VARCHAR(40),
    address VARCHAR(40),
    telephoneNumber VARCHAR(11) 
        CHECK (LENGTH(telephoneNumber) = 11),
    PRIMARY KEY (manufacturerID)
);

INSERT INTO Manufacturer VALUES (441,"Craft Supplies","Wishaw Industrial Estate","01415437212");
INSERT INTO Manufacturer VALUES (531,"Metal and Wood","Tyne Way Newcastle","01542123485");
INSERT INTO Manufacturer VALUES (627,"Tool Makers","231 London Walk Bristol","01347234987");
