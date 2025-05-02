CREATE TABLE Hairdresser (
    hairdresserid INT NOT NULL,
    firstname VARCHAR(20),
    lastname VARCHAR(30),
    contactnumber VARCHAR(13) NOT NULL
        CHECK(LENGTH(contactnumber >= 11)),
    salon VARCHAR(30),
    PRIMARY KEY (hairdresserid)
);

INSERT INTO Hairdresser VALUES (1928,"Phillip","Christie","07700 900142","Cuts & Co");
INSERT INTO Hairdresser VALUES (2019,"Sharon","Watt","07700 900582","On The Corner");
INSERT INTO Hairdresser VALUES (2210,"Huda","Quhshi","07700 900477","West Style");
INSERT INTO Hairdresser VALUES (2098,"Katie","Hocine","07827 933024","Uist Beauty");
INSERT INTO Hairdresser VALUES (2217,"Lizzie","MacInnes","07535 509294","Hair by Lizzi");
INSERT INTO Hairdresser VALUES (2910,"Jakki","MacKinnon","07789 429371","Jakki'z Hairdressing");
