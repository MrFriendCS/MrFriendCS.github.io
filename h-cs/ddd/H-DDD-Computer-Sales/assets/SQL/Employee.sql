CREATE TABLE Employee (
    employeeID VARCHAR(10) NOT NULL,
    firstName VARCHAR(15) NOT NULL
        CHECK (LENGTH(firstName) >= 3),
    lastName VARCHAR(20) NOT NULL
        CHECK (LENGTH(lastName) >= 3),
    houseNo INT
        CHECK (houseNo > 0),
    street VARCHAR(20),
    town VARCHAR(20),
    county VARCHAR(20),
    postcode VARCHAR(8),
    phone VARCHAR(20)
        CHECK (LENGTH(phone) = 11),
    daysPerWeek REAL
        CHECK (daysPerWeek >= 0.0 AND daysPerWeek <= 7.0),
    PRIMARY KEY (employeeID)
);

INSERT INTO Employee VALUES ('mhogan','Matt','Hogan','21','Street Lane','Mytown','Countyshire','CX2 2TT','09898778991',2.5);
INSERT INTO Employee VALUES ('hpatel','Hitesh','Patel','1','Avenue Place','Mytown','Countyshire','CX1 9BT','09833455784',5);
INSERT INTO Employee VALUES ('mhanlon','Martin','Hanlon','78','Square Gardens','Yourillage','Countyshire','CX6 3EF','09815644177',4);
INSERT INTO Employee VALUES ('lsach','Laura','Sach','','The House','Cutting','Countyshire','CX8 9OP','09847549988',3);
