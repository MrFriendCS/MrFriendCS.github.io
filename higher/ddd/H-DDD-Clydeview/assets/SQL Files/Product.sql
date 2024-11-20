CREATE TABLE Product (
    productID VARCHAR(10) NOT NULL,
    supplierID VARCHAR(5) NOT NULL,
    name VARCHAR(30) NOT NULL,
    price REAL NOT NULL,
    description VARCHAR(100) NOT NULL,
    FOREIGN KEY (supplierID)
        REFERENCES Supplier (supplierID),
    PRIMARY KEY (productID)
);

INSERT INTO Product VALUES ("BNBG01","DLL01","Fish bean bag toy",3.49,"Fish bean bag toy");
INSERT INTO Product VALUES ("BNBG02","DLL01","Bird bean bag toy",3.49,"Bird bean bag toy");
INSERT INTO Product VALUES ("BNBG03","DLL01","Rabbit bean bag toy",3.49,"Rabbit bean bag toy");
INSERT INTO Product VALUES ("BR01","BRS01","8 inch teddy bear",5.99,"8 inch teddy bear");
INSERT INTO Product VALUES ("BR02","BRS01","12 inch teddy bear",8.99,"12 inch teddy bear");
INSERT INTO Product VALUES ("BR03","BRS01","18 inch teddy bear",11.99,"18 inch teddy bear");
INSERT INTO Product VALUES ("RGAN01","DLL01","Raggedy Ann",4.99,"18 inch Raggedy Ann doll");
INSERT INTO Product VALUES ("RYL01","FNG01","King doll",9.49,"12 inch king doll with royal garments and crown");
INSERT INTO Product VALUES ("RYL02","FNG01","Queen doll",9.49,"12 inch queen doll with royal garments and crown");
