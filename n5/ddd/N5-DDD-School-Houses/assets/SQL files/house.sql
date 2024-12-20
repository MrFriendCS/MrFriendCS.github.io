CREATE TABLE House (
    id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    guidanceTeacher VARCHAR(30),
    emblem VARCHAR(10) NOT NULL,
    colour VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO House VALUES (1,"Gryffindor","Prof McGonagall","Lion","Scarlett and Gold");
INSERT INTO House VALUES (2,"Hufflepuff","Prof Sprout","Badger","Yellow and Black");
INSERT INTO House VALUES (3,"Ravenclaw","Prof Flitwick","Eagle","Blue and Bronze");
INSERT INTO House VALUES (4,"Slytherin","Prof Snape","Snake","Green and Silver");
