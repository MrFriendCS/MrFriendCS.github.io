# H DDD Clydeview

File: [Clydeview.db](assets/Clydeview.db "Download file")


## Data Dictionaries

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


