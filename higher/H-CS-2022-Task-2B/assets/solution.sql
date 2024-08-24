-- Don't change lines 1 to 5
.open WestFifeWalkers.db
.headers on
.mode column
-- Don't change lines 1 to 5

.print H CS 2022 Task 2B

.print
.print Q2b
SELECT forename, surname, Planner.plannerNo,
        COUNT(walkID) AS [Total participants]
    FROM Planner, Route, Walk
    WHERE Planner.plannerNo = Route.plannerNo
        AND Route.routeID = Walk.routeID
    GROUP BY forename, surname, Planner.plannerNo
    ORDER BY [Total participants] DESC;


.print
.print Q2c
CREATE TEMP VIEW longest (maxDistance) AS
    SELECT MAX(distance)
    FROM Route;

.print

SELECT Walker.walkerNo, forename, surname, telNo
    FROM Walker, Walk, Route, longest
    WHERE Walker.walkerNo = Walk.walkerNo
        AND Walk.routeID = Route.routeID
        AND distance = maxDistance
    GROUP BY Walker.walkerNo, Walker.forename,
        Walker.surname, Walker.telNo;


.print
.print Q2d

SELECT Route.routeID, woodName, description 
    FROM Route 
    WHERE footwear = "Trail shoes" 
        OR footwear = "Waterproof shoes" 
        OR footwear = "Walking shoes";

.print

SELECT Route.routeID, woodName, description 
    FROM Route 
    WHERE footwear LIKE "%shoes";


.print