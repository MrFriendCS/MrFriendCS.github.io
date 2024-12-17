# N5 DDD - Santa Gifts

File: [Santa.db](assets/Santa.db "Download file")

## Introduction

For as long as anyone can remember, Santa has been keeping lists on paper.  This causes the elves no end of problems when they get nibbled by a reindeer or Mrs Claus has a tidy up and throws out an old scrap of paper that Santa still needs.

The elves have decided to modernise to help keep track of the data that's needed for such a massive operation.  They are starting with a small database, to help Santa with the transition, with just tables of who's been nice, or naughty, and the gifts that Santa will deliver.


## Tasks

1. Display all the data in the `Child` table.

2. Display the full names of all the nice children.  Sort the results alphabetically for both forename and surname.

3. Display all the data in the `Gift` table.

4. Display every field of the `Gift` table if the gift is a `LEGO Technic Lamborghini`.

5. Child 98 has been very nice and will get an extra gift.  Add the following details to the `Gift` table:

```
401,98,"PS5",479.00
```

{:start="6"}
6. Create a query to show that the record has been added.

7. Child 172 has been very naughty.  Change their `nice` status in the `Child` table.

8. Create a query to show the record has been changed.

9. Child 172 will no longer be getting their original gift, or gifts.  Change anything they would have got to a `Lump of coal`, and change the cost to `50p`.

10. Create a query to show all records that have changed.

11. Display the child ID, forename, and surname of everyone who will receive a `Chad Valley Wooden Pizza` from Santa.

12. Display the ID and forename of everyone who shares your surname.  Order the names alphbetically.

13. Display the ID, forename, and gift(s) they will receive of everyone who shares your surname.  Order the names alphbetically.

14. When the elves aren't looking, make sure there are at least three presents for yourself in the `Gift` table.  Don't steal somebody else's!

15. Create a query to show your full name and all your gifts.  Ensure the gifts are alphabetical.

16. The elves want a delivery list for Santa.  It is to be sorted alphabetically by surname and then forename.  The elves are insistent that ___only___ nice children are to appear on this list, as they will be on their own 'special' list.  An example of the output is shown below:

| childId | firstName | lastName   | item |
| ------- | --------  | -------    | ---- |
| 173     | David     | Best       | Marbles |
| 7       | Bianca    | Brotherton | Playdoh |
| 91      | Billy     | Brotherton | Maths set |

{:start="17"}
17. Add an additional filter to the previous query so that it only shows what will be delivered to you.  Make any other changes that are necessary.


## Data Dictionary

### Entity: Child

| Attribute | Key   | Type    | Size  | Req'd | Validation |
| --------- | :---: | ----    | :---: | :---: | ---------- |
| childID   | PK    | Number  |       | Y     | |
| firstName |       | Text    | 20    | Y     | |
| lastName  |       | Text    | 30    | Y     | |
| nice      |       | Boolean |       | Y     | |

### Entity: Gift

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| giftID    | PK    | Number |       | Y     | |
| childID   | FK    | Number |       | Y     | Exists in Child table |
| item      |       | Text   | 50    | Y     | |
| cost      |       | Number |       | Y     | |


## ERD

![ERD 1:M](assets/Diagrams/ERD-ChildGift.png)
