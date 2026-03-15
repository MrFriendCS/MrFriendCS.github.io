CREATE TABLE CD (
    code VARCHAR(4) NOT NULL 
        CHECK(LENGTH(code) = 4),
    title VARCHAR(40) NOT NULL,
    artist VARCHAR(40) NOT NULL,
    label VARCHAR(20) NOT NULL,
    tracks INT 
        CHECK (tracks >= 10 
           AND tracks <= 60),
    cost REAL NOT NULL 
        CHECK(cost >= 6.99 
          AND cost <= 15.00),
    genre VARCHAR(20) NOT NULL
        CHECK (genre IN ("Choral", "Country", "Garage", "Indie", 
                         "Opera", "Pop", "R&B", "R&R", "Soul")),
    FOREIGN KEY (label)
        REFERENCES Label(label),
    PRIMARY KEY (code)
);

INSERT INTO CD VALUES ("42AM","The Best of","Eva Cassidy","Blix Street",20,9.99,"Pop");
INSERT INTO CD VALUES ("5J8Y","+","Ed Sheeran","Atlantic Records",13,10.00,"Indie");
INSERT INTO CD VALUES ("61DS","Stronger Together","Military Wives","Decca Records",14,7.49,"Choral");
INSERT INTO CD VALUES ("82FK","The Power of Love","Sam Bailey","Syco Music",11,7.50,"Soul");
INSERT INTO CD VALUES ("8G9K","iDos!","Greenday","Warner Bros",13,8.99,"Garage");
INSERT INTO CD VALUES ("8PL3","Opera","Andrea Bocelli","Decca Records",21,10.00,"Opera");
INSERT INTO CD VALUES ("8QGC","Our Version of Events","Emeli Sande","Virgin Records",19,8.99,"R&B");
INSERT INTO CD VALUES ("91TU","Right Place Right Time","Olly Murs","Epic Records",12,11.99,"Pop");
INSERT INTO CD VALUES ("942Y","Take Me Home","One Direction","Syco Music",13,10.00,"Pop");
INSERT INTO CD VALUES ("95VW","Grrr","The Rolling Stones","Polydor Records",51,11.99,"R&R");
INSERT INTO CD VALUES ("97F2","Red","Taylor Swift","Mercury Records",16,8.99,"Country");
INSERT INTO CD VALUES ("9KYX","Glory Days","Little Mix","Syco Music",20,9.99,"R&B");
