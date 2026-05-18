# AH SDD - MacCal Ferries Part 2


## Introduction

A new ferry operator, MacCal, is setting up in competition to a more establish rival.

MacCal is going to be digital by design and wants a system that refelcts that.

Each sailing has:

* unique sailing number
* date of sailing (yyyy-mm-dd format)
* time of sailing (hh:mm format)
* port of departure
* port of arrival
* duration of sailing, in minutes
* number of passenger tickets sold
* number of cars tickets sold

The system should allow staff to:

* display the status of a sailing
* increase passenger tickets sold by one or more
* increase passenger tickets sold by one or more
* display the arrival time


## Assumptions

* The date and time used to create a sailing will be in the correct format.
* the port of departure / arrival will be a 3 letter [UN/LOCDE](https://unlocode.unece.org/directory/locodes/?country=GB).
* The duration of a sailing will be a positive integer.
* A maximum of 50 passengers per sailing.
* A maximum of 10 cars per sailing.


## UML Class Diagram

![UML class diagram](assets/Diagrams/class.png)


## Example User Interface


### Status

```
Sailing: 7
Date: 2026-05-18
Time: 15:40
From: CBA
To: ADM
Duration: 55 minutes
Passengers: 32
Car: 8
```


### Arrival time

```
Sailing: 7
Depart: 15:40
Arrive: 16:35
```


## Task

1. Implement the new class.

2. Test the class.
