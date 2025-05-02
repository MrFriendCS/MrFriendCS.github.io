# H SDD - People

## Problem description

The Barra Heritage Centre has come across some data from the 1871 census.  The committe wants to see what can be done with the data.

## Purpose

A CSV file, [people.csv](assets/people.csv "Download file"), stores a sample of the data:

* forename
* surname
* age

The data will be read into an array of records.  The program will count the number of surnames that start with `Mac` or `Mc` and find the oldest people.

A summary of the data will be saved to file, `summary1871.txt`.

An example of the summary is shown below:

```
1871 Census Summary
-------------------

There were 72 people with either 'Mac' or 'Mc' surnames.

The oldest age was 81.

Oldest people:

	Seumas MacNeil
	Peigi MacKinnon

===================
```


## Assumptions

* the file contains 100 records
* the file is correctly formatted


## Top level design (Structure diagram)

![Structure diagram](assets/sd.png)


## Task

Using the problem description and design, implement a program in the language of your choice.
