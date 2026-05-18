# AH SDD - MacCal Ferries


## Introduction

A new ferry operator, MacCal, is setting up in competition to a more establish rival.

MacCal is going to be digital by design 

Each sailing has:

* unique sailing number
* port of departure
* port of arrival
* date of sailing (yyyy-mm-dd format)
* time of sailing (hh:mm format)
* duration of sailing, in minutes
* number of passenger tickets sold
* number of cars tickets sold

The system should allow staff to:

* display the status of a sailing
* increase passanger tickets sold by one or more
* increase passanger tickets sold by one or more
* display the arrival time


## Assumptions

* The date and time used to create a sailing will be in the correct format.
* the port of departure / arrival will be a 3 letter [UN/LOCDE](https://unlocode.unece.org/directory/locodes/?country=GB).
* The duration of a sailing will be a positive integer.
* A maximum of 50 passengers per sailing.
* A maximum of 10 cars per sailing.


## Example User Interface


### Status

```
Sailing: 7
Date: 2026-05-18
Time: 15:40
From: CBA
To: ADM
Duration: 55 minutes
```


### Arrival time

```
Sailing: 7
Depart: 15:40
Arrive: 16:35
```


## Task

1. Create a UML class diagram for a locker that has properties and methods to support the new system.

2. Implement the new class.

3. Test the class.
