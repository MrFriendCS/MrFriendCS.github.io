# H SDD - Tuck Shop Part 2

## Introduction

The Youth Cafe runs a tuck shop that sells sweets, crisps, drinks etc. The details of how much each item costs to buy from the Co-op are kept in the file [tuckshop.csv](assets/tuckshop.csv "CSV file").  There are three fields in the file: Name, Weight, and Price.

The Youth Cafe sells the items at a small profit (10%).


## Task

Write a modular program that will increase the prices by 10%, update the names of the items so each starts with a capital letter, and then save the data in a new file called `saleprices.csv`.


## Program top-level design (Structure Diagram)

![Structure diagram](assets/sd.png "Structure diagram")


### Example: tuckshop.csv

```
...
Haribo Giant Stawbs,16  ,0.30
nutella & Go!,48,1.30
Walkers Ready Salted Crisps,45,1.00
...
```


### Example: saleprices.csv

```
...
Haribo Giant Stawbs,16,0.33
Nutella & Go!,48,1.43
Walkers Ready Salted Crisps,45,1.10
...
```
