# H SDD Qualifying

Iain is the competition secretary of a running club. One of his tasks is to select the best runners in the club to enter national competitions.

He wishes to write a program that will simplify the task of looking through a long text file of names, distances and times to find all the runners who have race times below the entry requirements for each competition.

The club stores names, distances, and times in text files.  The male sprinters are in a file called 'maleRunners.txt'.  An example of the data is shown below.  

| Name | Distance | Time |
| ---- | -------- | ---- |
| Daniel | 100    | 11.45 |
| Mohammed | 400  | 58.34 |
| Bob  | 100      | 12.04 |
| Freddie | 200   |  23.59 |
| Jonathan | 200  | 22.81 |

Before he writes the program, Iain scribbles out an algorithm defining how he will solve the problem.

```
0. initialise variables and data structures

1. read data from text file into array of records

2. ask the user to enter the length of the race (100, 200, or 400)

3. ask the user to enter the qualifying time, e.g. 11.5

4. display all the runners and their time, for the selected race, who have run faster than the qualifying time
```

Steps 1, 2, 3, and 4 are to be implemented as sub-programs.

The user input for Step 2 must be validated.

## Example UI

```
What distance: 400
Qualifying time: 59
Mohammed, 58.34
Nathan, 58.93
Greg, 50.2
Brian, 56.35
```
