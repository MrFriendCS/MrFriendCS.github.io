# AH SDD - Library


## Introduction

Castlebay School of Computing plans to install a self-service kiosk system to allow pupils to borrow and return books without needing staff assistance.

The new system should allow a pupil to:

* Display basic information about a book
* View whether a book is currently available
* Scan a book to borrow it
* Scan a book to return it
* Calculate overdue fines for late returns

Each book in the system has:

* A library number
* A title
* An author
* A status showing whether it is currently borrowed
* The date the book is due to be returned

When a pupil borrows a book, the system should update its status so that other pupils can see that it is unavailable and record the due date.

A book can be borrowed for 3 weeks.
If a book is returned after the due date, the system should calculate a fine based on the number of overdue days.



## Task

Create a small app to record how far someone has walked over a four week period.  The app will calculate the total distance, and the average distance walked to 1 decimal point.

The data and the results will be written to the file `walking.txt`.


### Example: User Interface

```
Enter the number of miles walked each week:

Week 1: 12.3
Week 2: 9.7
Week 3: 11.1
Week 4: 12.7
```

### Example: walking.txt

```
Walking Results - 4 Weeks
-------------------------

Week 1: 12.3
Week 2: 9.7
Week 3: 11.1
Week 4: 12.7

Total: 45.8 miles

Average: 11.4 miles (1 dp)
```
