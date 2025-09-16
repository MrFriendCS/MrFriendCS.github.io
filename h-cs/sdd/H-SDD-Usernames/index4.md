# H SDD - Usernames Part 4


## Introduction

Each year, only 100 students are able to enrol at the prestigous Barra School of Computing (BSC).

Each student is issued with a username.  Usernames are created from a student's first name, last name, and National Insurance (NI) number.  A NI number is made up of 2 letters, 6 numbers and a final letter.


## Task

Implement the design below to create usernames and then write them to the file `usernames.txt`.

Usernames are nine characters long:

- The first three characters of the first name.
- The last three characters of the last name.
- The middle 3 characters of the NI number.

Usernames are always lowercase.


## Top level design (Pseudocode)

```
1. Read the student data from a csv file    OUT: student(firstName, lastName, insuranceNo)

2. Create the usernames                     IN: student(firstName, lastName, insuranceNo)
                                            OUT: usernames()  
   
3. Write the usernames to a text file       IN: usernames()
```


### Refinements

```
2.1 Loop for each student

    2.1.1 Call a function to extract first    IN: firstName, 3
          three characters of first name      OUT: part1

    2.1.2 Call a function to extract last     IN: lastName, 3
          three characters of last name       OUT: part2

    2.1.3 Call a function to extract middle   IN: insuranceNo, 4, 3
          three characters of NI number       OUT: part3
          
    2.1.4 Combine all parts to create a
          username

    2.1.5 Call function to convert            IN: username
          uppercase to lowercase              OUT: username
```


## Assumptions

1. There are 100 student records in the file
2. The data in the file is correctly formatted.


## Example Data

### rawData.csv

```
Barbra,Newhouse,ZQ018158G
Jeth,Grewcock,LU962093W
Earl,Vasiljevic,XQ961836I
Angelika,Wonham,KP724204Z
...
```


### usernames.txt

```
baruse181
jetock620
earvic618
angham242
...
```
