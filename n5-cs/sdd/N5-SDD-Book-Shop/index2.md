# N5 SDD - Book Shop Part 2


## Introduction

The University of Barra (UoB) bookshop is upgrading its software.
To help students with the cost of the books they get a discount.
The book shop will accept a gift voucher to pay for all or some of the purchase.
Only one £10 gift voucher can be used per purchase.
When using a voucher, no change is given if the amount to pay is less than £10.


## Task

Use the structure diagram to implement a program that will accept a non-discounted amount, 
calculate the discounted price if appropriate, and then take into account using a voucher to pay for some, 
or all, of the amount.


## Top level design (Structure diagram)

![Structure diagram](assets/sd2.png "Structure diagram")


## Assumptions

1. The initial amount will be entered as pounds:

* £10 as 10
* 50p as 0.50

2. Any text entered is lower case, i.e. yes


### User Interface - Example 1

```
UoB Book Shop
-------------

Total amount: £10

Student? yes

Discount: £1.0
Amount to pay: £9.0

Voucher? yes
£10 voucher applied
No change given when using a voucher

Final amount to pay: £0.0
====================
```


### User Interface - Example 2
```
UoB Book Shop
-------------

Total amount: £7.25

Student? no
** No student discount applied **

Voucher? no
** No voucher applied **

Final amount to pay: £7.25
====================
```


### User Interface - Example 3
```
UoB Book Shop
-------------

Total amount: £25.50

Student? yes

Discount: £2.55
Amount to pay: £22.95

Voucher? yes
£10 voucher applied

Final amount to pay: £12.95
====================
```
