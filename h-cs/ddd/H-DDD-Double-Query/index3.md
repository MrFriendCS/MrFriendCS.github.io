# H DDD Double Query Part 5

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


## Data Dictionary

### Table: Plant

| Name        | Key  | Type   | Size | Req'd | Validation                 |
| ----------- | :--: | ------ | :--: | ----- | -------------------------- |
| category    |      | Text   | 10   | Y     |                            |
| name        |      | Text   | 20   | Y     |                            |
| variety     |      | Text   | 20   | Y     |                            |
| code        |      | Text   | 3    | Y     |                            |
| referenceID | PK   | Text   | 3    | Y     |                            |
| quantity    |      | Number |      | Y     | Range: >= 0                |
| price       |      | Number |      | Y     | Range: >= 0.00             |
| height      |      | Text   | 1    | Y     | Restricted choice: S, M, T |

Height: `S` = short, `M` = medium, `T` = tall.


## Introduction

Create SQL queries to display the required details.
Aliases should be used to display meaningful headings.
Use a temporary view containing a single value in the first query, then use this value in the second query.
Example output is shown for each answer.
Only the first five records are shown where more than five records are returned.


## Tasks

1.  List the reference ID, name, variety and price of the cheapest plant.

    | referenceID | name     | variety   | price |
    | ----------- | -------- | --------- | ----- |
    | P24         | Aconitem | Monkshood | 3.0   |


2.  List the reference ID, name and price of all perennial plants that are cheaper than the average price of patio plants.
The dearest plant should be listed first; plants with the same price should be listed in order of reference ID.

    | referenceID | name    | price |
    | ----------- | ------- | ----- |
    | P29         | Anemone | 8.5   |
    | P42         | Iris    | 6.0   |
    | P32         | Astilbe | 3.5   |
    | P41         | Hosta   | 3.5   |
    | P46         | Phlox   | 3.3   |


3.  List the reference ID, name and quantity of all patio or hedge plants that have a quantity greater than the largest quantity of any fuchsia plant.
Display the largest quantity first; plants with the same quantity should be listed in order of reference ID.

    | referenceID | name       | quantity |
    | ----------- | ---------- | -------- |
    | B07         | Eunonymous | 12       |
    | H59         | Bamboo     | 10       |
    | H64         | Dog Wood   | 10       |
    | B23         | Begonia    | 9        |


4.  Calculate the total quantity of fruit plants in stock.
List the reference ID, name and quantity of all tall plants that individually have a quantity greater than this total.

    | referenceID | name     | quantity |
    | ----------- | -------- | -------- |
    | H59         | Bamboo   | 10       |
    | H64         | Dog Wood | 10       |


5.  List the reference ID, name and variety of any other plant that costs the same as the plant with reference ID `S73`.
List the plants in alphabetical order of name.

    | referenceID | name     | variety |
    | ----------- | -------- | ------- |
    | S79         | Magnolia | Paul    |
    | C64         | Wisteria | Wonder  |


6.  Display the number of medium-height plant records that have a price below the average price of short plants.

    | Number of Plants |
    | ---------------- |
    | 13               |


7.  List the reference ID, name and price of any plant whose name starts with the letter `B` and costs at least as much as the dearest climbing plant.
Display the dearest plant first.

    | referenceID | name     | price |
    | ----------- | -------- | ----- |
    | H59         | Bamboo   | 149.0 |
    | S81         | Bay Tree | 70.0  |
    | S83         | Bay Tree | 40.0  |
    | H25         | Berberis | 35.0  |
    | B23         | Begonia  | 19.5  |


8.  The stock value of each plant record is calculated by multiplying its quantity by its price.
List the reference ID, name and stock value of all plant records with a stock value greater than the average stock value.
Display the largest stock value first; records with the same stock value should be listed in order of reference ID.

    | referenceID | name       | StockValue |
    | ----------- | ---------- | ---------- |
    | H59         | Bamboo     | 1490.0     |
    | H64         | Dog Wood   | 500.0      |
    | B23         | Begonia    | 175.5      |
    | H25         | Berberis   | 175.0      |
    | B07         | Eunonymous | 150.0      |
