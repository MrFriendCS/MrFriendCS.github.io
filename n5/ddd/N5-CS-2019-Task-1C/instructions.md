# N5 CS 2019 Task 1 Part B & C

## Data Dictionary

### Table: Vlogger

| Attribute | Key   | Type   | Size  | Req'd | Validation  |
| --------- | :---: | ----   | :---: | :---: | ----------  |
| vloggerID | PK    | number |       | Y     |             |
| forename  |       | text   | 20    | Y     |             |
| surname   |       | text   | 20    | Y     |             |
| username  |       | text   | 6     | Y     | Length = 6  |
| expertise |       | text   | 15    | Y     | Restricted choice: Programming, Gaming, Baking, Crafts, Makeup, Clothes |


## Part B Task

___1b___ Using the data dictionary complete the Vlogger table by adding the validation. 

Print evidence to show that you have added both validations to the Vlogger table.  (__2 marks__)

## Part C Tasks

___1c(i)___ Mirren wants to advertise the best videos.

She wants to display the username and videoName of all videos with a rating greater than 3.

Implement the SQL statement that will output usernames and videoNames from the Vlogger and Video tables where the rating is greater than 3.

Print evidence of your SQL statement and the output from the query after it has been implemented. (__4 marks__)

___1c (ii)___ One of the videos called “Slime” contains a recipe for slime which does not work.
It should be removed from the database.

Implement the SQL statement that will delete the Slime video which has a videoID of 3.

Print evidence of your SQL statement and the Video table after the SQL statement has been implemented. (__2 marks__)