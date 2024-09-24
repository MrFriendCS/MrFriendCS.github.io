# N5 DDD Video Games

## Tasks

1. Select everything from the company table.

2. Select everything from the game table.

3. Select the company name and country for each record in the company table.

4. Display the title and genre for each record in the game table.

5. Create a query that returns the details of all games that are suitable for those aged 5 or younger.

6. Display all the records for games that have sold more than 18,000 copies.

7. Create a query to find all companies founded after the 1st January 1991.  (Think carefully - how is the date stored?)

8. Show all games that are action or adventure genre

9. Display all games that cost less than £20 and have an age guidance suitable for those at least 16 years old.

10. Show all games created by the Elite company, and are of the action genre.

11. Display all the company details and order by website address.  Keywords needed:

``` sql
SELECT
    FROM
    ORDER BY   (ASC / DESC)
```

12. Create a query to display all the games sold with the highest number displayed first.

13. Show all the information about the games.  Order it by company name, then order of age guidance.


## Data dictionary

### Table: company

| Attribute    | Key   | Type   | Size  | Req'd | Validation |
| ---------    | :---: | ----   | :---: | :---: | ---------- |
| company_name | PK    | text   | 20    | Y     |            |
| country      |       | text   | 20    | Y     |            |
| founded      |       | date   |       | Y     | range: >= 1 Jan 1970 |
| website      |       | text   | 30    | N     |            |
| profit       |       | number |       | Y     |            |

### Table: game

| Attribute    | Key   | Type   | Size  | Req'd | Validation |
| ---------    | :---: | ----   | :---: | :---: | ---------- |
| title        | PK    | text   | 30    | Y     |            |
| company_name | FK    | text   | 20    | Y     | Exists in company table |
| genre        |       | text   | 15    | Y     |            |
| age          |       | number |       | Y     | restricted choice: 3, 7, 12, 16, 18 |
| price        |       | number |       | Y     | range: >= 0 and <= 100 |
| released     |       | date   |       | Y     | range: >= 1 Jan 1970 |
| copies_sold  |       | number |       | Y     | range: >= 0 |