-- Title: H CS 2025 Task 2 Part B
-- Author: Mr Friend
-- Date: 20 Jan 2025

-- 2c
CREATE TEMP VIEW AvgValuation (avgValuation) AS
    SELECT AVG(valuation)
    FROM Comic;

SELECT comicTitle, issue, publisherName, valuation
    FROM Comic, Publisher, AvgValuation
    WHERE Publisher.publisherID = Comic.publisherID
      AND valuation > (avgValuation + 300);


-- 2d
SELECT characterName, SUM(valuation) AS [Total Valuation]
    FROM CharacterInfo, ComicCharacter, Comic
    WHERE CharacterInfo.characterID = ComicCharacter.characterID
      AND Comic.comicID = ComicCharacter.comicID
      AND characterName LIKE "%Duck%"
      AND mainCharacter = TRUE
    GROUP BY characterName
    ORDER BY [Total Valuation] DESC;


-- 2e
SELECT comicTitle, issue, publisherName, valuation * 2 AS [Double Price]  -- * 2
    FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter 
    WHERE Series.seriesName = "The OK Seven"  
      AND characterName = "Starlordly"  
      AND Comic.publisherID = Publisher.publisherID  
      AND Comic.seriesID = Series.seriesID  
      AND CharacterInfo.characterID = ComicCharacter.characterID
      AND Comic.comicID = ComicCharacter.comicID;  -- Equi-join
