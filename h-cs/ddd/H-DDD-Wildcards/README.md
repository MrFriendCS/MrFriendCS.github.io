# H DDD Wildcards

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


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


Create SQL queries to display the required details.

1.	List the full name, postcode and the renewal month of all members with
 a surname that begins with the letter `D`.
2.	List the membership number, surname and full postal address of all members
 who have a surname that contains the pattern `oo`.  List these members in
 alphabetical order of surname.
3.	List the first name and home town of members with a first name that contains
 the letter `o` and who live in a town that starts with the letter `B` and ends
 with the letter `n`.
4.	List the full name of any members who have a surname that has exactly 4 letters,
 starting with the letter `L`.
5.	List the membership number, town and postcode of all members with a postcode
 that contains the letter `a` and the digit `2` separated by exactly 1 character.
6.	List the full name and type of membership of all members who have a surname
 that contains the letters `i` and `e` separated by exactly two characters.
7.	List the membership number, date of birth and the type of membership for all
 adult members who were born in the month of October.
