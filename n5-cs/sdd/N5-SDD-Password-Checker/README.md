# N5 SDD - Password Checker


The developers of Bright, the possible replacement for Glow, want users to be issued with temporary passwords for the first time that they log into the system.

They have produced a program to create temporary passwords, but they want to confirm if they are valid.


## Program Analysis

A program is required that will determine if passwords are valid.  A password is vaild if:

* the first part is a single capital letter (A to Z)
* the second part is six characters long
* the third part is a two digit number
* the fourth part is a special character:
    * !
    * ?
    * $


### Input

* enter the parts of a password


### Process

* check each part of a password
* determine if all parts are valid
* store result
* combine parts into a single password


### Output

* password entered
* password's validity


## Design

The main steps of the program are shown below.

```
1. Initialise variables

2. Get password:
   2.1. Get password part 1
   2.2. Check part 1 validity
   
   2.3. Get password part 2
   2.4. Check part 2 validity
   
   2.5. Get password part 3
   2.6. Check part 3 validity
   
   2.7. Get password part 4
   2.8. Check part 4 validity
   
2.2. Check validity of parts
2.3. Create result
2.4. Store result
2.5. Store password
   
3. Display password
   
4. Display result
```


## User Interface


### Example 1

```
Password Checker
----------------

Part 1: G
Part 2: lasgow
Part 3: 99
Part 4: !

Password: Glasgow99!
Validity: Valid

================
```


### Example 2

```
Password Checker
----------------

Part 1: g
Part 2: lasgow
Part 3: 99
Part 4: %

Password: glasgow99%
Validity: Invalid - Capital Special

================
```
