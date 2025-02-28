# H DDD Clydeview

File: [Clydeview.db](assets/Clydeview.db "Download file")


## Data Dictionary

### Table: Member

| Attribute        | Key   | Type  | Req'd | Size  | Validation |
| ---------        | :---: | ----- | :---: | :---: | ---------- |
| membershipNumber | PK    | text  | Y     | 6     | |
| Firstname        |       | text  | Y     | 30    | |
| Surname          |       | text  | Y     | 30    | |
| Address          |       | text  | Y     | 50    | |
| Town             |       | text  | Y     | 50    | |
| Postcode         |       | text  |       | 10    | |
| dateOfBirth      |       | date  |       |       | |
| monthOfRenewal   |       | text  |       | 15    | |
| typeOfMembership |       | text  |       | 7     | Restricted choice: Adult, Child, Senior, Student |


### Table: Plant

| Attribute   | Key   | Type   | Req'd | Size  | Validation |
| ---------   | :---: | -----  | :---: | :---: | ---------- |
| Category    |       | text   |       | 10    | |
| plantName   |       | text   | Y     | 20    | |
| Variety     |       | text   | Y     | 20    | |
| code        |       | text   | Y     | 3     | |
| referenceID | PK    | text   | Y     | 3     | |
| Unit        |       | number |       |       | Range: >= 0 |
| Price       |       | number |       |       | Range: >= 0.00 |
| Height      |       | text   |       | 1     | Restricted choice: S, M, T |


### Table: Question1

| Attribute | Key   | Type   | Req'd | Size  | Validation |
| --------- | :---: | -----  | :---: | :---: | ---------- |
| PupilID   | PK    | number | Y     |       | |
| Forename  |       | text   | Y     | 12    | |
| Surname   |       | text   | Y     | 12    | |
| test1     |       | number | Y     |       | Range: >= 0 and <= 10 |
| test2     |       | number | Y     |       | Range: >= 0 and <= 10 |
| test3     |       | number | Y     |       | Range: >= 0 and <= 10 |
| test4     |       | number | Y     |       | Range: >= 0 and <= 10 |


### Table: Question2

| Attribute   | Key   | Type   | Req'd | Size  | Validation |
| ---------   | :---: | -----  | :---: | :---: | ---------- |
| StaffID     | PK    | number | Y     |       | |
| Forename    |       | text   | Y     | 12    | |
| Surname     |       | text   | Y     | 12    | |
| hourlyRate  |       | number | Y     |       | Range: >= 0.00 |
| hoursWorked |       | number | Y     |       | Range: >= 0 |


### Table: Question3

| Attribute | Key   | Type   | Req'd | Size  | Validation |
| --------- | :---: | -----  | :---: | :---: | ---------- |
| StudentID | PK    | number | Y     |       | |
| Forename  |       | text   | Y     | 50    | |
| Surname   |       | text   | Y     | 50    | |
| test1     |       | number | Y     |       | Range: >= 0 and <= 20 |
| test2     |       | number | Y     |       | Range: >= 0 and <= 20 |
| test3     |       | number | Y     |       | Range: >= 0 and <= 20 |
| test4     |       | number | Y     |       | Range: >= 0 and <= 20 |
| test5     |       | number | Y     |       | Range: >= 0 and <= 20 |


### Table: Question4

| Attribute    | Key   | Type   | Req'd | Size  | Validation |
| ---------    | :---: | -----  | :---: | :---: | ---------- |
| ProductID    | PK    | number | Y     |       | |
| productName  |       | text   | Y     | 12    | |
| buyingPrice  |       | number | Y     |       | Range: >= 0 |
| sellingPrice |       | number | Y     |       | Range: >= 0 |


### Table: Question5

| Attribute   | Key   | Type   | Req'd | Size  | Validation |
| ---------   | :---: | -----  | :---: | :---: | ---------- |
| productName |       | text   | Y     | 20    | |
| ProductID   | PK    | text   | Y     | 50    | |
| priceUK     |       | number | Y     |       | Range: >= 0.00 |


### Table: Question6

| Attribute     | Key   | Type   | Req'd | Size  | Validation |
| ---------     | :---: | -----  | :---: | :---: | ---------- |
| fishType      | PK    | text   | Y     | 12    | |
| pricePerKilo  |       | number | Y     |       | Range: >= 0.00 |
| numberOfKilos |       | number | Y     |       | Range: >= 0.0 |
