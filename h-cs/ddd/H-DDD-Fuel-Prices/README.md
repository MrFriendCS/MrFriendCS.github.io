# H DDD Fuel Price


File: [FuelPrices.db](../../../n5-cs/ddd/N5-DDD-Fuel-Prices/assets/FuelPrices.db "Download file")


## Data dictionary


### Table: Station

| Attribute   | Key   | Type    | Size  | Req'd | Validation |
| ---------   | :---: | ----    | :---: | :---: | ---------- |
| id          | PK    | Number  |       | Y     | |
| name        |       | Text    | 30    | Y     | |
| postcode    |       | Text    | 8     | Y     | Length >= 5 |
| motorway    |       | Boolean |       | N     | |
| supermarket |       | Boolean |       | N     | |
| latitude    |       | Number  |       | N     | |
| longitude   |       | Number  |       | N     | |
| e5          |       | Number  |       | N     | |
| e10         |       | Number  |       | N     | |
| b7s         |       | Number  |       | N     | |
| b7p         |       | Number  |       | N     | |
| open        |       | Time    |       | N     | |
| close       |       | Time    |       | N     | |
| openSun     |       | Time    |       | N     | |
| closeSun    |       | Time    |       | N     | |
| carWash     |       | Boolean |       | N     | |
| toilets     |       | Boolean |       | N     | |


# Introduction

In the database there are two types of petrol, Unleaded (E10) and Super Unleaded (E5), and two types of diesel, Standard (B7S) and Premium (B7P).

Each of the stations has it location recorded with latitude (lat) and longitude (long).

![Compass](../../../n5-cs/ddd/N5-DDD-Fuel-Prices/assets/Diagrams/Compass.png)


## Tasks

