CREATE TABLE Club ( 
    clubID VARCHAR(6) NOT NULL UNIQUE,
    name VARCHAR(30) NOT NULL,
    location VARCHAR(30) NOT NULL,
    type VARCHAR(20) NOT NULL,
    opened DATE,
    trainer BOOLEAN,
    rooms INT
        CHECK(rooms >= 0),
    PRIMARY KEY (clubID)
);

INSERT INTO Club VALUES ("SP107","Well Life","Allentown","Leisure Centre","2015-05-24",FALSE,2);
INSERT INTO Club VALUES ("SP128","KickAbout","Brockton","Astroturf","1999-11-22",FALSE,2);
INSERT INTO Club VALUES ("SP197","Puddles","Baldwin","Swimming Pool","2009-01-18",FALSE,3);
INSERT INTO Club VALUES ("SP324","Trim","Allentown","Gym","2010-05-11",TRUE,5);
INSERT INTO Club VALUES ("SP345","Living Fit","Lowhall","Leisure Centre","2002-07-05",TRUE,1);
INSERT INTO Club VALUES ("SP365","Shape Up","Baldwin","Gym","2005-08-04",TRUE,1);
INSERT INTO Club VALUES ("SP433","Waves","Brockton","Swimming Pool","1996-05-16",TRUE,2);
INSERT INTO Club VALUES ("SP487","Toners","Lowhall","Gym","1996-08-15",FALSE,3);
