CREATE TABLE Model (
    modelID INT NOT NULL
        CHECK (modelID > 0),
    manufacturerID INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    cpuSpeed REAL
        CHECK (cpuSpeed > 0.0),
    ram REAL
        CHECK (ram > 0.0),
    cores INT
        CHECK (cores >= 1),
    wifi BOOLEAN,
    releaseDate DATE,
    PRIMARY KEY (modelID),
    FOREIGN KEY (manufacturerID)
        REFERENCES Manufacturer (manufacturerID)
);

INSERT INTO Model VALUES (1,1,'Raspberry Pi 1 Model A',0.7,256.0,1,0,'2013-02-01');
INSERT INTO Model VALUES (2,1,'Raspberry Pi 1 Model B 256MB',0.7,256.0,1,0,'2012-04-01');
INSERT INTO Model VALUES (3,1,'Raspberry Pi 1 Model B 512MB',0.7,512.0,1,0,'2012-10-01');
INSERT INTO Model VALUES (4,1,'Raspberry Pi 1 Model A+',0.7,512.0,1,0,'2014-11-01');
INSERT INTO Model VALUES (5,1,'Raspberry Pi 1 Model B+',0.7,512.0,1,0,'2014-07-01');
INSERT INTO Model VALUES (6,1,'Raspberry Pi 2 Model B',0.9,1024.0,4,0,'2015-02-01');
INSERT INTO Model VALUES (7,1,'Raspberry Pi 3 Model B',1.2,1024.0,4,1,'2016-02-01');
INSERT INTO Model VALUES (8,1,'Raspberry Pi 3 Model B+',1.4,1024.0,4,1,'2018-03-14');
INSERT INTO Model VALUES (9,1,'Raspberry Pi 3 Model A+',1.4,1024.0,4,1,'2018-11-01');
INSERT INTO Model VALUES (10,1,'Raspberry Pi 4 Model B 1GB',1.5,1024.0,4,1,'2019-06-24');
INSERT INTO Model VALUES (11,1,'Raspberry Pi 4 Model B 2GB',1.5,2048.0,4,1,'2019-06-24');
INSERT INTO Model VALUES (12,1,'Raspberry Pi 4 Model B 4GB',1.5,4096.0,4,1,'2019-06-24');
INSERT INTO Model VALUES (13,1,'Raspberry Pi Zero',1.0,512.0,1,0,'2015-11-01');
INSERT INTO Model VALUES (14,1,'Raspberry Pi Zero W',1.0,512.0,1,1,'2017-02-28');
INSERT INTO Model VALUES (15,2,'Apple Lisa',0.008,1.0,1,0,'1983-01-19');
INSERT INTO Model VALUES (16,2,'Apple iMac',3.7,8192.0,4,1,'2019-03-19');
INSERT INTO Model VALUES (17,2,'Apple MacBook Pro',2.6,16384.0,6,1,'2019-05-21');
INSERT INTO Model VALUES (18,2,'Apple MacBook Air',2.6,8192.0,2,1,'2019-07-09');
INSERT INTO Model VALUES (19,3,'Commodore VIC-20',0.00102,0.005,1,0,'1980-01-01');
INSERT INTO Model VALUES (20,3,'Commodore 64',0.001023,0.064,1,0,'1982-08-01');
INSERT INTO Model VALUES (21,3,'Amiga 500',0.00716,0.5,1,0,'1987-04-01');
