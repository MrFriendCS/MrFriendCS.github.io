CREATE TABLE Book (
    category VARCHAR(5) NOT NULL 
        CHECK (category IN ("Adult", "Child")),
    genre VARCHAR(13) NOT NULL 
        CHECK (genre IN ("Joke", "Sport", "Fiction", "Fantasy",
                         "Thriller", "Autobiography", "Mystery")),
    title VARCHAR(100) NOT NULL,
    authorRef INT NOT NULL,
    publisher VARCHAR(30) NOT NULL,
    ISBN VARCHAR(10) NOT NULL 
        CHECK (LENGTH(ISBN) = 10),
    dateOfPublication DATE,
    numberOfPages INT NOT NULL 
        CHECK(numberOfPages >=26 
          AND numberOfPages <= 950),
    FOREIGN KEY (authorRef) 
        REFERENCES Author (authorRef),
    PRIMARY KEY (title)
);

INSERT INTO Book VALUES ("Child","Fantasy","Galactic Snapshots","2864","Puffin","0140373683","2010-08-03",96);
INSERT INTO Book VALUES ("Child","Mystery","Harry Potter and the Chamber of Secrets","3197","Bloomsbury","0747538492","1998-07-02",251);
INSERT INTO Book VALUES ("Child","Sport","London Olympics 2012","3507","Raintree","1406223948","2011-07-05",32);
INSERT INTO Book VALUES ("Adult","Thriller","Point of Origin","3390","Sphere","0751544787","2009-08-23",400);
INSERT INTO Book VALUES ("Adult","Autobiography","Recipe for Life","4097","Penguin","1405912855","2014-02-27",432);
INSERT INTO Book VALUES ("Child","Fiction","Roboskool","2715","Puffin","0140363240","2005-03-12",79);
INSERT INTO Book VALUES ("Child","Joke","Say Cheese","1902","Corgi","0552529753","1996-11-07",64);
INSERT INTO Book VALUES ("Adult","Fiction","The Casual Vacancy","3197","Little Brown Company","0751552860","2012-09-27",503);
INSERT INTO Book VALUES ("Adult","Fiction","The Horse Whisperer","4231","Sphere","0751539368","2006-08-10",448);
INSERT INTO Book VALUES ("Adult","Mystery","The President's Daughter","3846","Penguin","o140269061","2011-11-14",400);
INSERT INTO Book VALUES ("Child","Fiction","The Very Hungry Caterpillar","2002","Puffin","2067152998","1990-09-29",26);
INSERT INTO Book VALUES ("Child","Fiction","Threadbear","3713","Hodder and Stoughton","0340531290","2007-07-05",32);