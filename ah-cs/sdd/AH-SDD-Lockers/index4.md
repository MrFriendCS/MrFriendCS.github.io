# AH SDD - Lockers Part 4


## Introduction

A secondary school plans to introduce a new locker system for pupils.
Each pupil will be assigned a locker where they can safely store their belongings during the school day.

The lockers will be smart, meaning that they can be controlled via software.
A program will be required that will allow a member of staff to manage individual lockers via an app.


### Lockers

Each locker has a small ePaper display on the locker to display the following information:

* a unique locker number
* who it is assigned to
* locked / unlocked

An example of a display is show below:

&nbsp;&nbsp;&nbsp;&nbsp;&#127380; 5  
&nbsp;&nbsp;&nbsp;&nbsp;&#129489; Pete Smith  
&nbsp;&nbsp;&nbsp;&nbsp;&#128273; Locked


### Staff

The app should allow staff to:

* lock a locker
* unlock a locker
* get the information about a locker (locker number, pupil name, and locked status)
* search for unlocked lockers
* search for the locker number(s) of a specific pupil
* assign a locker to a pupil


## Analysis


### End-User Requirements

The following end user requiremnts were identified:

* EU1 - Staff are able to lock a locker remotely.
* EU2 - Staff are able to unlock a locker remotely.
* EU3 - Staff are able to find all unlocked lockers.
* EU4 - Staff are able to view all the information about a locker (locker number, pupil name, and locked status).
* EU5 - Staff are able to find the locker(s) assigned to a specific pupil.
* EU6 - Staff are able to assign a locker to a pupil.


### Functional Requiremnts

The following functional requiremnts were identified:

* FR1 - The program shall store a locker number for each locker.
* FR2 - The program shall store the name of a pupil assigned to each locker.
* FR3 - The program shall store whether a locker is locked or unlocked using a Boolean value.
* FR4 - The program shall provide a method to lock a locker.
* FR5 - The program shall provide a method to unlock a locker.
* FR6 - The program shall search through lockers to find unlocked lockers.
* FR7 - The program shall provide a method to retieve all the information about a locker.
* FR8 - The program shall search through lockers to find the locker(s) assigned to a specific pupil.
* FR9 - The program shall provide a method to allow staff to assign a locker to a pupil.
* FR10 - The program shall store multiple locker objects in an array.


### UML Use Case Diagram

The analysis of the proposed system allowed a UML use case diagram to be created.

![UML use case diagram](assets/diagrams/useCase.png)


## Design


### UML Class Diagram

From the analysis, a class for Locker was designed.

![UML clase diagram](assets/diagrams/class.png)


### Top Level Design

![Structure diagram](assets/diagrams/sd.png)


#### Example UI

```
Smart Locker System
-------------------

Number of lockers read from file: 20

The following lockers are unlocked:

    5
    19

Locker 13 is assigned to Jodie Whittaker.

Locker 14 has been assigned to Ncuti Gatwa.
```


## Implementation


### Locker Class

From UML class diagram, the Locker class was implemented.

Class code: [Locker.py](assets/Locker.py "Download file")


### Locker Class Testing

The class was tested using the following code.

Class test code: [lockerTest.py](assets/lockerTest.py "Download file")


### Locker Data

The details of the all the lockers have been saved to a file.

Locker data: [Lockers.csv](assets/Lockers.csv "Download file")



## Tasks

1. Using the class and data provided, implement the top level design.
