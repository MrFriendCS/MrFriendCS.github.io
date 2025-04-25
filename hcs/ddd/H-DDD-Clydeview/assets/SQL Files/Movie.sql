CREATE TABLE Movie (
    movieID INT NOT NULL,
    title VARCHAR(30) NOT NULL,
    director VARCHAR(30),
    yearReleased INT NOT NULL
        CHECK(yearReleased >= 1900
          AND yearReleased <= 2030),
    durationsMins INT NOT NULL
        CHECK(durationsMins >= 0),
    PRIMARY KEY (movieID)
);

INSERT INTO Movie VALUES (1,"Toy Story","John Lasseter",1995,81);
INSERT INTO Movie VALUES (2,"A Bug's Life","John Lasseter",1998,95);
INSERT INTO Movie VALUES (3,"Toy Story 2","John Lasseter",1999,93);
INSERT INTO Movie VALUES (4,"Monsters Inc.","Pete Docter",2001,92);
INSERT INTO Movie VALUES (5,"Finding Nemo","Andrew Stanton",2003,107);
INSERT INTO Movie VALUES (6,"The Incredibles","Brad Bird",2004,116);
INSERT INTO Movie VALUES (7,"Cars","John Lasseter",2006,117);
INSERT INTO Movie VALUES (8,"Ratatouille","Brad Bird",2007,115);
INSERT INTO Movie VALUES (9,"WALL-E","Andrew Stanton",2008,104);
INSERT INTO Movie VALUES (10,"Up","Pete Docter",2009,101);
INSERT INTO Movie VALUES (11,"Toy Story 3","Lee Unkrich",2010,103);
INSERT INTO Movie VALUES (12,"Cars 2","John Lasseter",2011,120);
INSERT INTO Movie VALUES (13,"Brave","Brenda Chapman",2012,102);
INSERT INTO Movie VALUES (14,"Monsters University","Dan Scanlon",2013,110);
