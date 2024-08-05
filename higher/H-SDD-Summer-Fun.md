# Higher SDD Tasks - Summer 2024

## Introduction

There are nearly eight weeks between classes in June and August.  There are eight tasks below, just one a week, to complete over the break.  Replit will switch off the Education element at the end of July, so make sure your code is still accessible when this happens.  An option would be to use [Thonny ](https://thonny.org/) or the [RPF Code Editor](https://editor.raspberrypi.org/en/) and save your code to OneDrive or OneNote.

## Task 1

Create a function (`inchesToFeet`) that will accept an integer.  The actual parameter will represent a length in inches.  The function is to convert this value into feet and inches and return these values.

### Example 1

#### Code

``` python
print(inchesToFeet(36))
```

#### Output

```
(3, 0)
```

### Example 2

#### Code

``` python
print(inchesToFeet(78))
```

#### Output

```
(6, 6)
```

## Task 2

Create a function (`makeUsername`) that will accept a string.  It will use the string to create a username and return it as a lowercase string, in the format:

* Characters: es
* Characters: first 4 characters of actual parameter, if long enough
* Integer: random single digit (1 to 9)
* Character: random single character (a to z)

### Example 3

#### Code

``` python
print(makeUsername("William"))
```

#### Output

```
eswill2f
```

### Example 4

#### Code

``` python
print(makeUsername("SUE"))
```

#### Output

```
essue5t
```

## Task 3

Create a function (`reverse`) that will reverse the characters in a string.

### Example 5

#### Code

``` python
print(reverse("William"))
```

#### Output

```
mailliW
```

### Example 6

#### Code

``` python
print(reverse("How are you m8?"))
```

#### Output

```
?8m uoy era woH
```

## Task 4

Create a function (`shift`) that will accept a letter (lower or uppercase) and return the next letter (uppercase).  If the letter is `z` or `Z` then `A` is returned.  Any other characters are returned unchanged.

### Example 7

#### Code

``` python
print(shift("a"))
```

#### Output

```
B
```

### Example 8

#### Code

``` python
print(shift("?"))
```

#### Output

```
?
```

## Task 5

Create a function (`contains`) that will accept a string and a character.  If the character is anywhere in the string the function will return `True`, otherwise it will return `False`.  The function is not case sensitive.

### Example 9

#### Code

``` python
print(contains("Help!", "!"))
```

#### Output

```
True
```

### Example 10

#### Code

``` python
print(contains("Help!", "h"))
```

#### Output

```
True
```

### Example 11

#### Code

``` python
print(contains("Help!", "a"))
```

#### Output

```
False
```

## Task 6

Create a function (`letterTypes`) that will accept a string.  The function will count the number of uppercase and lowercase characters and return the values.

### Example 12

#### Code

``` python
print(letterTypes("Ada Lovelace was the first programmer!"))
```

#### Output

```
(2, 30)
```

### Example 13

#### Code

``` python
print(letterTypes("####! ####!"))
```

#### Output

```
(0, 0)
```

## Task 7

Create a function (`checkIBSN13`) that will check if a 13-digit [ISBN](https://en.wikipedia.org/wiki/ISBN#ISBN-13_check_digit_calculation) is valid.  It will accept a string, and return a Boolean value.  The function must be able to accept ISBNs with and without dashes that separate the values.

The book 'The Computers That Made Britain: The Home Computer Revolution of the 1980s' has an ISBN-13 of 9781912047857.  There are 12 digits plus the final check digit.  The check digit is calculated using the other 12 digits.

Each digit is multiplied by either 1 or 3, depending on its position.

| 1st, 3rd, ...   | 2nd, 4th, ... |
| -------------   | ------------- |
| 9 &times; 1 = 9 | 7 &times; 3 = 21 |
| 8 &times; 1 = 8 | 1 &times; 3 = 3 |
| 9 &times; 1 = 9 | 1 &times; 3 = 3 |
| 2 &times; 1 = 2 | 0 &times; 3 = 0 |
| 4 &times; 1 = 4 | 7 &times; 3 = 21 |
| 8 &times; 1 = 8 | 5 &times; 3 = 15 |

Calculate the sum (example of working):

```
Sum = 9 + 21 + 8 + 3 + 9 + 3 + 2 + 0 + 4 + 21 + 8 + 15
Sum = 103
```

Calculate the remainder (example of working):

```
Remainder = Sum mod 10
Remainder = 103 mod 10
Remainder = 3
```

Calculate the sum digit (example of working):

```
Check digit = 10 - Remainder
Check digit = 10 - 3
Check digit = 7
```

### Example 14

#### Code

``` python
print(checkIBSN13("9781916868076"))
```

#### Output

```
True
```

### Example 15

#### Code

``` python
print(checkIBSN13("978-0-306-40615-7"))
```

#### Output

```
True
```

## Task 8

Create a procedure (`circleStuff`) that will accept a number that represents a radius.  It will calculate and display various values, rounded to 2 decimal points:

* Diameter
* Circumference
* [Area of a circle](https://www.mathsisfun.com/geometry/circle-area.html)
* [Volume of a sphere](https://www.mathsisfun.com/geometry/sphere-volume-area.html)

Any results that have no decimal part will be shown as an integer.

### Starter code

``` python
# Import math Library
import math

# Print the value of pi
print (math.pi)
```

### Example 16

#### Code

``` python
circleStuff(10.5)
```

#### Output

```
Diameter: 21 units
Circumference: 65.97 units
Area: 346.36 units squared
Volume: 4849.05 units cubed
```
