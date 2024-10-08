# H SDD - Temperature v2

## Overview

A year's worth of temperature readings are in a [csv file](assets/tempF.csv "data file"), 8,759 readings in total.  All of the temperature readings are in Fahrenheit and need to be converted to Celsius, rounded to 1 decimal place.

## Top Level Design (Pseudocode)

1. Read the data from the csv file: `tempF.csv`
2. [Convert](https://www.mathsisfun.com/temperature-conversion.html "Maths is Fun!") the temperatures to Celsius
3. Write the data to the text file: `tempC.txt`

## Top Level Design (Structure diagram)

![Structure diagram](assets/sd.png)

### Data: tempF.csv

The supplied data is in the format:

* Date: YYYY-MM-DD
* Time: HH:MM:SS
* Temperature: 1 decimal place

```
2010-01-01,01:00:00,34.5
2010-01-01,02:00:00,34.2
2010-01-01,03:00:00,33.9
...
```

### Data: tempF.txt

The exported data is to be in the format:

* Date: YYYY-MM-DD
* Time: HH:MM:SS
* Temperature: 1 decimal place

```
2010-01-01,01:00:00,1.4
2010-01-01,02:00:00,1.2
2010-01-01,03:00:00,1.1
...
```
