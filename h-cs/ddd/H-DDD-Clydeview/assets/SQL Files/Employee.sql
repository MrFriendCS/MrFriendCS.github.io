CREATE TABLE Employee (
    employeeID INT NOT NULL,
    jobTitle VARCHAR(8) NOT NULL,
    name VARCHAR(20),
    building VARCHAR(2),
    yearsEmployed INT NOT NULL
        CHECK(yearsEmployed >= 0),
    PRIMARY KEY (employeeID)
);

INSERT INTO Employee VALUES (13428,"Engineer","Becky A.","1e",4);
INSERT INTO Employee VALUES (13677,"Engineer","Dan B.","1e",2);
INSERT INTO Employee VALUES (14002,"Engineer","Sharon F.","1e",6);
INSERT INTO Employee VALUES (14093,"Engineer","Dan M.","1e",4);
INSERT INTO Employee VALUES (14162,"Engineer","Malcom S.","1e",1);
INSERT INTO Employee VALUES (14208,"Admin","Tylar S.","2w",2);
INSERT INTO Employee VALUES (14235,"Admin","Sherman D.","2w",8);
INSERT INTO Employee VALUES (14689,"Admin","Jakob J.","2w",6);
INSERT INTO Employee VALUES (15725,"Admin","Lillia A.","2w",7);
INSERT INTO Employee VALUES (15730,"Admin","Brandon J.","2w",7);
INSERT INTO Employee VALUES (15992,"Manager","Scott K.","1e",9);
INSERT INTO Employee VALUES (16432,"Manager","Shirlee M.","1e",3);
INSERT INTO Employee VALUES (16547,"Manager","Daria O.","2w",6);
