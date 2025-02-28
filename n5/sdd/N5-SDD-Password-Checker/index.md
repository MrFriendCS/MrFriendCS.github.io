# N5 SDD - Password Checker

The developers of Bright, the possible replacement for Glow, want users to be issued with temporary passwords for the first time that they log into the system.

They have produced a program to create the temporary passwords in batches of up to five at a time, but they want to confirm if they are valid.

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

* enter a valid number of passwords to check
* enter the parts of a password

### Process

* check each part of a password
* determine if all parts are valid
* store result
* combine parts into a single password
* store password

### Output

* list of passwords entered
* list of passwords' validity


## Design

The main steps of the program are shown below.

```
1. Get valid number of passwords to check

2. Loop for each password
   2.1. Get password parts
   2.2. Check validity of parts
   2.3. Create result
   2.4. Store result
   2.5. Store password
   
3. Loop for each password
   3.1. Display password
   
4. Loop for each result
   4.1. Display result
```

## User Interface

### Example 1

```
How many passwords to check? 1

Part 1: G
Part 2: lasgow
Part 3: 99
Part 4: !

Passwords
---------
1. Glasgow99!

Results
-------
1. Valid
```
### Example 2

```
How many passwords to check? 1

Part 1: g
Part 2: lasgow
Part 3: 99
Part 4: %

Passwords
---------
1. glasgow99%

Results
-------
1. Invalid: Capital Special
```
