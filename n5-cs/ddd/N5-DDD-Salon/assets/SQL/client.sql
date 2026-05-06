CREATE TABLE Client (
    clientid INT NOT NULL,
    hairdresserID INT NOT NULL,
    firstName VARCHAR(20),
    lastName VARCHAR(30),
    phone VARCHAR(13) NOT NULL
        CHECK(LENGTH(phone >= 11)),
    FOREIGN KEY (hairdresserID)
        REFERENCES Hairdresser (hairdresserID),
    PRIMARY KEY (clientID)
);

INSERT INTO Client VALUES (hairdresserID,clientID,"firstName","lastName","phone");
INSERT INTO Client VALUES (1928,10290,"Wen","Qiu","0141 496 0536");
INSERT INTO Client VALUES (2019,10291,"Peta","Mulisdottir","0151 496 0838");
INSERT INTO Client VALUES (1928,11766,"Michael","Waters","07700 900556");
INSERT INTO Client VALUES (1928,12654,"Faseeha","al-Allam","07700 900569");
INSERT INTO Client VALUES (2019,20533,"Egisto","Mario","0131 496 0294");
INSERT INTO Client VALUES (2210,32100,"Emily","Sieff","020 7946 0126");
INSERT INTO Client VALUES (2210,36172,"Phillip","Roach","0131 496 0734");
