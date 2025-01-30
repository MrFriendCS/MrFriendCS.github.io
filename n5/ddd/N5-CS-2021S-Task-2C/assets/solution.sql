-- Title: N5 CS 2023 Specimen Task 2 Part C
-- Author: Mr Friend
-- Date: 23 Nov 2023


-- Q2d(i) - Change player details
UPDATE Player
    SET clubName = "Dundee North",
        shirtNumber = 24
    WHERE registration = 814209;

-- Evidence
SELECT * 
    FROM Player 
    WHERE registration = 814209;


-- Q2d(ii) - Goalkeeping coaching day
SELECT Club.clubName, forename, surname
    FROM Club, Player
    WHERE Club.clubName = Player.clubName
        AND league = 1
        AND position = "Goalkeeper";


-- Q2e - Find invalid striker shirt number
SELECT forename, surname
    FROM Player
    WHERE (shirtNumber < 10
        OR shirtNumber > 15)
       AND position = "Striker";

