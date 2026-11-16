-- Title: N5 CS 2019 Task 1 Part C
-- Author: Mr Friend
-- Date: 25 Nov 2023


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
