# N5 DDD - Santa Gifts

## Introduction

For as long as anyone can remember, Santa has been keeping lists on paper.  This causes the elves no end of problems when they get nibbled by a reindeer or Mrs Claus has a tidy up and throws out an old scrap of paper that Santa still needs.

The elves have decided to modernise to help keep track of the data that's needed for such a massive operation.  They are starting with a small database, to help Santa with the transition, with just tables of who's been nice, or naughty, and the gifts that Santa will deliver.

## Tasks

1. Display the names of all the nice children.

2. Display every field of the `gift` table if the gift is a `LEGO Technic Lamborghini`.

3. Child 98 has been especially nice and will get an extra gift.  Add the following detils to the `gift` table:

```
401,98,"PS5"
```

4. Child 172 has been very naughty.  Change their `nice` status in the `child` table.

5. Child 172 will no longer be getting their original gift.  Make sure they now get a `Lump of coal`.

6. Display the child ID, forename, and surname of everyone who will recieve a `Chad Valley Wooden Pizza` from Santa.

7. Display the forename of everyone who shares your surname and show what gifts they will receive.  Order the names alphbetically.

8. Show what you will be getting from Santa.

9. When the elves aren't looking, add a couple of presents for yourself to the gift table.  Don't steal somebody else's!

10. The elves want a delivery list for Santa.  It is to be sorted alphabetically by surname and then forename.  The elves are insistent that ___only___ nice children are to appear on this list.  An example of the output is shown below:

| Forename | Surname    | Item |
| -------- | -------    | ---- |
| David    | Best       | Marbles |
| Bianca   | Brotherton | Playdoh |
| Billy    | Brotherton | Maths set |

11. Make sure you are on Santa's delivery list!

## Data Dictionary

### Entity: child

| Attribute  | Key   | Type    | Size  | Req'd | Validation |
| ---------  | :---: | ----    | :---: | :---: | ---------- |
| child_id   | PK    | number  |       | Y     |            |
| first_name |       | text    | 20    | N     |            |
| last_name  |       | text    | 30    | N     |            |
| nice       |       | boolean |       | N     |            |

### Entity: gift

| Attribute  | Key   | Type   | Size  | Req'd | Validation |
| ---------  | :---: | ----   | :---: | :---: | ---------- |
| gift_id    | PK    | number |       | Y     |            |
| child_id   | FK    | number |       | N     | Exists in child table |
| item       |       | text   | 50    | N     |            |
