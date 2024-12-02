# H DDD Practise


File: [Practise.db](../../../n5/ddd/N5-DDD-Practise/assets/Practise.db "Download file")


## Data Dictionary 1

### Table: datatypes

| Attribute | Key   | Req'd | Type    | Validation |
| --------- | :---: | :---: | ----    | ---------- |
| rowID     | PK    | Y     | Text    | |
| integer   |       |       | Number  | Range: >= 1 and <= 100 |
| real      |       |       | Number  | Range: >= 1 and <= 100 |
| Date      |       |       | Date    | Range: >= 1900 and <= 2023 |
| Time      |       |       | Time    | |
| boolean   |       |       | Boolean | |


### Table: marathon

| Attribute | Key   | Req'd | Type   | Validation |
| --------- | :---: | :---: | ----   | ---------- |
| forename  |       | Y     | Text   | |
| surname   |       | Y     | Text   | |
| country   |       |       | Text   | Length = 3 |
| Number    | PK    | Y     | Number | Range: > 0 |
| gender    |       | Y     | Text   | Restricted choice: Men, Women |
| half      |       | Y     | Time   | |
| finish    |       | Y     | Time   | |


## Data Dictionary 2

### Table: pupil

| Attribute | Key   | Req'd | Type    | Validation |
| --------- | :---: | :---: | ----    | ---------- |
| pupilID   | PK    | Y     | Number  | Range: > 0 |
| homeID    | FK    |       | Number  | Exists in address table |
| firstName |       | Y     | Text    | |
| lastName  |       | Y     | Text    | |
| dob       |       | Y     | Date    | |
| age       |       | Y     | Number  | Range: >= 0 |
| enrolled  |       | Y     | Boolean | |


### Table: address

| Attribute | Key   | Req'd | Type    | Validation |
| --------- | :---: | :---: | ----    | ---------- |
| addressID | PK    | Y     | integer | |
| firstLine |       | Y     | Text    | |
| town      |       | Y     | Text    | |
| postcode  |       | Y     | Text    | |
| phone     |       |       | Text    | Length = 12 |


### Table: staff

| Attribute | Key   | Req'd | Type   | Validation |
| --------- | :---: | :---: | ----   | ---------- |
| staffID   | PK    | Y     | Number | |
| title     |       | Y     | Text   | |
| lastName  |       | Y     | Text   | |
| role      |       | Y     | Text   | |


### Table: subject

| Attribute | Key   | Req'd | Type   | Validation |
| --------- | :---: | :---: | ----   | ---------- |
| subjectID | PK    | Y     | Number | |
| subject   |       | Y     | Text   | |


### Table: teacher

| Attribute | Key     | Req'd | Type   | Validation |
| --------- | :---:   | :---: | ----   | ---------- |
| staffID   | PK / FK | Y     | Number | Exists in staff table |
| subject   | PK / FK | Y     | Text   | Exists in subject table |


## Data Dictionary 3

### Table: port

| Attribute      | Key   | Req'd | Type | Validation |
| ---------      | :---: | :---: | ---- | ---------- |
| portCode       | PK    | Y     | Text | Length = 3 |
| portName       |       | Y     | Text | |
| localAuthority |       | Y     | Text | |
| marineRegion   |       | Y     | Text | |
| serviceType    |       | Y     | Text | |


### Table: route

| Attribute       | Key   | Req'd | Type   | Validation |
| ---------       | :---: | :---: | ----   | ---------- |
| routeID         | PK    | Y     | Text   | |
| departCode      | FK    | Y     | Text   | Exists in port table |
| arriveCode      | FK    | Y     | Text   | Exists in port table |
| route           |       | Y     | Text   | |
| service         |       | Y     | Text   | |
| ferryType       |       | Y     | Text   | |
| seasonal        |       | Y     | Text   | |
| operator        |       | Y     | Text   | |
| serviceID       |       | Y     | Text   | |
| serviceCode     |       | Y     | Text   | |
| operatorUrl     |       |       | Text   | |
| subsidyType     |       |       | Text   | |
| subsidyProvider |       |       | Text   | |
| distanceMiles   |       |       | Number | |
| durationHours   |       |       | Number | |
