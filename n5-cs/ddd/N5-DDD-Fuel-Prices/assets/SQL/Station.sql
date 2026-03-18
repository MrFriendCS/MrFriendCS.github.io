CREATE TABLE Station (
    id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    postcode VARCHAR(8) NOT NULL
        CHECK (LENGTH(postcode) >= 5), 
    motorway BOOL
        CHECK (motorway IN (0,1)),
    supermarket BOOL
        CHECK (supermarket IN (0,1)),
    latitude REAL,
    longitude REAL,
    e5 REAL
        CHECK (e5 >= 0.0),
    e10 REAL
        CHECK (e10 >= 0.0),
    b7s REAL
        CHECK (b7s >= 0.0),
    b7p REAL
        CHECK (b7p >= 0.0),
    open TIME
        CHECK (open LIKE "__:__:__"),
    close TIME
        CHECK (close LIKE "__:__:__"),
    openSun TIME
        CHECK (openSun LIKE "__:__:__"),
    closeSun TIME
        CHECK (closeSun LIKE "__:__:__"),
    carWash BOOL
        CHECK (carWash IN (0,1)),
    toilets BOOL
        CHECK (toilets IN (0,1)),
    PRIMARY KEY (id)
);
