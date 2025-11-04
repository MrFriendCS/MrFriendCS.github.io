# H DDD Wildcards Task 3

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


## Data Dictionary

### Table: Plant

| Attribute   | Key   | Type   | Req'd | Size  | Validation |
| ---------   | :---: | -----  | :---: | :---: | ---------- |
| Category    |       | text   |       | 10    | |
| plantName   |       | text   | Y     | 20    | |
| Variety     |       | text   | Y     | 20    | |
| code        |       | text   | Y     | 3     | |
| referenceID | PK    | text   | Y     | 3     | |
| Unit        |       | number |       |       | Range: >= 0 |
| Price       |       | number |       |       | Range: >= 0.00 |
| Height      |       | text   |       | 1     | Restricted choice: S, M, T |


Create SQL queries to display the required details.

1.	List the name and variety of any plant that has the letter `x` somewhere
 in the name of its variety.  These details should be listed in alphabetical
 order of plant name.
2.	List the category, name, plant code and price of any plant with a plant
 code that has exactly 2 characters.
3.	List the name of any plant, together with its plant code and height, with
 a code that contains the letter 'P' and a plant name that contains the letters
 'a' and 't' separated by exactly one character.
4.	List the name, reference ID and price of all plants with an `a` in the name
 which also end with the letter 'a'.  The dearest plant should be listed first;
 plants with the same price should be listed in alphabetical order of referenceID.
5.	List the plant code, referenceID and category of any plant that has a `3` in
 the middle of its referenceID (each referenceID has 3 characters) and the letter
 'r' anywhere in its plant code.  These plants should be listed in alphabetical
 order of category.
6.	List the plant name, unit size and price of any plant with the letters `a`
 and `n` (separated by exactly 2 other letters) in its name.  Arrange these plant
 details so that the largest unit size is listed first; plants with the same unit
 size should be arranged so that the cheapest plant is listed first.
7.	List the referenceID, plant name, variety and height of any plant with the
 letter `e` as the second letter of its plant name.  Only plants the belong to
 a variety that starts with the letter 'C' and ends with the letter 'e' should be listed.

