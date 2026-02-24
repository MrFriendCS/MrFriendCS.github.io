# H CS 2022 Task 1 Part B


File: [mammals.txt](assets/mammals.txt "Download") (Right click: `Save link as ...`)


## Problem description

During the month of September, West Fife Walkers asked their walkers to enter sightings of different Scottish mammals into an existing app. When the user selects the ‘add sighting’ button, the app checks the data is valid and either:

* adds the valid sighting as a new line in a single text file stored on a server

or

* responds with an error stating the inputs are missing or invalid 

The app’s user interface is shown below.

![App's user interface](assets/userinterface.png "App's user interface")


## Purpose

A program is now required to analyse the data stored in the text file. The program should:

* display the age of the oldest person to add a sighting
* display the dates of sightings of a chosen mammal in a particular town
* count and display the number of sightings for each date in the text file.

A top-level design for the main steps and partial refinements of the sightings program is shown below. Data read from the text file is stored in an array of records in the program.


## Program top-level design (pseudocode)

<table>
<tr>
<td>1 Read from text file into sightings array of records</td>
<td>OUT: sightings(town,mammal,date,age)</td>
</tr>
<tr>
<td>2 Find and display the age of the oldest walker in the sightings data</td>
<td>IN: sightings(town,mammal,date,age)</td>
</tr>
<tr>
<td>3 Find and display the dates of sightings of a chosen mammal in a particular town</td>
<td>IN: sightings(town,mammal,date,age)</td>
</tr>
<tr>
<td>4 Count and display the number of sightings for each date in the text file</td>
<td>IN: sightings(town,mammal,date,age)</td>
</tr>
</table>


## Refinements

```
3.1  Ask user to enter town
3.2  Call a function to return a string input that starts with an upper-case character
3.3  Ask user to enter mammal
3.4  Call a function to return a string input that starts with an upper-case character
3.5  Display “The dates of sightings were:”
3.6  Start loop for each sighting in array of records
3.7    If sighting matches entered town and mammal then
3.8	     Display date
3.9    End if
3.10 End loop
```


## Refinement of function for steps 3.2 and 3.4

```
Set firstChar to ASCII value of first character in string
If the firstChar is between 97 and 122 then
  Set firstChar to firstChar −32
  Set string to concatenation of the new first character and the remaining string
End if
Return the string

4.1  Set dayToCount to first date in sightings array
4.2  Set count to 1
4.3  Start loop from second record to end of sightings array
4.4    If date in current record is the same as dayToCount then
4.5      Add 1 to count
4.6    Else
4.7      Display dayToCount and count
4.8      Set dayToCount to date in current record
4.9      Set count to 1
4.10   End if
4.11 End loop	
4.12 Display dayToCount and count
```


___1c___ Using the problem description and design, implement the program in a language of your choice. Your program should:

* use a procedure to:
    * read data from the file to an array of records
    * find and display the age of oldest walker
    * find and display dates of sightings
    * count and display sightings for each date in the file
* use a function to validate upper-case characters
* be maintainable and modular
* follow the design and the refinements provided

(__15 marks__)

Print evidence of:

* your completed program code 
* your output showing the number of sightings for each date in the text file.

Include your name and candidate number on all evidence.


___1d___ Step 4 of the main algorithm counts the number of sightings for each date in the file. There are six sightings on 1 September 2021.

Describe how a watchpoint could be used to test that these sightings are counted correctly.

(__2 marks__)


___1e___ With reference to your own program code, evaluate:

* the efficiency of the function that changes the first character of the user’s input to upper-case
* the maintainability of your program, referring to modularity

(__2 marks__)
