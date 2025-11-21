# N5 SDD - Chance Part 3


## Task

Create a small program that will simulate a coin being flipped.  Internally, it will use `0` and `1` instead of `Heads` and `Tails`.  The values that the user can enter must be limited to `h` or `t`.


### Top level design (structure diagram)

![Structure diagram](assets/sd2.png)


## User Interface

Examples of the expected user interface are shown below, with some possible input and output values.


### Example 1

```
Coin Flipper
------------

Heads or Tails? h

Correct!  It was heads.

============
```


### Example 2

```
Coin Flipper
------------

Heads or Tails? snails

Only 'h' or 't' can be used.

Heads or Tails? h

Incorrect!
It was tails!

============
```
