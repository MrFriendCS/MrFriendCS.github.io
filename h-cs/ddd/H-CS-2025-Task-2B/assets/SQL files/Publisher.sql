CREATE TABLE Publisher (
    publisherID INT NOT NULL,
    publisherName VARCHAR(30) NOT NULL,
    foundedYear INT NOT NULL,
    headquarters VARCHAR(10) NOT NULL,
    PRIMARY KEY (publisherID)
);

INSERT INTO Publisher VALUES (1,"Epic Doddles",1960,"America");
INSERT INTO Publisher VALUES (2,"Kapow Publications",1962,"America");
INSERT INTO Publisher VALUES (3,"Heroic Inklings",1967,"UK");
INSERT INTO Publisher VALUES (4,"Panel Pals",1973,"Australia");
