# N5 CS 2018 Task 2

Scotven offers a mobile wi-fi service at outdoor events. They check the signal strength by taking readings from five locations.

![Map](assets/Map.png "Map")

The analysis and design for a program is shown below:

## Program analysis

A program is required to display the five readings taken at the event and a signal pattern. The signal pattern will show the strength of readings (S = strong, M = medium and P = poor) in the order the readings were taken (1 to 5), for example “SSMPS”.

## Assumptions
* readings of signal strengths are recorded with two decimal places from 0.00% to 100.00%
* a strong signal is greater than 80% signal strength
* a medium signal is less than a strong signal and more than a poor signal
* a poor signal is less than 30% signal strength

## Inputs
* five valid readings from the venue

## Processes

* round each reading to zero decimal places
* create a five character string representing the signal pattern

## Outputs
* a message displaying the signal pattern for example:
  * Signal Pattern is: SSMPS

* the five rounded readings with each reading number for example:
  * Reading 1 - 89
  * Reading 2 - 82
  * Reading 3 - 56
  * Reading 4 - 12
  * Reading 5 - 99

## Program design (structure diagram)

![Structure diagram](assets/sd.png "Structure diagram")

***2a*** Using the program analysis and design, implement the program in a language of your choice. Ensure the program matches the structure diagram provided.  (**15 marks**)

Print evidence of your program code.

***2b*** Your program should be tested to ensure it produces different signal patterns correctly.

Complete the table below to create one set of test data that will produce the expected output for the signal pattern shown.  (**2 marks**)

![Test data](assets/tt.png "Test table")

You must demonstrate that your program correctly outputs the signal pattern and the rounded readings.

Print evidence of inputs and outputs to show that you have completed the test.

***2c*** Your program should be tested to ensure that each signal strength character is correctly assigned as S, M or P. Six extreme test values are required to test this fully.

State the six test data values required:  (**3 marks**)

* Extreme 1 ***_
* Extreme 2 ***_
* Extreme 3 ***_
* Extreme 4 ***_
* Extreme 5 ***_
* Extreme 6 ***_

***2d*** With reference to your code, evaluate your program by commenting on the following:

* Fitness for purpose (**1 mark**)
* Where your code demonstrates efficient use of programming constructs (**1 mark**)
* Robustness of your completed program (**1 mark**)
* Readability of your code (**2 marks**)
