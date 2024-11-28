# N5 DDD Prison

File: [prison.db](assets/prison.db "Download file")

## Tasks

1. Select everything from the prisoner table. Keywords needed:

``` SQL
SELECT
    FROM
```

{:start="2"}
2. Write a SQL statement to show first name, last name, and prison ID.

3. Add a query to show only the hair colour, eye colour, and height of each prisoner.

4. Display all the information for prisoners with black hair. Keywords needed:

``` SQL
SELECT
    FROM
    WHERE
```
     
{:start="5"}	 
5. Add a query to show prison ID, conviction, and date of birth for all prisoner born on or after 1st Jan 2000.

6. Display the eye colour and date of birth for every prisoner convicted of cyberbullying.

7. Select all details of anyone convicted of kidnapping who is in an open prison. Keywords needed:

``` SQL
SELECT
    FROM
    WHERE
        (AND / OR)
```

{:start="8"}
8. Display the eyes, hair, and prison IDs for all prisoner with either black eyes or black hair.

9. Display the eyes, hair, and  prison IDs for all prisoner with either black eyes and black hair.

10. Find all MacNeils who are not in an open prison. display their forename, conviction, and date of birth.
    
11. Find all redheads convited of assault.  Display their names and eye colour.

12. Show the dates of birth and prison IDs of all prisoners born in 1999.

13. Display details for all the prisoners who are bald and have amber eyes.


## Data dictionary

### Table: Prisoner

| Attribute  | Key   | Type    | Size  | Req'd | Validation |
| ---------  | :---: | ----    | :---: | :---: | ---------- |
| prison_id  | PK    | Number  |       | Y     | |
| surname    |       | Text    | 30    | Y     | Length >= 3 |
| forename   |       | Text    | 20    | Y     | Length: >= 3 |
| hair       |       | Text    | 6     | N     | Restricted choice: Auburn, Black, Blond, Brown, Grey, None, Red, White |
| eyes       |       | Text    | 5     | N     | Restricted choice: Amber, Black, Blue, Brown, Green, Hazel, Grey |
| height     |       | Number  |       | Y     | Range: >= 1.3 and <= 2.5 |
| conviction |       | Text    | 20    | Y     | |       
| open       |       | Boolean |       | Y     | |
| dob        |       | Date    |       | Y     | |
