# N5 SDD - Five Lunches


## Introduction

To help people budget, an app is need to help calculate the cost of five school 


## Task

Using Python, create a program that implements the pseudocode below.

```
# Calculate the cost of 5 lunches

# Declarations for the program
DECLARE lunch INITIALLY 0.0
DECLARE total INITIALLY 0.0
DECLARE costs INITIALLY [0.0, 0.0, 0.0, 0.0, 0.0]

# Get the costs of 5 lunches from the user
SEND "Enter to cost of:" TO DISPLAY

FOR day FROM 1 to 5 DO
    SEND "Day " & day & ": £" TO DISPLAY
    RECEIVE lunch FROM KEYBOARD
    SET costs[day] TO lunch
END FOR

# Calculate the total
FOR meal FROM 1 to 5 DO
    SET total TO total + costs[meal]
END FOR

# Display the total
SEND "The total cost is: £" & total TO DISPLAY
```


## User Interface Example

```
School Lunches
--------------

Enter to cost of:

Day 1: £2.60
Day 2: £2.40
Day 3: £3.00
Day 4: £1.44
Day 5: £2.50

The total cost is: £11.94
==============
```
