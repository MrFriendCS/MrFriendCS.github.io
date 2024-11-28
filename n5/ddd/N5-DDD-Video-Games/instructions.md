# N5 DDD Video Games


File: [VideoGames.db](assets/VideoGames.db "Download file")


## Tasks

``` sql
SELECT
    FROM
```

1. Select everything from the company table.

2. Select everything from the game table.

3. Select the company name and country for each record in the company table.

4. Display the title and genre for each record in the game table.

``` sql
SELECT
    FROM
    WHERE
```

{:start="5"}
5. Create a query that returns the details of all games that are suitable for those aged 5 or younger.

6. Display all the records for games that have sold more than 18,000 copies.

7. Create a query to find all companies founded after the 1st January 1991.  (Think carefully - how is the date stored?)

8. Show all games that are action or adventure genre

9. Display all games that cost less than £20 and have an age guidance suitable for those at least 16 years old.

10. Show all games created by the Elite company, and are of the action genre.

``` sql
SELECT
    FROM
    ORDER BY   (ASC / DESC)
```

{:start="11"}
11. Display all the company details and order by website address.

12. Create a query to display all the games sold with the highest number displayed first.

13. Show all the information about the games.  Order it by company name, then order of age guidance.


## Data dictionary

### Table: company

| Attribute | Key   | Type     | Size  | Req'd | Validation |
| --------- | :---: | ----     | :---: | :---: | ---------- |
| name      | PK    | VARCHAR  | 20    | Y     |            |
| country   |       | VARCHAR  | 20    | Y     |            |
| founded   |       | DATE     |       | Y     | range: >= 1 Jan 1970 |
| website   |       | VARCHAR  | 30    | N     |            |
| profit    |       | INT      |       | Y     |            |

### Table: game

| Attribute    | Key   | Type    | Size  | Req'd | Validation |
| ---------    | :---: | ----    | :---: | :---: | ---------- |
| title        | PK    | VARCHAR | 30    | Y     |            |
| company      | FK    | VARCHAR | 20    | Y     | Exists in company table |
| genre        |       | VARCHAR | 15    | Y     |            |
| age          |       | INT     |       | Y     | restricted choice: 3, 7, 12, 16, 18 |
| price        |       | FLOAT   |       | Y     | range: >= 0 and <= 100 |
| released     |       | DATE    |       | Y     | range: >= 1 Jan 1970 |
| copies_sold  |       | INT     |       | Y     | range: >= 0 |