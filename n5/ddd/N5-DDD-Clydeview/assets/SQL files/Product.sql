CREATE TABLE Product (
    productName VARCHAR(40) NOT NULL,
    productCode VARCHAR(40),
    numberInStock INT,
    onOrder BOOL,
    costPrice REAL,
    manufacturerID INT NOT NULL,
    FOREIGN KEY (manufacturerID) 
        REFERENCES Manufacturer (manufacturerID),
    PRIMARY KEY (productCode)
);

INSERT INTO Product VALUES ("Claw Hammer","CH20",2,TRUE,4.99,531);
INSERT INTO Product VALUES ("Combi Drill","CMBD",12,TRUE,148.77,627);
INSERT INTO Product VALUES ("Mallet","MA16",7,FALSE,5.50,531);
INSERT INTO Product VALUES ("Medium Paint Brush (Size 2)","MPB2",34,TRUE,5.65,531);
INSERT INTO Product VALUES ("Metal File","MTF5",9,FALSE,8.49,441);
INSERT INTO Product VALUES ("Pliers","PLS6",5,TRUE,11.99,441);
INSERT INTO Product VALUES ("Saw","SW22",4,FALSE,9.99,531);
INSERT INTO Product VALUES ("Top Handled Jigsaw","JIG4",2,TRUE,165,627);
