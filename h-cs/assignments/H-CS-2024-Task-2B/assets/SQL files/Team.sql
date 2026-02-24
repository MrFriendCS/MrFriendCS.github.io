CREATE TABLE Team (
    teamRef VARCHAR(255) NOT NULL,
    teamName VARCHAR(255) NOT NULL,
    headCoach VARCHAR(255) NOT NULL,
    assistantCoach VARCHAR(255) NOT NULL,
    PRIMARY KEY (teamRef)
);


INSERT INTO Team VALUES("ENG","England","Jordan Walker","Francis Carroll");
INSERT INTO Team VALUES("NIR","Northern Ireland","Alex McCarthy","Adrian Thompson");
INSERT INTO Team VALUES("SCO","Scotland","Devon Jackson","Blake Shearer");
INSERT INTO Team VALUES("WAL","Wales","Jaden Wilson","Benny Fitzgerald");
