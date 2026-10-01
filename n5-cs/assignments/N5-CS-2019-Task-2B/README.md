# N5 CS 2019 Task 2B

Logan is a technician who has to generate usernames for a school’s Wi-Fi service.

Logan wants to write a program that will automatically generate unique usernames for students. The usernames have to be six characters long. The program should generate and display a list of student usernames.

## Program analysis

The program will ask how many usernames are to be generated. For each username, the first three letters of the student’s first name will be entered and then combined with a random ending from the list below.

The program stores five endings:

ing  
end  
axe  
gex  
goh

For a student with the first name David the technician would enter Dav. The program will generate the username by joining Dav to one of the endings listed above. For example the username generated could be Daving.

### Main Steps: Pseudocode

```
1. Store the endings

2. Enter the number of students

3. Start fixed loop for each student

    4. Enter first three letters of student’s name

    5. Generate random number

    6. Generate username

    7. Display the username

8. End Loop
```

### REFINEMENTS

```
4.1.  Start conditional loop

4.2.    Get the first three letters of student’s name

4.3.    If the length of the name is not equal to 3 then

4.4.      Display an error message

4.5.    End If

4.6.  Repeat until the name entered is 3 characters long


6.1.  If the first random number was generated add the first stored ending to the end of the first three letters of the student’s name

6.2.  If the second random number was generated add the second stored ending to the end of the first three letters of the student’s name

6.3.  If the third random number was generated add the third stored ending to the end of the first three letters of the student’s name

6.4.  If the fourth random number was generated add the fourth stored ending to the end of the first three letters of the student’s name

6.5.  If the fifth random number was generated add the fifth stored ending to the end of the first three letters of the student’s name

```

***2b*** Using the program design and refinements, implement the program in a language of your choice. Ensure the program matches the pseudocode provided. **(15 marks)**

Print evidence of your program code.

***2c*** Your program should be tested to ensure it will only accept 3 characters.

Complete the test table below **(2 marks)**

| Type of test | User input | Expected result | Actual result |
| --- | --- | --- | --- |
| Normal | | Input accepted | Printout of final output to show the input is accepted |
| Exceptional | | Error message displayed | Printout to show that an error message is generated. |

***2d*** Test your program using the following student names.

Chris  
Christina  
Christopher  
Chrethe  
Chrisoula  
Christie

Provide evidence of the inputs and outputs to show that you have completed the test. **(1 mark)**

***2e*** With reference to your code and testing, evaluate your own program by commenting on the following:

* Efficient use of programming constructs in your code **(1 mark)**

* Robustness of your completed program **(1 mark)**

* The readability of your code **(1 mark)**

* Evaluate the fitness for purpose of the solution **(1 mark)**
