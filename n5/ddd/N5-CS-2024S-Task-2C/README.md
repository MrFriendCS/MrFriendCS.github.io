# N5 CS 2024 Specimen Task 2 Part C

[Originally 2021S ==> 2024S] #

[Database needs looking at as Player fields in a different order] #

## Data Dictionary

### Entity: Club

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| clubName  | PK    | text   | 20    | Y     | length <= 20 |
| street    |       | text   | 40    | Y     | length <= 40 |
| postcode  |       | text   | 8     | Y     | length <= 8 |
| formed    |       | date   |       | Y     | |
| league    |       | number |       | Y     | Restricted choice: 1, 2, 3 |


### Entity: Player

| Attribute    | Key   | Type   | Size  | Req'd | Validation |
| ---------    | :---: | ----   | :---: | :---: | ---------- |
| registration | PK    | number |       | Y     | Range: >= 100000 and <= 999999 |
| clubName     | FK    | text   | 12    | Y     | Existing clubName from Club table |
| forename     |       | text   | 20    | Y     | |
| surname      |       | text   | 30    | Y     | |
| mobileNo     |       | text   | 12    | Y     | length = 12 |
| dateOfBirth  |       | date   |       | Y     | |
| position     |       | text   | 10    | Y     | Restricted choice: Striker, Midefielder, Defender, Goalkeeper |
| shirtNumber  |       | number |       | Y     | Range: >= 1 and <= 25 |


___2c___ Using the data dictionary above, complete the relational database by adding the required validation to the shirtNumber field.  (__1 mark__)

Print evidence to show that you have added the validation to the database, to match the data dictionary requirements.


___2d(i)___ Noreen Glass, registration number 814209, has moved teams from Aviemore Aces to Dundee North. She will play in the number 24 shirt at her new club.

Implement __one__ SQL statement that will make the required changes to Noreen’s information.  (__3 marks__)

Print evidence of the SQL statement and the ‘Player’ table, clearly showing the change you have implemented.


___(ii)___ The Association would like to invite suitable players to a goalkeeper coaching day.

Implement an SQL statement that will only display a list of club names, players’ full names and mobile phone numbers for all league 1 goalkeepers.  (__4 marks__)

Print evidence of the SQL statement and the output.


___2e___ The Association’s rules state that players who play in the ‘Striker’ position are given a shirt number between 10 and 15.

Test the following SQL statement, which is intended to identify strikers who do not have the correct shirt number:

```sql
SELECT forename, surname
    FROM Player
    WHERE shirtNumber < 10
       OR shirtNumber > 15;
```

Explain why the output is not correct.  (__1 mark__)


___2f___ The following SQL statement produces an error when executed.

```sql
INSERT INTO Player
    VALUES (220745,"Unknown","Erin","Smith","07993 874657",
	        "1999-05-31","Striker",23);
```


___(i)___ Identify the value in the SQL statement that produces an error.  (__1 mark__)


___(ii)___ Explain why this error is expected if the database is fit for purpose.  (__1 mark__)
