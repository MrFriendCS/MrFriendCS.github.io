CREATE TABLE Datatypes ( 
        rowID INT NOT NULL,
        colour VARCHAR(10) 
            CHECK(LENGTH(colour) >= 3),
        score INT 
            CHECK(score >= 0 AND score <= 100),
        height FLOAT NOT NULL 
            CHECK(height >= 1.0 
              AND height <= 2.5),
        dob DATE 
            CHECK(dob >= "1900-01-01" 
              AND dob <= "2024-12-31"),
        start TIME 
            CHECK(start >= "08:00:00" 
              AND start <= "16:00:00"),
        nice BOOLEAN NOT NULL,
        PRIMARY KEY (rowID)
    );

INSERT INTO Datatypes VALUES (1,"Red",96,1.12,"1947-03-29","10:33:49",0);
INSERT INTO Datatypes VALUES (2,"Orange",26,2.01,"1949-02-08","09:28:28",0);
INSERT INTO Datatypes VALUES (3,"Green",25,1.61,"1988-02-26","14:03:17",1);
INSERT INTO Datatypes VALUES (4,"Turquoise",95,1.97,"1926-02-04","14:41:17",1);
INSERT INTO Datatypes VALUES (5,"Yellow",47,2.09,"1990-07-12","11:47:14",1);
INSERT INTO Datatypes VALUES (6,"Yellow",10,1.26,"1974-08-14","12:30:42",0);
INSERT INTO Datatypes VALUES (7,"Indigo",59,1.78,"1929-01-13","13:44:46",1);
INSERT INTO Datatypes VALUES (8,"Pink",97,1.88,"1913-12-06","13:04:51",1);
INSERT INTO Datatypes VALUES (9,"Maroon",53,2.04,"1915-09-04","14:49:14",1);
INSERT INTO Datatypes VALUES (10,"Puce",97,1.05,"1912-08-04","11:58:48",1);
INSERT INTO Datatypes VALUES (11,"Crimson",22,1.7,"1951-10-16","14:26:17",0);
INSERT INTO Datatypes VALUES (12,"Purple",72,1.67,"1962-12-19","12:15:54",1);
INSERT INTO Datatypes VALUES (13,"Violet",1,1.4,"1933-06-01","12:22:22",1);
INSERT INTO Datatypes VALUES (14,"Maroon",13,1.87,"1968-01-22","11:00:01",0);
INSERT INTO Datatypes VALUES (15,"Mauv",26,1.73,"2020-04-04","15:00:46",0);
INSERT INTO Datatypes VALUES (16,"Maroon",51,1.94,"1945-02-18","15:59:34",1);
INSERT INTO Datatypes VALUES (17,"Turquoise",4,2.48,"1973-11-03","09:22:03",1);
INSERT INTO Datatypes VALUES (18,"Orange",28,1.9,"1954-03-28","12:33:04",1);
INSERT INTO Datatypes VALUES (19,"Orange",85,2.09,"1902-09-18","11:31:51",1);
INSERT INTO Datatypes VALUES (20,"Yellow",87,1.52,"1929-05-19","15:14:14",0);
INSERT INTO Datatypes VALUES (21,"Violet",16,1.63,"1914-06-12","14:00:15",0);
INSERT INTO Datatypes VALUES (22,"Blue",89,1.42,"2010-01-12","09:42:51",0);
INSERT INTO Datatypes VALUES (23,"Blue",71,1.59,"2018-06-06","13:34:34",0);
INSERT INTO Datatypes VALUES (24,"Green",61,2.03,"2005-07-26","10:56:27",0);
INSERT INTO Datatypes VALUES (25,"Maroon",41,1.1,"1952-06-04","11:13:07",1);
INSERT INTO Datatypes VALUES (26,"Mauv",87,1.65,"1936-12-15","09:35:08",1);
INSERT INTO Datatypes VALUES (27,"Violet",20,2.01,"1931-10-09","12:03:21",1);
INSERT INTO Datatypes VALUES (28,"Crimson",94,1.43,"1918-12-23","08:03:49",1);
INSERT INTO Datatypes VALUES (29,"Blue",4,2.24,"2024-06-17","12:41:16",1);
INSERT INTO Datatypes VALUES (30,"Mauv",64,1.25,"1988-08-21","14:32:30",1);
INSERT INTO Datatypes VALUES (31,"Fuscia",62,1.35,"1986-06-26","15:05:26",0);
INSERT INTO Datatypes VALUES (32,"Yellow",84,1.25,"1910-03-08","08:50:14",0);
INSERT INTO Datatypes VALUES (33,"Goldenred",42,1.04,"1917-11-27","12:36:04",1);
INSERT INTO Datatypes VALUES (34,"Yellow",18,1.46,"2004-10-15","08:11:51",1);
INSERT INTO Datatypes VALUES (35,"Fuscia",36,1.67,"1928-06-02","08:02:07",1);
INSERT INTO Datatypes VALUES (36,"Fuscia",57,1.32,"1983-07-23","15:18:13",1);
INSERT INTO Datatypes VALUES (37,"Puce",93,2.18,"2007-09-17","10:45:07",1);
INSERT INTO Datatypes VALUES (38,"Purple",32,1.71,"1981-09-01","11:53:26",1);
INSERT INTO Datatypes VALUES (39,"Teal",25,1.88,"1915-03-07","09:38:11",1);
INSERT INTO Datatypes VALUES (40,"Puce",76,1.72,"1960-07-08","15:52:25",0);
INSERT INTO Datatypes VALUES (41,"Turquoise",76,1.2,"1983-08-03","08:56:24",1);
INSERT INTO Datatypes VALUES (42,"Purple",54,1.87,"1986-06-25","12:39:22",0);
INSERT INTO Datatypes VALUES (43,"Orange",53,1.62,"2009-03-22","11:47:40",1);
INSERT INTO Datatypes VALUES (44,"Violet",58,2.23,"1907-12-21","14:39:00",0);
INSERT INTO Datatypes VALUES (45,"Pink",41,2.02,"1903-03-01","08:52:44",1);
INSERT INTO Datatypes VALUES (46,"Blue",89,1.17,"2000-12-04","13:23:07",1);
INSERT INTO Datatypes VALUES (47,"Green",12,1.39,"1995-10-03","14:08:44",1);
INSERT INTO Datatypes VALUES (48,"Violet",85,2.37,"1902-02-15","12:31:01",1);
INSERT INTO Datatypes VALUES (49,"Violet",14,1.87,"1953-10-12","13:46:34",1);
INSERT INTO Datatypes VALUES (50,"Fuscia",6,2.09,"2018-12-02","15:59:18",1);
