# N5 SDD - Five Lunches


## Task

Using Python, create a program that implements the pseudocode below.

```
# Calculate the cost of 5 lunches

# Declarations for the program
DECLARE lunch INITIALLY 0.0
DECLARE total INITIALLY 0.0
DECLARE costs INITIALLY [0.0, 0.0, 0.0, 0.0, 0.0]

# Get the costs of 5 lunches from the user
FOR day FROM 1 to 5 DO
    SEND "Enter to cost of day " & day & ": £"
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


## User Experience

Example below.

```
School Lunches
--------------

Enter to cost of day 1: £2.60
Enter to cost of day 2: £2.40
Enter to cost of day 3: £3.00
Enter to cost of day 4: £1.44
Enter to cost of day 5: £2.50

The total cost is: £11.94
```
