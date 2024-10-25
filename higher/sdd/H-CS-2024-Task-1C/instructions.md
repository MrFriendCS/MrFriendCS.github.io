# H CS 2024 - Task 1 Part C

## Problem description

A research organisation currently gathers and stores data on the salaries paid to the chief executive officers (CEOs) of the top 100 technology companies in the country.  They want a program to help them use this data effectively.


## Purpose

A CSV file ([companies.csv](assets/companies.csv "Download")) stores the following data about the 100 companies:

* company name
* number of employees
* salary paid to CEO

This data will be read into parallel arrays.

The program will allow the user to enter the name of a company to find and display the difference between that company’s CEO’s salary and the highest paid CEO of all 100 companies.

The program will also find the highest number of employees employed by a single company, and the number of companies who employ within 10% of that figure. 

Examples of the program outputs are shown below.

```
Enter the name of the company you would like to check:

Goldman
GameGo company has the highest paid CEO.
The Goldman CEO earns £222 817 less than the highest paid CEO.

The highest number of employees employed by a single company is 888.
11 companies employ within 10% of 888.
```


## Assumptions

* the external file is current and updated regularly 


## Design

A top level design for the main steps of the program (with partial refinements) is shown below.

```
1 Read from file into parallel arrays.     OUT: company(), numEmployees(), ceoSalary()

2 Find and display the difference between  IN: company(), ceoSalary()
  the chosen company’s CEO salary and the
  highest CEO salary.

3 Find and display the highest number of   IN: numEmployees()
  employees employed by a single company,
  and the number of companies who employ
  within 10% of that figure.
```

### Refinements

```
2.1   Ask user to enter the name of chosen company
2.2   Set found to false
2.3   Call findMaxPos function to return the position of highest CEO salary
2.4   Loop for company array
2.5   If current company is the chosen company
2.6   Set found to true
2.7   Set position to current index
2.8   End if
2.9   End loop
2.10  If chosen company name is in list
2.11      Subtract and store chosen company’s CEO salary from highest CEO salary
2.12      Display message containing name of company with highest CEO salary, name
          of chosen company, and difference in salaries
2.13  Else
2.14      Display "Company not found"
2.15  End if


3.1   Call findMaxPos function to return position of highest number of employees 
3.2   Set count to 0 
3.3   Loop for numEmployees array 
3.4       If current employees is greater than or equal to maximum employees*0.9 
3.5           Set count to count + 1 
3.6       End If 
3.7   End Loop 
3.8   Display message showing number of companies that employ within 10% of the
      highest number of employees
```


__1c__ Using the problem description and design, implement the program in a language of your choice.

You should:

* use a single function to find and return the position of the highest CEO salary, and the position of highest number of employees
* use procedures to:
    * read data from the ‘companies.csv’ file to parallel arrays
    * find and display the difference between the chosen company’s CEO salary and the highest CEO salary
    * find and display the highest number of employees employed by a single company, and the number of companies who employ within 10% of that figure
* test your program by using the chosen company Goldman

(___15 marks___)

Print evidence of:

* your program code
* program outputs from 1(c)


__1d__	Step 2 of the program is tested with the following sample test data.

```
Grap,724,375000
Ver,163,1031000
Meto,728,816000
TelTo,252,1031000
Selop,555,842000
Sever,307,569000
Lehar,805,564000
EastA,401,32000
```


__1d(i)__ The refinement at 2.12 is shown below:

```
2.12   Display message containing name of company with highest CEO salary,
       name of chosen company, and difference in salaries.
```

Explain why the output from the refinements provided for step 2 would be incorrect if the sample test data was used with Selop as a chosen input.

(___1 mark___)


__1d(ii)__ Describe the additional refinements that would be required before step 2.12 to ensure that the correct company name(s) are found.

(___2 marks___)


__1e__ Evaluate the efficiency of your own program, with reference to the use of the findMaxPos function. 

(___1 mark___)
