CREATE TABLE Video (
    videoID INT NOT NULL,
    vloggerID INT NOT NULL,
    videoName VARCHAR(30) NOT NULL,
    duration INT NOT NULL,
    dateCreated DATE NOT NULL,
    content VARCHAR(40) NOT NULL,
    rating INT NOT NULL
        CHECK (rating >= 1
          AND  rating <= 5),
    PRIMARY KEY (videoID),
    FOREIGN KEY (vloggerID)
        REFERENCES Vlogger (vloggerID)
);

INSERT INTO Video VALUES (1,7,"C++",60,"2017-12-30","Lesson 1 Learn about C++",1);
INSERT INTO Video VALUES (2,9,"Java",30,"2019-11-12","Learn Java in 24 hours",4);
INSERT INTO Video VALUES (3,10,"Slime",45,"2020-05-15","Make slime",1);
INSERT INTO Video VALUES (4,10,"Slime",12,"2020-04-25","Glitter Slime",5);
INSERT INTO Video VALUES (5,7,"Lego",8,"2019-01-24","Mission 1",5);
INSERT INTO Video VALUES (6,3,"COD",180,"2018-05-27","History of COD",2);
INSERT INTO Video VALUES (7,6,"Eye Shadow",35,"2019-02-14","Eye shadow tutorial",3);
INSERT INTO Video VALUES (8,12,"Christmas Decorations",0,"2019-12-01","Snowmen",4);
INSERT INTO Video VALUES (9,15,"Microbits",180,"2019-09-02","Programming for kids",2);
INSERT INTO Video VALUES (10,8,"Jeans",240,"2019-06-18","Jeans for all",3);
