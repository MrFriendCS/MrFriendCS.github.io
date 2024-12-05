# N5 DDD - Santa Gifts

File: [Santa.db](assets/Santa.db "Download file")

## Introduction

For as long as anyone can remember, Santa has been keeping lists on paper.  This causes the elves no end of problems when they get nibbled by a reindeer or Mrs Claus has a tidy up and throws out an old scrap of paper that Santa still needs.

The elves have decided to modernise to help keep track of the data that's needed for such a massive operation.  They are starting with a small database, to help Santa with the transition, with just tables of who's been nice, or naughty, and the gifts that Santa will deliver.


## Tasks

1. Display the names of all the nice children.

2. Display every field of the `Gift` table if the gift is a `LEGO Technic Lamborghini`.

3. Child 98 has been especially nice and will get an extra gift.  Add the following detils to the `Gift` table:

```
401,98,"PS5"
```

{:start="4"}
4. Child 172 has been very naughty.  Change their `nice` status in the `Child` table.

5. Child 172 will no longer be getting their original gift.  Make sure they now get a `Lump of coal`.

6. Display the child ID, forename, and surname of everyone who will receive a `Chad Valley Wooden Pizza` from Santa.

7. Display the forename of everyone who shares your surname and show what gifts they will receive.  Order the names alphbetically.

8. Using the `Gift` table, show what you will be getting from Santa.

9. When the elves aren't looking, add a couple of presents for yourself to the `Gift` table.  Don't steal somebody else's!

10. Using the `Gift` table, show what you will now be getting from Santa.

11. The elves want a delivery list for Santa.  It is to be sorted alphabetically by surname and then forename.  The elves are insistent that ___only___ nice children are to appear on this list.  An example of the output is shown below:

| firstName | lastName   | item |
| --------  | -------    | ---- |
| David     | Best       | Marbles |
| Bianca    | Brotherton | Playdoh |
| Billy     | Brotherton | Maths set |

{:start="12"}
12. Modify the delivery list so it only shows what will be dilivered to you.


## Data Dictionary

### Entity: Child

| Attribute | Key   | Type    | Size  | Req'd | Validation |
| --------- | :---: | ----    | :---: | :---: | ---------- |
| childID   | PK    | Number  |       | Y     |            |
| firstName |       | Text    | 20    | N     |            |
| lastName  |       | Text    | 30    | N     |            |
| nice      |       | Boolean |       | N     |            |

### Entity: Gift

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| giftID    | PK    | Number |       | Y     |            |
| childID   | FK    | Number |       | N     | Exists in child table |
| item      |       | Text   | 50    | N     |            |

### ERD

![ERD 1:M](assets/Diagrams/ERD-ChildGift.png)
