CREATE TABLE Author (
    authorRef INT NOT NULL,
    forename VARCHAR(20),
    surname VARCHAR(20),
    nationality VARCHAR(20),
    dob DATE,
    website VARCHAR(80),
    PRIMARY KEY (authorRef)
);

INSERT INTO Author VALUES (1862,"Nick","Hornby","British","1957-04-17","www.nickhornbyofficial.com");
INSERT INTO Author VALUES (1902,"Gareth","Owen","British",NULL,"www.garethowen.com");
INSERT INTO Author VALUES (2002,"Eric","Carle","American","1929-06-25","www.eric-carle.com");
INSERT INTO Author VALUES (2715,"Jon","Blake","British",NULL,"jonblakeblog.wordpress.com");
INSERT INTO Author VALUES (2864,"Kenneth","Oppel","Canadian","1967-08-31","www.kennethoppel.ca");
INSERT INTO Author VALUES (3197,"Joanne","Rowling","British","1965-07-31","www.jkrowling.com");
INSERT INTO Author VALUES (3390,"Patricia","Cornwell","American","1956-06-09","www.patriciacornwell.com");
INSERT INTO Author VALUES (3507,"Nick","Hunter","British",NULL,NULL);
INSERT INTO Author VALUES (3713,"Mick","Inkpen","British",NULL,NULL);
INSERT INTO Author VALUES (4079,"Jack","Higgins","British","1929-07-27",NULL);
INSERT INTO Author VALUES (4097,"Mary","Berry","British","1935-03-24",NULL);
INSERT INTO Author VALUES (4231,"Nicholas","Evans","British","1950-07-26","www.nicholasevens.com");
