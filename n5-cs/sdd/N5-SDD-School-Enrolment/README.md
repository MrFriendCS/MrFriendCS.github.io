# N5 SDD - School Enrolment


## Introduction

A program has been written to help office staff when they enrol a new pupil.
Using the age of a pupil, the program will decide which part of a school a pupil should be in.

The rules are:

* 3 to 4 - Pre-school
* 5 to 11 - Primary
* 12 to 18 - Secondary

The school only accepts pupils aged 3 to 18.

Unfortunately, the original programmer has left and the program needs to be tested to 
ensure it meets the needs of the office staff.


## Task

Test the program.  Where appropriate, improve it and debug it.


## Original code

```python
# Title: School Enrolment
# Author: 
# Date: 

age = 0
age = input("Age: ")
while age <= 3 and age >= 18:
    print("Invalid!")
    age = str(input("Age: "))
if age < 5:
    print("Pre-school")
elif aeg > 5 and age < 12:
    print("Primary")
elif:
    print("Secondary")
```
