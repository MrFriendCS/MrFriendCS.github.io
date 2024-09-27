# N5 DDD Prison

## Tasks

1. Select everything from the prisoner table. Keywords needed:

``` SQL
SELECT
    FROM
```

2. Write a SQL statement to show first name, last name, and prison ID.

3. Add a query to show only the hair colour, eye colour, and height of each prisoner.

4.  Display all the information for prisoners with black hair. Keywords needed:

``` SQL
SELECT
    FROM
    WHERE
```
        
5. Add a query to show prison ID, conviction, and date of birth for all prisoner born on or after 1st Jan 2000.

6. Display the eye colour and date of birth for every prisoner convicted of cyberbullying.

7. Select all details of anyone convicted of kidnapping who is in an open prison. Keywords needed:

``` SQL
SELECT
    FROM
    WHERE
        (AND / OR)
```

8. Display the eyes, hair, and prison IDs for all prisoner with either black eyes or black hair.

9. Display the eyes, hair, and  prison IDs for all prisoner with either black eyes and black hair.

10. Find all MacNeils who are not in an open prison. display thier forename, conviction, and date of birth.
    
11. Find all redheads convited of assault.  Display their names and eye colour.

12. Show the dates of birth and prison IDs of all prisoners born in 1999.

13. Display details for all the prisoners who are bald and have amber eyes.

## Data dictionary

### Table: prisoner

| Attribute  | Key   | Type    | Size  | Req'd | Validation |
| ---------  | :---: | ----    | :---: | :---: | ---------- |
| prison_id  | PK    | INT     |       | Y     |            |
| surname    |       | VARCHAR | 30    | Y     | length: >= 3 |
| forename   |       | VARCHAR | 20    | Y     | length: >= 3 |
| hair       |       | VARCHAR | 6     | N     | restricted choice: Auburn, Black, Blond, Brown, Grey, None, Red, White |
| eyes       |       | VARCHAR | 5     | N     | restricted choice: Amber, Black, Blue, Brown, Green, Hazel, Grey |
| height     |       | FLOAT   |       | Y     | range: >= 1.3 and <= 2.5 |
| conviction |       | VARCHAR | 20    | Y     |            |       
| open       |       | BOOLEAN |       | Y     |            |
| dob        |       | DATE    |       | Y     |            |
