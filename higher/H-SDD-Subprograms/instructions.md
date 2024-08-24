# H SDD - Subprograms

## Introduction

Create a small program that will ask the user for two values, add them together, and display the result.

It must use subprograms!

## Information

### Parameter passing

Not all subprograms require a parameter to be passed to the subprogram, e.g. `print()`.

Some subprograms can be passed more than one parameter, e.g. `round(3.1415, 2)`.

### Return values

Not all subprograms return a value.

## Program top-level design

The data flow shows where a subprogram is to be used in the program.

* IN: Parameter passed to subprogram
* OUT: Value returned by subprogram

<table>
    <tr>
        <td>1. Get first value</td>
        <td>OUT: value1</td>
    </tr>
    <tr>
        <td>2. Get second value</td>
        <td>OUT: value2</td>
    </tr>
    <tr>
        <td>3. Calculate the total</td>
        <td>IN: value1, value2<br>
OUT: total</td>
    </tr>
    <tr>
        <td>4. Display the result</td>
        <td>IN: total</td>
    </tr>
</table>
