-- Title: 2024 H CS Task 2 Part C
-- Author: Mr Friend
-- Date: 30 Jan 2025

 -- 2c
 SELECT initial, surname, swimCategory, teamName, COUNT(*) AS [Races won]
    FROM Swimmer, Team, Result
    WHERE Team.teamRef = Swimmer.teamRef
      AND Swimmer.swimmerID = Result.swimmerID
      AND position = 1
    GROUP BY initial, surname, swimCategory, teamName;


-- 2d

-- Find fastest
CREATE TEMP VIEW fast (fastest) AS
    SELECT MIN(raceTime)
    FROM Result
    WHERE lane = 1
       OR lane = 8;

-- Use fastest
SELECT initial, surname, teamName, city, eventDate
    FROM Swimmer, Team, Event, Result, Race, fast
    WHERE Team.teamRef = Swimmer.teamRef
      AND Swimmer.swimmerID = Result.swimmerID
      AND Event.eventID = Race.eventID
      AND Race.raceNumber = Result.raceNumber
      AND result.raceTime = fast.fastest;


-- 2e
SELECT teamName, COUNT(position) AS [Total medals won]
    FROM Result, Swimmer, Team
    WHERE Result.swimmerID = Swimmer.swimmerID
      AND Swimmer.teamRef = Team.teamRef
      AND position <= 3  -- Added to make query fit for purpose
    GROUP BY teamName;
