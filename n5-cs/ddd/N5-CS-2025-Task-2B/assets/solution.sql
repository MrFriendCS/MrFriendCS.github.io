-- Q2(d)(i)
INSERT INTO Climate
    VALUES (105, "Temperate Oceanic", "15-20", "70-80");


-- Q2(d)(ii)
UPDATE Plant
    SET climateRef = 103
    WHERE ediblePart = "Fruit";

-- Q2(d)(iii)
SELECT plantName, climateType, ediblePart,soilType, temperatureRange
    FROM Climate, Plant
    WHERE climate.climateRef = Plant.climateRef
      AND ediblePart = "Leaves"
    ORDER BY temperatureRange DESC;

-- Q3
SELECT Climate.climateRef, temperatureRange, plantName, ediblePart
FROM Climate, Plant                          -- Plant table missing
WHERE Climate.climateRef = Plant.climateRef  -- Equi-join missing
  AND soilType = "Loam"
  AND climateType = "Mediterranean";
