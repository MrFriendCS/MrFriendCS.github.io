CREATE TABLE Race (
    raceNumber INT NOT NULL,
    raceCategory VARCHAR(255) NOT NULL,
    stroke VARCHAR(255) NOT NULL,
    distance INT NOT NULL,
    eventID VARCHAR(255) NOT NULL,
	FOREIGN KEY (eventID)
	    REFERENCES Event (eventID),
	PRIMARY KEY (raceNumber)
);


INSERT INTO Race VALUES(1,"Intermediate","Backstroke",100,"Event 1");
INSERT INTO Race VALUES(2,"Advanced","Breaststroke",200,"Event 1");
INSERT INTO Race VALUES(3,"Intermediate","Butterfly",100,"Event 1");
INSERT INTO Race VALUES(4,"Advanced","Freestyle",50,"Event 1");
INSERT INTO Race VALUES(5,"Intermediate","Freestyle",200,"Event 1");
INSERT INTO Race VALUES(6,"Advanced","Backstroke",100,"Event 2");
INSERT INTO Race VALUES(7,"Intermediate","Breaststroke",200,"Event 2");
INSERT INTO Race VALUES(8,"Advanced","Butterfly",200,"Event 2");
INSERT INTO Race VALUES(9,"Intermediate","Freestyle",100,"Event 2");
INSERT INTO Race VALUES(10,"Advanced","Freestyle",400,"Event 2");
INSERT INTO Race VALUES(11,"Intermediate","Backstroke",200,"Event 3");
INSERT INTO Race VALUES(12,"Advanced","Breaststroke",100,"Event 3");
INSERT INTO Race VALUES(13,"Intermediate","Butterfly",200,"Event 3");
INSERT INTO Race VALUES(14,"Advanced","Freestyle",100,"Event 3");
INSERT INTO Race VALUES(15,"Intermediate","Freestyle",400,"Event 3");
INSERT INTO Race VALUES(16,"Advanced","Backstroke",200,"Event 4");
INSERT INTO Race VALUES(17,"Intermediate","Breaststroke",100,"Event 4");
INSERT INTO Race VALUES(18,"Advanced","Butterfly",100,"Event 4");
INSERT INTO Race VALUES(19,"Intermediate","Freestyle",50,"Event 4");
INSERT INTO Race VALUES(20,"Advanced","Freestyle",200,"Event 4");
