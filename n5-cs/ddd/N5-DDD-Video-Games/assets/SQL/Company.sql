CREATE TABLE Company ( 
    name VARCHAR(20) NOT NULL,
    country VARCHAR(20) NOT NULL,
    founded DATE NOT NULL 
        CHECK (founded >= "1970-01-01"),
    website VARCHAR(30),
    profit INT NOT NULL,
    PRIMARY KEY (name)
);

INSERT INTO Company VALUES ("Eaglehead Software","USA","1991-01-01","www.eagleheadsoft.com",234000);
INSERT INTO Company VALUES ("Elite","UK","1998-04-21","www.elite_games.co.uk",287000);
INSERT INTO Company VALUES ("Station Games","UK","1990-03-03","www.stationgames.com",414000);
INSERT INTO Company VALUES ("StudioArts","USA","1993-01-03","www.starts.com",1071000);
INSERT INTO Company VALUES ("TB Games","UK","1995-07-06","www.tb-games.co.uk",1294000);
INSERT INTO Company VALUES ("Victory","USA","1991-03-02","www.victory-soft.com",1454000);
