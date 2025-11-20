# N5 DDD Entity and ERD Design Part 3


## Information

The RetroClothing website uses a relational database to store details of items of women’s clothing for sale and the brand of each item in two separate tables called `Item` and `Brand`.

To minimise data entry errors, RetroClothing applies the following restrictions:

* The nationality of the brands used in the website are American, British or Italian
* The eras featured on the site are 1940s, 1950s, 1960s and 1970s
* Item codes all have 7 characters
* Item size should be limited to 8, 10, 12, 14 and 16

Sample data stored in each table is shown below.


### Item Table

| Item Code | Description                        | Size | Era   | Brand ID |
| --------- | -----------                        | ---- | ----  | -------- |
| RSS1001   | Red swim suit                      | 10   | 1950s | B3 |
| FDP1002   | Floral dungarees playsuit          | 10   | 1970s | B2 |
| BSC2103   | Brown swing coat                   | 16   | 1960s | B5 |
| CSP3204   | Circle skirt black white polka dot | 12   | 1950s | B4 |
| FPD3225   | Floral print hostess dress         | 10   | 1970s | B5v


### Brand Table


| Brand ID | Brand           | Year Established | Nationality |
| -------- | -----           | ---------------- | ----------- |
| B1       | Valentino       | 1965             | Italian |
| B2       | Mary Quant      | 1970             | British |
| B3       | Rose Marie Reid | 1946             | American |
| B4       | Elmoor          |                  | British |
| B5       | Susan Small     | 1942             | British |


## Tasks

1.  Create a data dictionary for the Item entity.
2.  Create a data dictionary for the Brand entity.
3.  Create an Entity Relationship Diagram, including attributes, to represent the relationship between the Item and Brand entities.
4.  Describe the type of relationship that exists between the Item and Brand entities.
