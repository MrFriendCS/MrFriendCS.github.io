CREATE TABLE Table3 (
    studentID INT NOT NULL,
    forename VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    test1 INT NOT NULL
        CHECK(test1 >= 0 AND test1 <= 20),
    test2 INT NOT NULL
        CHECK(test2 >= 0 AND test2 <= 20),
    test3 INT NOT NULL
        CHECK(test3 >= 0 AND test3 <= 20),
    test4 INT NOT NULL
        CHECK(test4 >= 0 AND test4 <= 20),
    test5 INT NOT NULL
        CHECK(test5 >= 0 AND test5 <= 20),
    PRIMARY KEY (studentID)
);

INSERT INTO Table3 VALUES (1,"Bill","Smith",15,12,12,13,14);
INSERT INTO Table3 VALUES (2,"Harry","Johnstone",12,11,14,13,16);
INSERT INTO Table3 VALUES (3,"Ann","Clark",14,14,13,15,15);
INSERT INTO Table3 VALUES (4,"Billy","Smith",10,9,12,11,14);
INSERT INTO Table3 VALUES (5,"Tom","Harris",14,14,14,12,14);
