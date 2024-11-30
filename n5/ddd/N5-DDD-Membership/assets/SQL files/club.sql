CREATE TABLE club (
    id VARCHAR(6) NOT NULL UNIQUE,
    name VARCHAR(30) NOT NULL,
    location VARCHAR(30) NOT NULL,
    type VARCHAR(20) NOT NULL,
    opened DATE,
    trainer BOOLEAN,
    rooms INT CHECK(rooms >= 0),
    PRIMARY KEY (id)
);

INSERT INTO club VALUES ("SP107","Well Life","Allentown","Leisure Centre","2015-05-24",0,2);
INSERT INTO club VALUES ("SP128","KickAbout","Brockton","Astroturf","1999-11-22",0,2);
INSERT INTO club VALUES ("SP197","Puddles","Baldwin","Swimming Pool","2009-01-18",0,3);
INSERT INTO club VALUES ("SP324","Trim","Allentown","Gym","2010-05-11",1,5);
INSERT INTO club VALUES ("SP345","Living Fit","Lowhall","Leisure Centre","2002-07-05",1,1);
INSERT INTO club VALUES ("SP365","Shape Up","Baldwin","Gym","2005-08-04",1,1);
INSERT INTO club VALUES ("SP433","Waves","Brockton","Swimming Pool","1996-05-16",1,2);
INSERT INTO club VALUES ("SP487","Toners","Lowhall","Gym","1996-08-15",0,3);
