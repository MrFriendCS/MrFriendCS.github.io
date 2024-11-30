CREATE TABLE datatypes (
    row_id INT NOT NULL UNIQUE,
    colour VARCHAR(10)
        CHECK(LENGTH(colour) >= 3),
    score INT
        CHECK(score >= 0 AND score <= 100),
    height FLOAT NOT NULL
        CHECK(height >= 1.0 AND height <= 2.5),
    dob DATE
        CHECK(dob >= "1900-01-01" AND dob <= "2024-12-31"),
    start TIME
        CHECK(start >= "08:00:00" AND start <= "16:00:00"),
    nice BOOLEAN NOT NULL,
    PRIMARY KEY (row_id)
);

INSERT INTO datatypes VALUES (1,"Yellow",23,1.41,"1984-02-12","11:37:25",1);
INSERT INTO datatypes VALUES (2,"Green",97,1.23,"1909-11-20","15:54:45",1);
INSERT INTO datatypes VALUES (3,"Pink",40,1.84,"1997-04-12","15:32:23",1);
INSERT INTO datatypes VALUES (4,"Violet",96,1.89,"2014-01-16","09:14:41",0);
INSERT INTO datatypes VALUES (5,"Purple",3,2.36,"1975-10-14","11:55:06",1);
INSERT INTO datatypes VALUES (6,"Purple",51,1.97,"2022-04-11","11:33:55",0);
INSERT INTO datatypes VALUES (7,"Khake",40,1.03,"1993-02-11","14:52:02",1);
INSERT INTO datatypes VALUES (8,"Orange",92,1.69,"1945-02-11","15:33:34",0);
INSERT INTO datatypes VALUES (9,"Mauv",53,1.96,"1967-09-01","10:35:38",1);
INSERT INTO datatypes VALUES (10,"Pink",57,1.79,"1920-11-09","14:12:07",1);
INSERT INTO datatypes VALUES (11,"Red",99,1.85,"1939-04-02","08:17:09",1);
INSERT INTO datatypes VALUES (12,"Mauv",28,1.42,"1922-04-21","09:08:21",1);
INSERT INTO datatypes VALUES (13,"Goldenred",4,2.13,"1996-06-20","08:45:45",1);
INSERT INTO datatypes VALUES (14,"Blue",97,1.9,"1926-09-19","09:48:15",0);
INSERT INTO datatypes VALUES (15,"Red",86,1.21,"1924-05-21","10:54:03",1);
INSERT INTO datatypes VALUES (16,"Red",47,1.49,"1970-12-06","13:04:45",1);
INSERT INTO datatypes VALUES (17,"Aquamarine",65,1.72,"1916-12-28","12:06:33",0);
INSERT INTO datatypes VALUES (18,"Goldenred",73,1.84,"1983-07-25","12:54:45",1);
INSERT INTO datatypes VALUES (19,"Fuscia",80,1.65,"1943-10-03","08:05:46",1);
INSERT INTO datatypes VALUES (20,"Teal",63,2.2,"1974-06-13","14:35:35",0);
INSERT INTO datatypes VALUES (21,"Green",63,2.35,"1950-05-09","13:54:13",0);
INSERT INTO datatypes VALUES (22,"Orange",61,1.12,"1910-10-25","10:19:08",0);
INSERT INTO datatypes VALUES (23,"Indigo",20,1.98,"1923-02-11","10:02:28",0);
INSERT INTO datatypes VALUES (24,"Mauv",66,1.36,"1933-08-19","11:35:29",0);
INSERT INTO datatypes VALUES (25,"Crimson",86,1.04,"1925-03-29","13:55:13",1);
INSERT INTO datatypes VALUES (26,"Yellow",70,1.51,"1943-01-15","10:59:29",1);
INSERT INTO datatypes VALUES (27,"Crimson",27,1.68,"1972-08-28","12:50:30",1);
INSERT INTO datatypes VALUES (28,"Yellow",59,1.34,"1903-07-11","10:57:31",0);
INSERT INTO datatypes VALUES (29,"Purple",59,2.28,"1940-07-02","11:13:35",0);
INSERT INTO datatypes VALUES (30,"Pink",39,2.4,"2023-04-24","14:21:58",0);
INSERT INTO datatypes VALUES (31,"Puce",56,1.98,"1916-07-13","13:14:33",0);
INSERT INTO datatypes VALUES (32,"Blue",15,2.36,"2011-06-04","14:55:30",1);
INSERT INTO datatypes VALUES (33,"Blue",28,1.24,"1976-12-21","12:13:05",1);
INSERT INTO datatypes VALUES (34,"Green",55,2.0,"1951-07-20","08:36:22",1);
INSERT INTO datatypes VALUES (35,"Aquamarine",29,1.92,"1967-08-22","14:53:46",1);
INSERT INTO datatypes VALUES (36,"Aquamarine",6,1.5,"1960-08-18","13:59:55",1);
INSERT INTO datatypes VALUES (37,"Aquamarine",56,1.48,"1956-08-29","10:05:32",0);
INSERT INTO datatypes VALUES (38,"Red",62,1.97,"1947-05-27","10:10:20",1);
INSERT INTO datatypes VALUES (39,"Violet",37,2.15,"1952-07-19","09:24:54",0);
INSERT INTO datatypes VALUES (40,"Orange",50,1.01,"2000-06-05","11:31:36",1);
INSERT INTO datatypes VALUES (41,"Fuscia",21,2.36,"1972-03-23","11:40:05",1);
INSERT INTO datatypes VALUES (42,"Puce",83,1.09,"2008-04-10","08:44:59",1);
INSERT INTO datatypes VALUES (43,"Blue",56,1.54,"2024-06-29","09:46:31",0);
INSERT INTO datatypes VALUES (44,"Mauv",62,1.3,"1922-10-12","12:48:48",1);
INSERT INTO datatypes VALUES (45,"Fuscia",54,1.75,"1921-03-23","08:58:02",0);
INSERT INTO datatypes VALUES (46,"Turquoise",68,2.38,"1939-02-17","15:44:54",0);
INSERT INTO datatypes VALUES (47,"Red",1,1.35,"2018-02-28","09:33:44",1);
INSERT INTO datatypes VALUES (48,"Green",83,2.36,"1925-04-04","12:14:20",0);
INSERT INTO datatypes VALUES (49,"Blue",50,1.36,"1962-08-30","14:48:24",1);
INSERT INTO datatypes VALUES (50,"Aquamarine",89,1.16,"1912-04-22","10:37:11",1);
