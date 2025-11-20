# N5 SDD - Result Part 3


## Introduction

A teacher wants an automatic grading system that will classify a test score using the table below.

    | Score    | Result |
    | :----:   | :----: |
    | 50-100   | Pass |
    | 0-49     | Fail |

Only scores from ___0___ to ___100___ are acceptable.


### Top level design (structure diagram)

![Structure diagram](assets/sd3.png)


## User Interface

Examples of the expected user interface are shown below, with some possible input and output values.


### Example 1

```
Test Result
-----------

Score: 75

Result: Pass

============
```


### Example 2

```
Test Result
-----------

Score: 101

Only scores from 0 to 100 can be used.

Score: 1

Result: Fail

============
```