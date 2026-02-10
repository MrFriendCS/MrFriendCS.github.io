/*
.open Vlogger.db
.headers on
.mode column
PRAGMA foreign_keys = on;
*/


/*
Title: N5 CS 2019 Task 1 Part C
Author: Mr Friend
Date: 25 Nov 2023
*/


-- Q1c(i) - Advertise best videos
SELECT username, videoName
    FROM Vlogger, Video
    WHERE Vlogger.vloggerID = Video.vloggerID
        AND rating > 3;


-- Q1c(ii) - Delete 'Slime' video
DELETE FROM Video
    WHERE videoID = 3;

-- Q1c(ii) - Evidence
SELECT *
    FROM Video;


   

/*
Not required to answer assignment questions.
Used to revert database back to start state.
*/


-- Q1c(ii) - Add 'Slime' movie
INSERT INTO Video
    VALUES (3,10,"Slime",45,"2020-05-15","Make slime",1);
