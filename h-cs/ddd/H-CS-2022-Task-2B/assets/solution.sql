-- Title: H CS 2022 Task 2 Part B
-- Author: Mr Friend
-- Date: 22 Feb 2025

-- Q2b
SELECT forename, surname, Planner.plannerNo,
       COUNT(walkID) AS [Total participants]
    FROM Planner, Route, Walk
    WHERE Planner.plannerNo = Route.plannerNo
      AND Route.routeID = Walk.routeID
    GROUP BY forename, surname, Planner.plannerNo
    ORDER BY [Total participants] DESC;


-- Q2c
-- Find longest
CREATE TEMP VIEW longest (maxDistance) AS
    SELECT MAX(distance)
    FROM Route;

-- Use most longest
SELECT Walker.walkerNo, forename, surname, telNo
    FROM Walker, Walk, Route, longest
    WHERE Walker.walkerNo = Walk.walkerNo
      AND Walk.routeID = Route.routeID
      AND distance = maxDistance
    GROUP BY Walker.walkerNo, Walker.forename,
             Walker.surname, Walker.telNo;


-- Q2d

-- Original
SELECT Route.routeID, woodName, description 
    FROM Route 
    WHERE footwear = "Trail shoes" 
       OR footwear = "Waterproof shoes" 
       OR footwear = "Walking shoes";

-- Updated
SELECT Route.routeID, woodName, description 
    FROM Route 
    WHERE footwear LIKE "%shoes";
