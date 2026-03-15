CREATE TABLE Station (
    id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    postcode VARCHAR(8) NOT NULL, 
    motorway BOOL
        CHECK (motorway = 0 OR motorway = 1),
    supermarket BOOL
        CHECK (supermarket = 0 OR supermarket = 1),
    latitude REAL,
    longitude REAL,
    e5 REAL,
    e10 REAL,
    b7s REAL,
    b7p REAL,
    open TIME
        CHECK (open LIKE "__:__:__"),
    close TIME
        CHECK (close LIKE "__:__:__"),
    openSun TIME
        CHECK (openSun LIKE "__:__:__"),
    closeSun TIME
        CHECK (closeSun LIKE "__:__:__"),
    carWash BOOL
        CHECK (carWash = 0 OR carWash = 1),
    toilets BOOL
        CHECK (toilets = 0 OR toilets = 1),
    PRIMARY KEY (id)
);
