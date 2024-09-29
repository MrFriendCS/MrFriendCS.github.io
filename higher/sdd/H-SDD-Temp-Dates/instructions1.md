# H SDD - Temperature Dates


## Introduction

Barra Data Solutions (BDS) is hoping to break into the market for providing data services to other companies.  If a company has a problem with data, BDS intends to be the solution!

The local heritage centre has some histrorical temperature records that it wishes to use.  There is a year's worth of temperature readings, hour by hour, in a csv file ([dataUS.csv](assets/dataUS.csv "Download file")).  There 8,759 records in the file.

Unfortunately, the dates are in the US format, and all of the temperatures are in Fahrenheit.


## Task

Convert all of the dates from US to ISO format.  Convert all of the temperatures from Fahrenheit to Celsius.  Write the data to a new csv file, `dataISO.csv`.


## Top level design (Pseudocode)

```
1. Read the data from a csv file              OUT: dates(), times(), temps()

2. Convert the temperatures from              IN: temps()
   Fahrenheit to Centigrade                   OUT: temps()  
   
3. Convert the dates from US to ISO format    IN: dates()
                                              OUT: dates()

4. Write the data to a csv file               IN: dates(), times(), temps()
```

### Refinements

```
2.1 Loop for each temperature
    2.1.1 Call function to convert    IN: tempF
          current temperature         OUT: tempC

3.1 Loop for each date
    3.1.1 Call function to convert    IN: dateUS
          current date                OUT: dateISO
```


## Assumptions

1. There are 8,759 records.
2. The data is correctly formatted in the file provided to BDS.


## Data Formats

### Dates

Example date: 1st August 2024

* US: mm-dd-yyyy __/__ 08-01-2024
* ISO: yyyy-mm-dd __/__ 2024-08-01

### Temperatures

C = (F - 32) * 5/9
