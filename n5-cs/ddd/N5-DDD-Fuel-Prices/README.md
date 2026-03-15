# N5 DDD Fuel Price - WiP


File: [FuelPrices.db](assets/FuelPrices.db "Download file")


## Data dictionary


### Table: Prisoner

| Attribute   | Key   | Type    | Size  | Req'd | Validation |
| ---------   | :---: | ----    | :---: | :---: | ---------- |
| id          | PK    | Number  |       | Y     | |
| name        |       | Text    | 30    | Y     | Length >= 3 |
| postcode    |       | Text    | 8     | Y     | Length >= 3 |
| motorway    |       | Boolean |       | N     | Restricted choice: Auburn, Black, Blond, Brown, Grey, None, Red, White |
| supermarket |       | Boolean |       | N     | Restricted choice: Amber, Black, Blue, Brown, Green, Hazel, Grey |
| latitude    |       | Number  |       | Y     | Range: >= 1.3 and <= 2.5 |
| longitude   |       | Number  |       | Y     | |
| e5          |       | Number  |       | Y     | |
| e10         |       | Number  |       | Y     | |
| b7s         |       | Number  |       | Y     | |
| b7p         |       | Number  |       | Y     | |
| open        |       | Time    |       | Y     | |
| close       |       | Time    |       | Y     | |
| openSun     |       | Time    |       | Y     | |
| closeSun    |       | Time    |       | Y     | |
| carWash     |       | Boolean |       | Y     | |
| toilets     |       | Boolean |       | Y     | |



## Tasks

1. 



{:start="5"}	 



