CREATE TABLE Table2 (
    staffID INT NOT NULL,
    forename VARCHAR(12) NOT NULL,
    surname VARCHAR(12) NOT NULL,
    hourlyRate FLOAT NOT NULL
        CHECK(hourlyRate >= 0),
    hoursWorked INT NOT NULL
        CHECK(hoursWorked >= 0),
    PRIMARY KEY (staffID)
);

INSERT INTO Table2 VALUES (1,"Kenneth","Brown",7.50,20);
INSERT INTO Table2 VALUES (2,"David","Gilmour",6.00,34);
INSERT INTO Table2 VALUES (3,"Ashley","Grant",6.00,35);
INSERT INTO Table2 VALUES (4,"Vickie","Moore",6.00,35);
INSERT INTO Table2 VALUES (5,"Laura","Green",4.50,20);
