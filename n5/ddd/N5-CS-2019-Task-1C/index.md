# N5 CS 2019 Task 1 Part C


File: [Vlogger.db](assets/Vlogger.db "Download file")

## Data Dictionary

### Entity: Vlogger

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| vloggerID | PK    | Number |       | Y     | |
| forename  |       | Text   | 20    | Y     | |
| surname   |       | Text   | 20    | Y     | |
| username  |       | Text   | 6     | Y     | |
| expertise |       | Text   | 15    | Y     | |

### Entity: Video

| Attribute   | Key   | Type   | Size  | Req'd | Validation |
| ---------   | :---: | ----   | :---: | :---: | ---------- |
| videoID     | PK    | Number |       | Y     | |
| vloggerID   | FK    | Number |       | Y     | Exists in Video table |
| videoName   |       | Text   | 50    | Y     | |
| duration    |       | Number |       | Y     | |
| dateCreated |       | Date   |       | Y     | |
| content     |       | Text   | 40    | Y     | |
| rating      |       | Number |       | Y     | Range: >=1 and <=5|


## Tasks

___1c(i)___ Mirren wants to advertise the best videos.

She wants to display the username and videoName of all videos with a rating greater than 3.

Implement the SQL statement that will output usernames and videoNames from the Vlogger and Video tables where the rating is greater than 3.

Print evidence of your SQL statement and the output from the query after it has been implemented. (__4 marks__)


___1c (ii)___ One of the videos called “Slime” contains a recipe for slime which does not work.
It should be removed from the database.

Implement the SQL statement that will delete the Slime video which has a videoID of 3.

Print evidence of your SQL statement and the Video table after the SQL statement has been implemented. (__2 marks__)
