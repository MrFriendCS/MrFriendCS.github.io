# H SDD Qualifying


## Introduction

Iain is the competition secretary of a running club. One of his tasks is to select the best runners in the club to enter national competitions.  The races are either 100 m, 200 m, or 400 m.

He wishes to write a program that will simplify the task of looking through a long text file of names, distances and times to find all the runners who have race times below the entry requirements for each competition.

The club stores names, distances, and times in text files.  The male sprinters are in a file called 'maleRunners.txt'.  An example of the data is shown below.

| Name     | Distance | Time |
| ----     | -------- | ---- |
| Daniel   | 100      | 11.45 |
| Mohammed | 400      | 58.34 |
| Bob      | 100      | 12.04 |
| Freddie  | 200      | 23.59 |
| Jonathan | 200      | 22.81 |

Before he writes the program, Iain scribbles out an algorithm defining how he will solve the problem.

```
1. Get data                       OUT: runner(name, distance, time)

2. Get race distance              OUT: distance

3. Get qualifying time            OUT: time

4. Display qualifiying runners    IN: runner(name, distance, time), distance, time
```


## User interface - Example

```
Distance: 400
Qualifying time: 59

Qualifing Runners
-----------------
Mohammed, 58.34
Nathan, 58.93
Greg, 50.2
Brian, 56.35
=================
```
