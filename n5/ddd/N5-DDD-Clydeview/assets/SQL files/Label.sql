CREATE TABLE Label (
    label VARCHAR(20) NOT NULL,
    founded INT NOT NULL,
    parentCompany VARCHAR(30),
    countryOfOrigin VARCHAR(7) NOT NULL 
        CHECK (countryOfOrigin IN ("Germany", "Japan", "UK", "USA")),
    website VARCHAR(50),
    PRIMARY KEY (label)
);

INSERT INTO Label VALUES ("Atlantic Records","1947","Warner Music Group","USA","www.atlanticrecords.com");
INSERT INTO Label VALUES ("Blix Street","2006","","USA","www.blixstreet.com");
INSERT INTO Label VALUES ("Decca Records","1929","Universal Music Group","UK","www.decca.com");
INSERT INTO Label VALUES ("Epic Records","1953","Sony Music","USA","www.epicrecords.com");
INSERT INTO Label VALUES ("Mercury Records","1945","Universal Music Group","UK","www.mercuryclassics.com");
INSERT INTO Label VALUES ("Polydor Records","1924","Universal Music Group","Germany","www.polydor.co.uk");
INSERT INTO Label VALUES ("Syco Music","2002","Syco Music","UK","www.sycoentertainment.com");
INSERT INTO Label VALUES ("Virgin Records","1973","Universal Music Group","USA","www.virginrecords.com");
INSERT INTO Label VALUES ("Warner Bros","1958","Warner Music Group","Japan","www.warnerbrosrecords.com");
