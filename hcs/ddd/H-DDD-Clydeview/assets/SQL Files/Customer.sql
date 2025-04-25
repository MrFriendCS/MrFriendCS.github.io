CREATE TABLE Customer (
    customerID INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    address VARCHAR(30) NOT NULL,
    city VARCHAR(20) NOT NULL,
    postcode VARCHAR(8) NOT NULL,
    contactName VARCHAR(40) NOT NULL,
    email VARCHAR(50),
    PRIMARY KEY (customerID)
);

INSERT INTO Customer VALUES (1000000001,"Village Toys","200 Maple Lane","Dundee","DD21 1YX","John Smith","sales@villagetoys.com");
INSERT INTO Customer VALUES (1000000002,"Kids Place","333 South Lake Drive","Clydebank","G81 1KL","Michelle Green",NULL);
INSERT INTO Customer VALUES (1000000003,"Fun4All","1 Sunny Place","Montrose","DD10 9ZW","Jim Jones","jjones@fun4all.com");
INSERT INTO Customer VALUES (1000000004,"Fun4All","829 Riverside Drive","Paisley","PA1 2BB","Denise L. Stephens","dstephens@fun4all.com");
INSERT INTO Customer VALUES (1000000005,"The Toy Store","4545 53rd Street","Crieff","PH7 7JP","Kim Howard",NULL);
