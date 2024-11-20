CREATE TABLE Owner (
    ownerID INTEGER NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    address VARCHAR(40) NOT NULL,
    town VARCHAR(20) NOT NULL,
    contactTele VARCHAR(11) NOT NULL 
        CHECK (LENGTH(contactTele) = 11),
    PRIMARY KEY (ownerID)
);

INSERT INTO Owner VALUES (1277,"Hardeep","Singh","64 Iona Way","Greenock","01475255707");
INSERT INTO Owner VALUES (2356,"Sally","Chan","142 Main Street","Greenock","01475242499");
INSERT INTO Owner VALUES (3510,"Elaine","Bryce","29 Clyde Drive","Gourock","01475636321");
INSERT INTO Owner VALUES (3821,"Cameron","Gray","17 Shuttle Street","Gourock","01475312245");
