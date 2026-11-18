CREATE TABLE Doctor (
    doctorID INT NOT NULL
        CHECK (doctorID >= 1),
    forename VARCHAR(15) NOT NULL,
    surname VARCHAR(15) NOT NULL,
    address VARCHAR(30) NOT NULL,
    postcode VARCHAR(8) NOT NULL,
    telNo VARCHAR(12) NOT NULL,
    dateQualified DATE NOT NULL,
    PRIMARY KEY (doctorID)
);

INSERT INTO Doctor VALUES (9,'Judy','Hardcastle','20 Ankle Place','Edinburgh','EH4 8HQ','0131 865346');
INSERT INTO Doctor VALUES (12,'Harry','Nutt','30 Hip Court','Edinburgh','EH12 9DF','07973 765346');
INSERT INTO Doctor VALUES (34,'Mohammed','McRae','99 Head Drive','Edinburgh','EH22 2HN','07774 738465');
INSERT INTO Doctor VALUES (38,'Alice','Budge','6 Knee Drive','Edinburgh','EH17 6RF','0131 441 5411');
INSERT INTO Doctor VALUES (41,'Susan','Edwards','8a Toe Street','Livingston','EH54 6YH','01506 880621');
INSERT INTO Doctor VALUES (48,'Gerard','Cooper','17 New Street','Edinburgh','EH14 6FG','0131 446 5110');
INSERT INTO Doctor VALUES (59,'Caroline','Gilmour','2 Anderson Way','Edinburgh','EH1 5RT','0131 467 2209');
