# N5 CS 2019 Task 1 Part C


File: [Vlogger.db](assets/Vlogger.db "Download file")

## Introduction

Video bloggers (vloggers) create videos to upload to social media websites.  Mirren 
promotes vloggers across Scotland.  She keeps a record of vloggers and the details of their 
videos.  Mirren names each video and rates them on a scale of 1 to 5 (one being the worst 
and five being the best).  Videos may be up to 300 seconds in length. 


## Data Dictionary


### Entity: Vlogger

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| vloggerID | PK    | number |       | Y     | |
| forename  |       | text   | 20    | Y     | |
| surname   |       | text   | 20    | Y     | |
| username  |       | text   | 6     | Y     | |
| expertise |       | text   | 15    | Y     | |


### Entity: Video

| Attribute   | Key   | Type   | Size  | Req'd | Validation |
| ---------   | :---: | ----   | :---: | :---: | ---------- |
| videoID     | PK    | number |       | Y     | |
| vloggerID   | FK    | number |       | Y     | Exists in Video table |
| videoName   |       | text   | 50    | Y     | |
| duration    |       | number |       | Y     | |
| dateCreated |       | date   |       | Y     | |
| content     |       | text   | 40    | Y     | |
| rating      |       | number |       | Y     | Range: >=1 and <=5 |


## Tasks

___1c(i)___ Mirren wants to advertise the best videos.

She wants to display the username and videoName of all videos with a rating greater than 3.

Implement the SQL statement that will output usernames and videoNames from the Vlogger and Video tables where the rating is greater than 3.

Print evidence of your SQL statement and the output from the query after it has been implemented.

(__4 marks__)


___1c (ii)___ One of the videos called “Slime” contains a recipe for slime which does not work.
It should be removed from the database.

Implement the SQL statement that will delete the Slime video which has a videoID of 3.

Print evidence of your SQL statement and the Video table after the SQL statement has been implemented.

(__2 marks__)
