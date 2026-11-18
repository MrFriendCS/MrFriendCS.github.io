# H DDD Double Query Part 4

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


## Entity Relationship Diagram (ERD)

The tables called `Holiday` and `Hotel` are shown below.

![ERD](assets/erd4.png)


## Tasks

Create SQL queries to display the required details.

Aliases should be used to display meaningful headings.

1.  Display the name, destination, country and distance from the airport of the hotel that is furthest from the airport.

    | name         | destination | country | kmFromAirport |
    | ----         | ----------- | ------- | ------------- |
    | Hotel Vicori | Lazio       | Italy   | 34.5 |


2.  Display the name and star rating of any hotel with a rating that is poorer than the average star rating of all the holidays that have the word `Break` or `Package` in their title.
The hotel with the highest star rating should be listed first; hotels with the same star rating should be listed in alphabetical order of hotel name.

    | name           | starRating |
    | ----           | ---------- |
    | Avanti         | 2 |
    | Catalonia Inn  | 2 |
    | Eastern Hotel  | 2 |
    | Lado Colina    | 2 |
    | Napolean Ville | 2 |

3.  Display the name, city and price per night of any hotel which is dearer than the dearest hotel in Edinburgh.
List the hotel details with the dearest hotel first; hotels with the same price should be listed in alphabetical order of city.

    | name                          | city      | pricePerNight |
    | ----                          | ----      | ------------- |
    | Tower Turrets                 | London    | 135.0 |
    | St James House                | London    | 120.0 |
    | Champs-Elysees Star Residence | Paris     | 120.0 |
    | Casa Luxor                    | Barcelona | 100.0 |
    | Villa Grande                  | Barcelona | 95.0 |

4.  Display the number of hotels that have the same star rating as the `Der Wald` hotel.

    | Same Stars |
    | ---------- |
    | 14 |


5.  Display the name and distance from the airport of any hotel in Lisbon that is closer to the airport than the average distance from the airport of all the hotels in Barcelona and Madrid.

    | name    | kmFromAirport |
    | ----    | ------------- |
    | Paz     | 10.0 |
    | Feriado | 12.3 |

6.  Display the name, departure date and duration of any holiday that has the same duration as the longest holiday to a city with the letter `o` as the second character of the city name.
Arrange these details so that the most recent holiday is listed first.

    | name              | dateOfDeparture | nights |
    | ----              | --------------- | ------ |
    | French Experience | 2024-07-13      | 6 |
    | Wimbledon Winner  | 2024-06-30      | 6 |
    | Lisbon Package    | 2024-06-12      | 6 |
