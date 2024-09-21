# N5 CS 2024 - Task 1 Part B


## Introduction

Delaney’s Disco wants to provide training sessions for their DJs. They want a computer program to be developed to ensure each training session runs smoothly.  


## Program analysis

The program will ask for the duration of a training session. The DJ enters the duration of each song they will play. The program will add up the duration of all songs until the total is greater than or equal to the duration of the training session. At this point, the program tells the DJ they have selected enough songs to complete the training session.

The program will select a random song when the DJ should switch on the foam machine.


### Assumptions

* The duration of the training session will be entered in minutes but stored as seconds. 
* The duration of the training session will between 10 and 30 minutes. 
* The duration of each song will be entered in seconds. 
* When the final song is played in full, the training session duration may be longer than the original session duration entered by the user. 


### Main steps

1 initialise variables 
2 get valid training session duration  
3 convert duration of training session to seconds 
4 calculate total duration of songs 
5 display training session summary


### Refinements

<table>
<tr><td>2.1</td><td>ask for duration of training session</td></tr> 
<tr><td>2.2</td><td>while duration of training session < 10 or > 30</td></tr> 
<tr><td>2.3</td><td>display error message to enter valid number</td></tr> 
<tr><td>2.4</td><td>ask user to re-enter duration of training session</td></tr> 
<tr><td>2.5</td><td>end while loop</td></tr> 
</table>

 

3.1 duration of training session = duration of training session * 60 

 

4.1    songCounter = 0 
4.2 while total < duration of training session 
4.3 get and store duration of next song in seconds 
4.4 total = total + duration of next song 
4.5 if total >= duration of training session 
4.6 display message to inform user that they have entered enough songs 
4.7 end if 
4.8 add 1 to songCounter 
4.9 end while loop 

 

5.1 counter = 1 
5.2 display message stating the number of songs played + songCounter 
5.3 foamMachine = random number between 1 and songCounter 
5.4 start fixed loop for each stored song duration 
5.5 display counter + “:” + duration of next song 
5.6 if foamMachine = counter 
5.7 display message to start foam machine 
5.8 end if 
5.9 counter = counter + 1 
5.10 end fixed loop 
5.11 display total with message 













![Refinement](assets/r1.png "Refinement")

### Refinement of ‘Calculate and store the cost of each stage of the journey’

![Refinement](assets/r2.png "Refinement")

### Refinement of ‘Display total miles, journey stage costs and total cost’

![Refinement](assets/r3.png "Refinement")

__1b__	Using the program analysis and the design, implement the program in a language of your choice.

Ensure the program matches the structure diagram given. (___15 marks___)

Print evidence of your program code.	

__1c(i)__  Your program should be tested to ensure it produces the correct output.

Use the test data provided below to check that your program produces the correct output.

![Test table](assets/tt1.png "Test table")

Print evidence of the test showing inputs and outputs.  (___1 mark___)

__1c(ii)__	In the test data below, the mileage entered at Charge station 2 is not correct.

Complete the test table below — this will show that the program is not fit for purpose.  (___2 marks___)

![Test data](assets/tt2.png "Test data")

__1c(iii)__   With reference to the test data above, describe how to make the program fit for purpose. (___1 mark___)
