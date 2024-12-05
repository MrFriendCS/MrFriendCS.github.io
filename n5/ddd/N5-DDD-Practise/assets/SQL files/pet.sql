CREATE TABLE Pet (
    name VARCHAR(20) NOT NULL,
    type VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    insurer INT NOT NULL,
    PRIMARY KEY (name),
    FOREIGN KEY (insurer)
        REFERENCES Insurer (id)
);

INSERT INTO Pet VALUES ("Pepper","Cat",16,0);
INSERT INTO Pet VALUES ("Cindy","Dog",4,2);
INSERT INTO Pet VALUES ("Snowy","Cat",7,1);
INSERT INTO Pet VALUES ("Micky","Mouse",1,2);
INSERT INTO Pet VALUES ("Minnie","Mouse",1,0);
INSERT INTO Pet VALUES ("Kitty","Cat",9,1);
INSERT INTO Pet VALUES ("Bonzo","Dog",6,2);
INSERT INTO Pet VALUES ("Roger","Rabbit",3,0);
