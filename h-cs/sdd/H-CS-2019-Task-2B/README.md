# H CS 2019 - Task 2 Part B


## Problem description 

Once a year a walking club asks all its members to submit the total number of miles they have walked.
The club collates this information in a text file.
A section of the [members.txt](assets/members.txt "Download file") file, which includes the names of members and the total miles they walked, is shown below. 
 
```
… 
Nikolai,Bryant,145.6 
Susan,Brown,34.2 
Teressa,Jones,398.5 
… 
```

The information in the file is then used to select prize winners. Prizes will be awarded for: 

* the furthest distance walked 
* any members who have walked more than 70% of the furthest distance 

A program is required to read the data for each member from the text file.  The program should use this data to find then display the furthest distance walked.  The names of every member who has walked more than 70% of the furthest distance should be written to an empty text file so that the file can be printed out later. 

The design for the walking club program is shown below. 


## Program top-level design (pseudocode)

| Step                                                  | Data Flow |
| :---                                                  | :-------- |
| 1. Read members’ data from file into array of records | __OUT__: members(forename,surname,distance) |
| 2. Find the furthest distance walked                  | __IN__: members(forename,surname,distance) <br> __OUT__: furthest |
| 3. Display the furthest distance walked               | __IN__: furthest |
| 4. Write club prize winners to file                   | __IN__: members(forename,surname,distance), furthest |


### Refinements

```
1.1 Open members.txt file
1.2 Start loop for each member
1.3     Get member forename
1.4     Get member surname
1.5     Get member distance
1.6     Store member forename, surname and distance in members() array
1.7 End loop
1.8 Close members.txt file

2.1  Set furthest to distance stored for first member in members() array
2.2 Start fixed loop from second member to end of array
2.3     If distance the current member walked is greater than furthest Then
2.4         Set furthest to current distance  
2.5     End If  
2.6 End fixed loop  

4.1 Open results.txt file
4.2 Write “The prize winning members are:” to the results.txt file
4.3 Start loop for each record in members() array
4.4     If the distance the member walked is greater than 0.7*furthest
4.5         write the forename and surname to the results.txt file
4.6     End if
4.7 End loop
```

___2c(i)___ Using the problem description and design, implement the program in a language of your choice. Your program should:

* be maintainable and modular 
* use a function to find and return the furthest distance walked by a member
* use a procedure to display the furthest distance walked 
* follow the design and the refinements provided

Print evidence of your program code and the results.txt file.  (__13 marks__)

___2c(ii)___ The club wants to display the number of whole marathons each member has walked. A marathon is 26.22 miles long.

An example of the calculation required is:

```
If Nikolai Bryant walks 145.6 miles this equates to:  
    145.6/26.22 miles = 5.59115179 marathons  
    Nikolai has therefore walked 5 whole marathons.
 ```

In the above example ‘Nikolai,Bryant,5’ would be stored. 

To accomplish this, further refinements of step 4 are added to the end of the current design. 

```
4.8  Write “The number of whole marathons walked by each member is” to the results.txt file 
4.9  Start loop for each record in members() array 
4.10     Calculate the number of whole marathons walked 
4.11     Write the forename, surname and the number of whole marathons to the results.txt file 
4.12 End loop 
4.13 Close the results.txt file
```

Using the above design, edit your original program code so that, for each member, the forename, surname and the number of whole marathons walked are stored in the results.txt file. 

Run your program and print evidence of your edited program code and evidence  that your program correctly stores the new data in the results.txt file. (2 marks)

___2d___ The function in step 2 is to be tested with the data shown below. 

```
    John,Davie,189.4
    Susie,Small,14.6
    Johnny,Atom,490.2
    Wendy,Khan,512.5
    Emir,Jones,170.3 
```

Using the variable names and data structure names from your own code, create a trace table to find the furthest distance walked by the members in the test data. (__2 marks__)

___2e___ With reference to your own program code, evaluate:

* the fitness for purpose of your program (__1 mark__)

* the maintainability of your program with reference to readability and modularity (__2 marks__)
