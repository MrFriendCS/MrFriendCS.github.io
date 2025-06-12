# H SDD - Conversion Functions

## Introduction

Create a file called `conversionFuncs.py`.  The file will contain the code for the following functions:

* _secToMinSec_
* _minToHourMin_
* _hourToDayHour_
* _mmToCMmm_
* _cmToMcm_
* _mToKMm_
* _inchesToFeetInches_
* _feetToYardsInches_


## Assumptions

The decimal part of any values passed to a function will be ignored.

The functions will return values of `(-1, -1)` if passed invalid values.


## Functions


### secToMinSec

This function will convert whole seconds to minutes and seconds.

#### Example code

``` python
print(secToMinSec(100))
```

#### Example output

```
(1, 40)
```


### minToHourMin

This function will convert whole minutes to hours and minutes.

#### Example code

``` python
print(minToHourMin(189))
```

#### Example output

```
(3, 9)
```


### hourToDayHour

This function will convert whole hours to days and hours.

#### Example code

``` python
print(hourToDayHour(56))
```

#### Example output

```
(2, 8)
```


### mmToCMmm

This function will convert whole millimetres to centimetres and millimetres.

#### Example code

``` python
print(mmToCMmm(115))
```

#### Example output

```
(11, 5)
```


### cmToMcm

This function will convert whole centimetres to metres and centimetres.

#### Example code

``` python
print(cmToMcm(72))
```

#### Example output

```
(0, 72)
```


### mToKMm

This function will convert whole metres to kilometres and metres.

#### Example code

``` python
print(mToKMm(2567))
```

#### Example output

```
(2, 567)
```


### inchesToFeetInches

This function will convert whole inches to feet and inches.

#### Example code

``` python
print(inchesToFeetInches(62))
```

#### Example output

```
(5, 2)
```


### feetToYardsInches

This function will convert whole feet to yards and feet.

#### Example code

``` python
print(feetToYardsInches(31))
```

#### Example output

```
(10, 1)
```


## Testing

Test the functions to ensure they work.  Apart from TAD, remove any code that is not in the functions.

Save the file [`conversionFuncsTests.py`](assets/conversionFuncsTests.py) to the same folder as `conversionFuncs.py`.  Open and run `conversionFuncs.py`.
