# H DDD Aggregate Functions Part 2

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


## Table: Plant

| Name        | Key | Type   | Size | Req'd | Validation |
| ----        | --- | ----   | ---- | ----- | ---------- |
| category    |     | Text   | 10   | Y     | |
| name        |     | Text   | 20   | Y     | |
| variety     |     | Text   | 20   | Y     | |
| code        |     | Text   | 3    | Y     | |
| referenceID | PK  | Text   | 3    | Y     | |
| unit        |     | Number |      | Y     | Range: >=0 |
| price       |     | Number |      | Y     | Range: >=0.00 |
| height      |     | Text   | 1    | Y     | Restricted choice: S, M, T |

Use SQL queries to display each set of required details, with appropriate aliases.

1.  Display the name of each category and the average price of plants in that category.  Round the average price to 2 decimal places.
2.  Display the plant codes together with the number of plants that share the same code.  The code with the most plants should be listed first; codes that have the same number of plants must be listed in alphabetical order of code.
3.  Display the list of plant heights and the range of the prices for each plant height (the range of prices is the difference between the dearest and the cheapest plant).
4.  Display the number of plants that have the letter `p` in their name together with the total cost of those plants.
5.  Display the largest and average unit size, of all plants that have a referenceID beginning with the letter `B`.  Round the average size to 1 decimal place.
6.  Display a list of quantities together with the number of plants that are sold in that quantity, and the lowest price.  The quantity with the least plants should be listed first; where the number of plants is the same, the plants should be listed by decreasing price.
7.  Display the list of categories and heights together with the average price of the plants in each sub-category of height.
