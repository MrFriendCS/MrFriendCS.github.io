CREATE TABLE Client (
    clientid INT NOT NULL,
    hairdresserid INT NOT NULL,
    firstname VARCHAR(20),
    lastname VARCHAR(30),
    contactnumber VARCHAR(13) NOT NULL
        CHECK(LENGTH(contactnumber >= 11)),
    FOREIGN KEY (hairdresserid)
        REFERENCES Hairdresser (hairdresserid),
    PRIMARY KEY (clientid)
);

INSERT INTO Client VALUES (10290,1928,"Wen","Qiu","0141 496 0536");
INSERT INTO Client VALUES (10291,2019,"Peta","Mulisdottir","0151 496 0838");
INSERT INTO Client VALUES (11766,1928,"Michael","Waters","07700 900556");
INSERT INTO Client VALUES (12654,1928,"Faseeha","al-Allam","07700 900569");
INSERT INTO Client VALUES (20533,2019,"Egisto","Mario","0131 496 0294");
INSERT INTO Client VALUES (32100,2210,"Emily","Sieff","020 7946 0126");
INSERT INTO Client VALUES (36172,2210,"Phillip","Roach","0131 496 0734");
