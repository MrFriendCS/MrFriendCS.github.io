CREATE TABLE Table1 (
    pupilID INT NOT NULL,
    forename VARCHAR(12) NOT NULL,
    surname VARCHAR(12) NOT NULL,
    test1 INT NOT NULL
        CHECK(test1 >= 0 AND test1 <= 10),
    test2 INT NOT NULL
        CHECK(test2 >= 0 AND test2 <= 10),
    test3 INT NOT NULL
        CHECK(test3 >= 0 AND test3 <= 10),
    test4 INT NOT NULL
        CHECK(test4 >= 0 AND test4 <= 10),
    PRIMARY KEY (pupilID)
);

INSERT INTO Table1 (VALUES (1,"Jane","Smith",9,7,8,6);
INSERT INTO Table1 VALUES (2,"Duncan","Scott",10,8,9,8);
INSERT INTO Table1 VALUES (3,"James","Webster",8,6,7,9);
INSERT INTO Table1 VALUES (4,"Julie","O'Brian",7,6,9,5);
INSERT INTO Table1 VALUES (5,"Mary","Davis",9,9,7,5);
INSERT INTO Table1 VALUES (6,"Adam","Young",10,8,7,6);
INSERT INTO Table1 VALUES (7,"Holly","Jeffreys",8,7,6,9);
INSERT INTO Table1 VALUES (8,"Annie","McKay",7,8,8,10);
