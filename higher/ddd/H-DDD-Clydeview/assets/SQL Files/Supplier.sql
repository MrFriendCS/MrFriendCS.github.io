CREATE TABLE Supplier (
    supplierID VARCHAR(5) NOT NULL,
    name VARCHAR(30) NOT NULL,
    address VARCHAR(30) NOT NULL,
    city VARCHAR(20) NOT NULL,
    postcode VARCHAR(8) NOT NULL,
    PRIMARY KEY (supplierID)
);

INSERT INTO Supplier VALUES ("BRE02","Bear Emporium","500 Park Street","Ayr","KA7 5AB");
INSERT INTO Supplier VALUES ("BRS01","Bears R Us","123 Main Street","Burnside","PA19 1UX");
INSERT INTO Supplier VALUES ("DLL01","Doll House Inc.","555 High Street","Dundee","DD1 7DD");
INSERT INTO Supplier VALUES ("FNG01","Fun and Games","42 Galaxy Road","London","N16 6PS");
INSERT INTO Supplier VALUES ("FRB01","Furball Inc.","1000 5th Avenue","New York","10001");
INSERT INTO Supplier VALUES ("JTS01","Jouets et Ours","1 Rue Amusement","Paris","75014");
