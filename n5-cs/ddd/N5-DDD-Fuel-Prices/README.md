# N5 DDD Fuel Price - WiP


File: [FuelPrices.db](assets/FuelPrices.db "Download file")


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


## Tasks

1. Display the postcode and name of all locations that have a carwash.
Sort both the postcode and the name alphabetically.

2. Display the name, id and latitude, where the latitude is bigger than __52.0__.
Display the namea alphabetically

3. Display the name of the station(s) with postcode _CO10 1GY_.

4. Display the name, id, and the price of Super Unleade of all motorway stations that sell Super Unleaded for more than £1.50.
Names are to be sorted descending.

5. Display the name, postcode, the opening and closing times.
Only display stations that are part of a supermarket, and have toilets.
Sort the postcodes alphabetically.

6. Display the name, latitude and longitude of any stations that have toilets but no car wash.
The names of the stations are to be displayed in reverse alphabetical order.

7. The BP station, with the id of 54, has changed its name to __RL__.

8. A new station has opened called "BARRAFFIN LTD".
It is to use the next available id and has a postcode of "HS9 5YD".
This station sells Super Unleaded for £1.23 and Premium Diesel for £1.32.
Add this new station to the database.

![Compass](assets/Diagrams/Compass.png)

{:start="9"}

9. Delete all stations to the west of __A&C MacLean__.

Write an SQL query to display the id, name, postcode, motorway, supermarket, latitude, longitude, e5, e10, b7s, b7p, close, open, openSun, closeSun, toilets. It has to only display things where the id is less than 10, or the Sunday opening time is after 6am, or it does not have a supermarket, or it closes after 11pm, or it has a latitude under 50 and a longitude over 10. Order by closing time latest to earliest, opening time earliest to latest, opening Sunday latest to earliest, the name in reverse alphabetical order, e5 in price highest to lowest, postcode in alphabetical order and b7s in cheapest to most expensive.