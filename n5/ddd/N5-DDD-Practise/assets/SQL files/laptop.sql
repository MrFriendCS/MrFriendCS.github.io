CREATE TABLE Laptop (
    laptop INT NOT NULL,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20) NOT NULL,
    value REAL NOT NULL,
    working BOOL NOT NULL,
    PRIMARY KEY (laptop)
);

INSERT INTO Laptop VALUES (1,"HP","Spectre",1700,TRUE);
INSERT INTO Laptop VALUES (2,"Dell","Latitude",800,TRUE);
INSERT INTO Laptop VALUES (3,"Microsoft","Surface",1350,FALSE);
INSERT INTO Laptop VALUES (4,"Dell","Inspiron",350,FALSE);
INSERT INTO Laptop VALUES (5,"Microsoft","Surface Pro",1850,TRUE);
INSERT INTO Laptop VALUES (6,"Apple","MacBook Air",1300,TRUE);
INSERT INTO Laptop VALUES (7,"HP","Envy",1200,TRUE);
INSERT INTO Laptop VALUES (8,"Microsoft","Surface",1850,TRUE);
INSERT INTO Laptop VALUES (9,"Microsoft","Surface Pro",1400,TRUE);
INSERT INTO Laptop VALUES (10,"Dell","Inspiron",450,TRUE);
INSERT INTO Laptop VALUES (11,"Dell","Spectre",1350,FALSE);
INSERT INTO Laptop VALUES (12,"Microsoft","Surface",1350,FALSE);
