# N5 DDD Practise


File: [Practise.db](assets/Practise.db "Download file")


## Data Dictionary


### Entity: datatypes

| Attribute | Key   | Type    | Size  | Req'd | Validation |
| --------- | :---: | ----    | :---: | :---: | ---------- |
| rowID     | PK    | Number  |       | Y     |            |
| colour    |       | Text    | 10    | N     | Length >= 3 |
| score     |       | Number  |       | N     | Range: >= 0 and <= 100 |
| height    |       | Number  |       | Y     | Range: >= 1.0 and <= 2.5 |
| Date      |       | Date    |       | N     | Range: >= 1900-01-01 and <= 2025-12-31 |
| Time      |       | Time    |       | N     | Range: >= 08:00:00 and <= 16:00:00 |
| nice      |       | Boolean |       | Y     |            |


### Entity: pupil

| Attribute | Key   | Type    | Size  | Req'd | Validation |
| --------- | :---: | ----    | :---: | :---: | ---------- |
| pupilID   | PK    | Number  |       | Y     |            |
| addressID | FK    | Number  |       | N     | Exists addressID in address table |
| firstName |       | Text    | 20    | Y     |            |
| lastName  |       | Text    | 30    | Y     |            |
| dob       |       | Date    |       | Y     |            |
| age       |       | Number  |       | Y     | Range: >= 0 |
| enrolled  |       | Boolean |       | Y     |            |


### Entity: address

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| addressID | PK    | Number |       | Y     |            |
| firstLine |       | Text   | 30    | Y     |            |
| town      |       | Text   | 30    | Y     |            |
| postcode  |       | Text   | 8     | Y     | Length >= 6 |
| phone     |       | Text   | 12    | N     |            |


### Entity: marathon

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| surname   |       | Text   | 30    | Y     |            |
| forename  |       | Text   | 20    | Y     |            |
| country   |       | Text   | 3     | N     | Length = 3 |
| Number    | PK    | Number |       | Y     | Range: > 0 |
| category  |       | Text   | 10    | Y     |            |
| gender    |       | Text   | 1     | Y     | Restricted choice: M, F |
| half      |       | Time   |       | N     |            |
| finish    |       | Time   |       | N     |            |


### Entity: taxi

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| taxiID    | PK    | Number |       | Y     |            |
| taxiReg   |       | Text   | 8     | Y     |            |
| make      |       | Text   | 20    |       |            |
| model     |       | Text   | 20    |       |            |
| colour    |       | Text   | 15    |       |            |


### Entity: journey

| Attribute  | Key   | Type   | Size  | Req'd | Validation |
| ---------  | :---: | ----   | :---: | :---: | ---------- |
| journeyID  | PK    | Number |       | Y     |            |
| taxiID     | FK    | Number |       | Y     | Exists taxiID in taxi |
| pickUpDate |       | Date   |       | N     |            |
| pickUpTime |       | Time   |       | N     |            |
| pax        |       | Number |       | N     |            |
| pickUpLoc  |       | Text   | 30    | N     |            |
| dropOffLoc |       | Text   | 30    | N     |            |
