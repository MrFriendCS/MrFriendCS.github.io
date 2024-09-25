# H SDD - House Prices


## Introduction

Kisimul Conveyancing Ltd (KCL) keeps a database of properties in the Western Isles.

KCL has noticed that the value of properties is generally increasing.  However, not all properties have seen the same increases, in fact some have lost value, it depends of the desirability of the location.

KCL wants to update the property values in its database, and extract some other information.  It will provide a file that only includes the postcodes and current values.

When KCL created the data file a small error changed some of the postcodes from HS1 to HS0.

### Postcode Format

Each property has a postcode in the format:

 * HSx #$$

Where:

 * __x__ is a single digit
 * __#__ is a single digit
 * __$__ is a single letter

The single digit  (___x___) will be used to determine the percentage change of each property.


### Examples

#### Postcode: HS5 7BD

* Decrease: 2%
* Original value: £100,000
* New value: £98,000

#### Postcode: HS6 7BD

* Increase: 2%
* Original value: £100,000
* New value: £102,000

#### Postcode: HS9 3TY

* Increase: 5%
* Original value: £100,000
* New value: £105,000


## Design

1. Read in the postcodes and current house prices from `housePrices.csv`
2. Find and count all HS0 postcodes, write the result to `errorPostcodes.txt`
3. Amend all HS0 postcodes to HS1
4. Calculate the new house prices, using the postcode, to the nearest pound
5. Write the postcodes, old house prices, and new house prices to `newPrices.csv`
6. Find the lowest and highest house prices.
7. Write the postcodes and new house prices of the top 2% and bottom 2% of all properties to `extremes.txt`.


### Structure diagram

![Structure diagram](assets/sd.png)


### Refinements

```
3.1 Call a function to amend postcode
    IN: postcodeHS0
    OUT: postcodeHS1

4.1 For a HS1 to HS5 postcode call a function to decrease the property value by 2%
    IN: currentPrice, percent
    OUT: newPrice
4.2 For a HS6 to HS8 postcode call a function to increase the property value by 2%
    IN: currentPrice, percent
    OUT: newPrice
4.3 For a HS9 postcodes call a function to increase the property value by 5%
    IN: currentPrice, percent
    OUT: newPrice
```


## Example Output


### errorPostcodes.txt

```
There were 27 incorrect postcodes.

Errors
-------
HS0 1AA
HS0 2BB
...
```

### newPrices.csv

```
HS1 1AA,100000,98000
HS6 2BB,100000,102000
HS9 3CC,100000,105000
...
```


### extremes.txt

```
The most expensive house cost £400000.
The least expensive house cost £40000.

The top 2% of properties by price are:
HS8 3CC,392800
HS9 4DD,400000
...

The bottom 2% of properties by price are:
HS1 5EE,47200
HS2 6DD,40000
...

```


## Assumptions

1. There are 1000 properties.
2. The data is correctly formatted in the file provided by KCL.
