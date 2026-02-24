CREATE TABLE Series (
    seriesID INT NOT NULL,
    seriesName VARCHAR(30) NOT NULL,
    startYear INT NOT NULL,
    endYear INT NOT NULL,
    PRIMARY KEY (seriesID)
);

INSERT INTO Series VALUES (1,"The OK Seven",1960,2000);
INSERT INTO Series VALUES (2,"The Revengos",1962,2013);
INSERT INTO Series VALUES (3,"The Bat Folks",1967,2007);
INSERT INTO Series VALUES (4,"Falcon and the Beasts",1962,2010);
INSERT INTO Series VALUES (5,"The American Nightmare",1967,2019);
