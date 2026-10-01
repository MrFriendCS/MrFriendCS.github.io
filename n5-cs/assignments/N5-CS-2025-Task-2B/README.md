# N5 CS 2025 Task 2 Part B


File: [plantDB.db](assets/plantDB.db "Download file")


## Introduction

An environmental group wants to encourage people to grow their own fruit and vegetables.
The group stores details on edible plants and the climates they grow in.


***2d***


***(i)***  A new climate is to be added to the database. Implement an SQL statement that will add the following climate:

climateRef: 105
climate type: Temperate Oceanic
temperature range: 15-20
humidity range: 70-80

Print evidence of your SQL statement and evidence clearly showing that the change has been implemented.

(**1 mark**)


***(ii)***  ClimateRef ‘103’ is the best climate for all plants that have an edible fruit.

Implement an SQL statement that will change the recommended climateRef to '103' where the edible part of the plant is 'Fruit'.

Print evidence of your SQL statement.

(**2 marks**)


***(iii)***  The group wants to promote growing edible leaves.
Implement an SQL statement that will display the plant name, climate type, edible part, soil type and temperature of all plants that grow edible leaves.

Show the results in order of temperature, with the highest temperature first.

Print evidence of your SQL statement and the output from the query after it has been implemented.

(**4 marks**)


***2e***  The following SQL statement is written to find the climateRef, temperature range, plant name and edible part of all plants that grow in loam soil and a Mediterranean climate.

```
SELECT Climate.climateRef, temperatureRange, plantName, 
ediblePart
FROM Climate
WHERE soilType = "Loam" 
AND climateType = "Mediterranean";
```

Test this SQL statement.

State two reasons why this SQL statement does not produce the expected output.

(**2 marks**)
