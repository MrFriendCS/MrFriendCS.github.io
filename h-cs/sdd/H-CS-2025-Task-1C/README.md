# H CS 2025 - Task 1 Part C


## Problem description

A fast-food outlet uses an app to allow users to order food online.
The data collected by the app is stored in a text file.
The owner of the fast-food outlet wants a program to analyse and use this data.


# Purpose

The program should:

- display the total number of orders delivered and the total number of orders collected
- find the first customer who has submitted a 5-star rating for a given month

The text file stores:

- order number
- date of order
- customer email address 
- delivery or collection option
- order cost
- star rating from 1 (lowest) to 5 (highest)

The data from the text file will be read into an array of records.

The program will display the total number of orders delivered and the total 
number of orders collected to date.
A month will be entered into the program to find the first customer to give 
a 5-star rating for that month.
This customer will win a free meal.
Details of the winning customer will be written to a text file called `winningCustomer.txt`.
If there is no winning customer, a suitable message will be written to the file.

## Assumptions

- A new text file of orders will be created for each year.
- Data will be exported from the app to the text file on a regular basis.
- The data in the text file is in chronological order. 
- The data is formatted correctly and is error-free.

A text file `orders.txt` is used when the program is being created.
This file contains data for the 505 orders that were made in October, November 
and December 2024.
A sample of this data is shown below.

```
Ord1,01-Oct-24,jacobjoseph@lukewarmmail.com,Delivery,14.45,4
Ord2,01-Oct-24,arthurian@geemail.com,Collection,34.24,1
Ord3,01-Oct-24,rebeccashearer@wahoo.co.uk,Collection,17.13,3
...
Ord505,31-Dec-24,buddy@lol.com,Collection,34.67,1
```

When the month October is entered, the expected output is shown below.

```
Enter the first three letters of the month to search: Oct
Total number of orders delivered to date: 290
Total number of orders collected to date: 215
```

The expected content of the file, `winningCustomer.txt` is shown below.

```
Ord9,maxpower11@inlook.com,19.34
```




## Design


### Program top-level design (pseudocode)

```
1 Read from file into array    OUT orders(orderNum,date,email,option,cost,rating)
  of records.

2 Find the position of         IN  orders(orderNum,date,email,option,cost,rating) 
  the customerwho gave the
  first 5-star rating in a     OUT position
  given month.

3 Write details of the         IN  orders(orderNum,date,email,option,cost,rating),
  winning customer, or         position
  `no winner` message,
  to a text file.

4 Display the total number     IN  orders(orderNum,date,email,option,cost,rating)
  of orders delivered and
  the total number of orders
  collected.
```

#### Refinements

```
2.1  Set position to -1
2.2  Set index to 0
2.3  Ask user to enter month to search for
2.4  While position is -1 and index is less than the length of the array
2.5    If current month is equal to searched month and current rating is 5 then
2.6      Set position to index
2.7    End if
2.8    Add 1 to index
2.9  End while
2.10 Return position

3.1  Open new file `winningCustomer.txt`
3.2  If position is 0 or above then
3.3    Write winning order number, email and cost to `winningCustomer.txt`
3.4  Else
3.5    Write `No winner` to `winningCustomer.txt`
3.6  End if
3.7  Close `winningCustomer.txt`

4.1  Call countOption function to return the number of orders delivered
4.2  Call countOption function to return the number of orders collected
4.3  Output the total number of orders delivered
4.4  Output the total number of orders collected
```

__1c__ Using the problem description and design, implement the program in a 
language of your choice.

Your program should:

- read data from the ([orders.txt](assets/orders.txt "Download")) file 
and store into an array of records
- use procedures to:
	- write details of winner or ‘no winner’ message to file
	- display the totals
- use a single function to find and return the total number of orders delivered 
and the total number of orders collected
- be maintainable and modular
- be tested using the month of 'Oct' as the input. The expected output is shown 
in the problem description. 
(___15 marks___)

Print evidence of your:

- program code 
- program output from your test run
- `winningCustomer.txt` file

__1d__ The function 'Find the position of the customer who gave the first 5-star rating 
in a given month' is tested using the sample data below.

```
Ord165,31-Oct-24,scr83@lol.com,Collection,19.99,2
Ord166,31-Oct-24,itsjustjen@inlook.com,Delivery,24.00,4
Ord167,01-Nov-24,arthurian@geemail.com,Delivery,38.18,4
Ord168,01-Nov-24,thetribalchief@lol.com,Collection,12.49,5
Ord169,01-Nov-24,scr83@lol.com,Delivery,55.55,3
Ord170,01-Nov-24,duckguy@male.com,Collection,44.89,5
```

Complete the trace table below to show the values up to the end of the iteration 
of the conditional loop.
(___2 marks___)

Month searched: Nov

| orderNum | position | If current month is equal to searched month and current rating is 5 |
| -------- | -------- | ----- | 
| Ord165   | -1       | False |
| Ord166   |          |       |
| Ord167   |          |       |
| Ord168   |          |       |


__1e__ With reference to your own program code, evaluate the following.

The efficiency of your program with reference to the use of the 'countOption' function. 
(___1 mark___)

The maintainability of the first subprogram 'Read from file into array of records' 
if the file now contained data for a whole year from January 2025 to December 2025. 
Your answer should refer to data structures and loops.
(___2 marks___)
