# N5 CS 2017 Specimen Task 1B


File: [WhitestarAmps.db](assets/WhitestarAmps.db "Download file")


## Data dictionary


### Entity name: Employee

| Attribute name | Key  | Type    | Size | Required | Validation |
| -------------- | :--: | ----    | :--: | :------: | ---------- |
| employeeNumber | PK   | Number  |      | Y        | Range: >=1000 AND <= 9999 |
| firstName      |      | Text    | 15   | Y        | |
| surname        |      | Text    | 15   | Y        | |
| address        |      | Text    | 50   | Y        | |
| contactNumber  |      | Text    | 11   | Y        | Length: = 11 |
| drivingLicence |      | Boolean |      | Y        | |


### Entity: Amplifier

| Attribute name | Key  | Type    | Size | Required | Validation |
| -------------- | :--: | ----    | :--: | :------: | ---------- |
| serialNumber   | PK   | Text    | 10   | Y        | Length: = 10  |
| dateBuilt      |      | Date    |      | Y        | |
| timeCompleted  |      | Time    |      | Y        | |
| model          |      | Text    | 7    | Y        | Restricted choice: Jazz8, Rock100 and Blues55 |
| testPassed     |      | Boolean |      | Y        | |
| employeeNumber | FK   | Number  |      | Y        | Existing employeeNumber from Employee table |


## Tasks

***1d*** The personal details of a new employee are listed below.

* Employee Number: 1599
* Name: Jeremy May
* Address: 67 Red Lane
* Driving licence: True
* Contact telephone Number: 07923782534

Implement the SQL statement that will add this new record to the correct table. (**2 marks**)

Print evidence of both the implemented SQL statement and the Employee table (clearly showing the new record).
