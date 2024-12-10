CREATE TABLE Datatypes ( 
        rowID INT NOT NULL,
        colour VARCHAR(10) 
            CHECK (LENGTH(colour) >= 3),
        score INT 
            CHECK (score >= 0 
			   AND score <= 100),
        height FLOAT 
            CHECK (height >= 1.0 
               AND height <= 2.5),
        dob DATE 
            CHECK (dob >= "1900-01-01" 
               AND dob <= "2024-12-31"),
        start TIME 
            CHECK (start >= "08:00:00" 
               AND start <= "16:00:00"),
        nice BOOLEAN NOT NULL,
        PRIMARY KEY (rowID)
    );

INSERT INTO Datatypes VALUES (1,"Violet",5,2.38,"2005-07-30","10:36:37",0);
INSERT INTO Datatypes VALUES (2,"Fuscia",91,1.98,"1958-08-30","11:58:40",0);
INSERT INTO Datatypes VALUES (3,"Violet",60,2.17,"1958-09-05","11:08:01",1);
INSERT INTO Datatypes VALUES (4,"Blue",25,2.35,"1992-12-04","13:09:45",1);
INSERT INTO Datatypes VALUES (5,"Indigo",58,2.44,"1965-08-24","13:32:27",0);
INSERT INTO Datatypes VALUES (6,"Crimson",90,1.55,"1971-10-09","15:51:58",1);
INSERT INTO Datatypes VALUES (7,"Goldenred",63,1.96,"1958-05-25","15:04:16",1);
INSERT INTO Datatypes VALUES (8,"Goldenred",85,2.3,"1910-01-21","13:52:18",1);
INSERT INTO Datatypes VALUES (9,"Indigo",29,2.12,"1970-02-11","10:53:43",1);
INSERT INTO Datatypes VALUES (10,"Aquamarine",44,1.35,"1957-10-05","09:08:37",0);
INSERT INTO Datatypes VALUES (11,"Orange",10,1.29,"1912-10-06","08:29:19",1);
INSERT INTO Datatypes VALUES (12,"Pink",25,2.04,"1954-04-03","08:29:35",1);
INSERT INTO Datatypes VALUES (13,"Green",88,1.17,"1950-07-05","12:08:26",0);
INSERT INTO Datatypes VALUES (14,"Blue",40,1.53,"2017-10-18","09:38:33",1);
INSERT INTO Datatypes VALUES (15,"Green",69,2.23,"1941-03-08","15:59:51",1);
INSERT INTO Datatypes VALUES (16,"Maroon",78,2.07,"1993-06-23","09:57:03",0);
INSERT INTO Datatypes VALUES (17,"Violet",3,1.35,"1925-11-01","08:49:25",1);
INSERT INTO Datatypes VALUES (18,"Blue",20,2.06,"1910-06-14","11:51:09",1);
INSERT INTO Datatypes VALUES (19,"Fuscia",69,1.18,"1943-02-01","09:55:15",1);
INSERT INTO Datatypes VALUES (20,"Aquamarine",20,1.12,"1987-02-27","15:51:02",1);
INSERT INTO Datatypes VALUES (21,"Fuscia",97,2.36,"1962-03-11","13:32:28",1);
INSERT INTO Datatypes VALUES (22,"Blue",25,2.02,"1999-09-30","12:25:08",1);
INSERT INTO Datatypes VALUES (23,"Purple",22,1.56,"1990-09-18","12:55:14",1);
INSERT INTO Datatypes VALUES (24,"Khake",1,2.3,"1968-11-02","15:19:55",0);
INSERT INTO Datatypes VALUES (25,"Violet",49,1.02,"1942-08-06","12:25:30",0);
INSERT INTO Datatypes VALUES (26,"Turquoise",99,2.24,"2008-11-15","13:28:00",1);
INSERT INTO Datatypes VALUES (27,"Green",15,1.17,"1969-08-23","09:50:07",1);
INSERT INTO Datatypes VALUES (28,"Turquoise",34,1.77,"1959-11-12","13:15:33",1);
INSERT INTO Datatypes VALUES (29,"Turquoise",69,1.43,"1900-01-07","09:05:21",1);
INSERT INTO Datatypes VALUES (30,"Turquoise",57,1.77,"1954-09-22","10:07:55",1);
INSERT INTO Datatypes VALUES (31,"Mauv",30,1.39,"1906-07-05","10:38:55",1);
INSERT INTO Datatypes VALUES (32,"Blue",61,1.96,"1918-03-03","15:08:04",1);
INSERT INTO Datatypes VALUES (33,"Teal",74,1.43,"1953-06-03","11:33:19",1);
INSERT INTO Datatypes VALUES (34,"Fuscia",92,1.2,"1915-03-26","13:59:56",1);
INSERT INTO Datatypes VALUES (35,"Khake",52,2.31,"1919-04-23","08:44:21",1);
INSERT INTO Datatypes VALUES (36,"Violet",48,1.25,"2011-03-03","10:57:09",1);
INSERT INTO Datatypes VALUES (37,"Maroon",93,1.59,"2016-06-07","12:00:13",0);
INSERT INTO Datatypes VALUES (38,"Fuscia",69,2.46,"2003-10-20","12:37:47",0);
INSERT INTO Datatypes VALUES (39,"Puce",100,1.6,"1996-05-03","12:56:37",0);
INSERT INTO Datatypes VALUES (40,"Orange",42,1.57,"2008-01-11","08:27:47",0);
INSERT INTO Datatypes VALUES (41,"Puce",73,1.52,"1941-12-25","13:42:32",0);
INSERT INTO Datatypes VALUES (42,"Goldenred",37,1.06,"2016-11-29","14:32:35",0);
INSERT INTO Datatypes VALUES (43,"Orange",83,1.57,"1990-03-01","08:57:29",0);
INSERT INTO Datatypes VALUES (44,"Goldenred",63,1.09,"1993-03-14","14:39:04",1);
INSERT INTO Datatypes VALUES (45,"Yellow",37,2.03,"2013-09-08","12:33:59",1);
INSERT INTO Datatypes VALUES (46,"Turquoise",82,2.17,"2024-11-13","12:47:49",1);
INSERT INTO Datatypes VALUES (47,"Orange",25,1.47,"1951-09-21","09:25:33",1);
INSERT INTO Datatypes VALUES (48,"Pink",37,1.97,"2015-10-29","11:20:11",1);
INSERT INTO Datatypes VALUES (49,"Goldenred",18,2.0,"1964-05-26","09:35:37",1);
INSERT INTO Datatypes VALUES (50,"Pink",48,1.71,"1903-09-19","15:34:51",1);
