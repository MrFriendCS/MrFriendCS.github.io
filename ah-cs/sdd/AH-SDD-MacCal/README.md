# AH SDD - MacCal Ferries


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


## Task

1. Create a UML class diagram for a sailing that has properties and methods to support the new system.
