# H SDD – Calculation

## Introduction

Creating functions to do repetitive task is a useful feature of modular programming.  Get the function right, and it will produce the correct result every time it is called.  

## Task

Create the following functions:

| Name             | Description          | Parameters |
| ----             | -----------          | ---------- |
| areaOfSqaure     | Area of a square     | length, dp |
| areaOfRectangle  | Area of a rectangle  | width, height, dp |
| areaOfTriangle   | Area of a triangle   | base, height, dp |
| areaOfCircle     | Area of a circle     | value, type, dp |
| volumeOfCube     | Volume of a cube     | length, dp |
| volumeOfCuboid   | Volume of a cuboid   | length, base, height, dp |
| volumeOfCylinder | Volume of a cylinder | height, value, type, dp |

Each function will return the value to the specified number of decimal places.

The parameter `type` has two acceptable values:

1. `radius`
2. `diameter`

A function will return `-1` if invalid parameters are used.

Save the code as `calculation.py`.


## Testing

Run the file ![Calculation-Test.py](Calculation-Test.py "Download file"). The file must be in the same folder as `calculation.py`.