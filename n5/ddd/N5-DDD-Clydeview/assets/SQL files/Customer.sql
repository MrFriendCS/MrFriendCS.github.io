CREATE TABLE Customer (
    customerNo INT NOT NULL,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    street VARCHAR(50) NOT NULL,
    town VARCHAR(20) NOT NULL,
    package VARCHAR(10) NOT NULL CHECK (package IN 
        ("Standard", "Large", "Premier")),
    directDebit BOOL NOT NULL,
    paymentDueDate DATE,
    PRIMARY KEY (customerNo)
);

INSERT INTO Customer VALUES (101,"Lauren","Calder","2 Paisley Street","Wemyss Bay","Premier",TRUE,"2020-04-12");
INSERT INTO Customer VALUES (102,"Abigail","Cameron","16 Paisley Street","Wemyss Bay","Standard",FALSE,"2020-04-12");
INSERT INTO Customer VALUES (103,"Ryan","Collins","17 Dunoon Drive","Gourock","Premier",TRUE,"2020-05-19");
INSERT INTO Customer VALUES (104,"Nicole","Rutherford","5A Panama Place","Port Glasgow","Large",FALSE,"2020-04-13");
INSERT INTO Customer VALUES (105,"Justine","O'Docherty","7 High Street","Kilmacolm","Premier",TRUE,"2020-04-18");
INSERT INTO Customer VALUES (106,"Shelby","Sweeney","3 Paisley Road","Port Glasgow","Premier",TRUE,"2020-05-26");
INSERT INTO Customer VALUES (107,"Donald","McAndrew","1 Big Hill Avenue","Inverkip","Standard",TRUE,"2020-08-01");
INSERT INTO Customer VALUES (108,"Rowan","Hastings","6 Clydeview Crescent","Gourock","Large",TRUE,"2020-05-05");
INSERT INTO Customer VALUES (109,"Grant","Donaldson","9 Dunoon Drive","Gourock","Premier",FALSE,"2020-04-07");
INSERT INTO Customer VALUES (110,"Christine","Flowers","63 Hamilton Drive","Greenock","Large",TRUE,"2020-04-19");
INSERT INTO Customer VALUES (111,"Ross","Lambie","12 Paisley Road","Kilmacolm","Standard",TRUE,"2020-03-27");
INSERT INTO Customer VALUES (112,"Paul","McGill","3C Cow Lane","Kilmacolm","Premier",FALSE,"2020-04-10");
INSERT INTO Customer VALUES (113,"Jack","Shields","4 Brookside Close","Port Glasgow","Large",FALSE,"2020-05-10");
INSERT INTO Customer VALUES (114,"Pauline","Milne","32 High Street","Kilmacolm","Premier",TRUE,"2020-05-09");
INSERT INTO Customer VALUES (115,"Margaret","Rice","5 Drumchapel Square","Greenock","Standard",FALSE,"2020-04-14");
