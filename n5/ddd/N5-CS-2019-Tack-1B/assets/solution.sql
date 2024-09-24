-- Don't touch lines 1 to 5
.open Vlogger.db
.headers on
.mode column
-- Don't touch lines 1 to 5

.print N5 CS 2019 Task 1C

.print
.print Q1c(i)
SELECT username, videoName
FROM Vlogger, Video
WHERE Vlogger.vloggerID = Video.vloggerID
AND rating > 3;


.print
.print Q1c(ii)
DELETE FROM Video
WHERE videoID = 3;


