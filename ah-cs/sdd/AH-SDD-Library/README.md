# AH SDD - Library


## Introduction

Castlebay School of Computing plans to install a self-service kiosk system to allow pupils to borrow and return books without needing staff assistance.

Each book in the system will have:

* a library number
* a title
* an author
* a status showing whether it is currently borrowed
* the date the book was borrowed (yyyy-mm-dd format)

The new system should allow a pupil to:

* view basic information about a book
* view whether a book is currently available
* borrow a book
* return a book
* view the days left / days late, as appropriate

When a pupil borrows a book, the system should update its status so that other pupils can see that it is unavailable and record the date.

A book can be borrowed for 3 weeks (21 days) before it is late.

When a pupil returns a book, the system should update its status so that other pupils can see that it is available.


## Example User Interface


### Basic information

```
Book ID: 1
Title: The Gruffalo
Author: Julia Donaldson
```


### Book availability

```
Book 1, The Gruffalo by Julia Donaldson, is in the library
```

```
Book 1, The Gruffalo by Julia Donaldson, has been borrowed.
Date borrowed: 2026-05-18
```

### Days left / Days late

```
Days left: 21
```

```
Days late: 9
```


## Tasks

1. Create a UML class diagram for a book that has properties and methods to support the new system.

2. Implement the new class.

3. Test the class.
