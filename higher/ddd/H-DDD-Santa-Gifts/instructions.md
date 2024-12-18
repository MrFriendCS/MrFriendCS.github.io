# H DDD - Santa Gifts

File: [Santa.db](../../../n5/ddd/N5-DDD-Santa-Gifts/assets/Santa.db "Download file")

## Introduction

For as long as anyone can remember, Santa has been keeping lists on paper.  This causes the elves no end of problems when they get nibbled by a reindeer or Mrs Claus has a tidy up and throws out an old scrap of paper that Santa still needs.

The elves have decided to modernise to help keep track of the data that's needed for such a massive operation.  They are starting with a small database, to help Santa with the transition, with just tables of who's been nice, or naughty, and the gifts that Santa will deliver.


## Tasks

Ensure that all column names are meaningful.

1. Display the number of children.

2. Display the number of gifts.

3. Display the full names of all children whose surnames start with `Mac` or `Mc`.  Forenames are to be alphabetical.

4. Display only the LEGO gifts.  Ensure there are no duplicates in the displayed list.

5. Calculate the total cost of all the gifts.

6. Santa's local currency is Norwegian Kroner, with £1 = 14.079458 kr.  Display the total cost in Kroner, rounded to 0 decimal places.

7. Santa estimates that overall it costs about £15 to make a toy, but Mrs Claus thinks it's more.  Calculate the correct value.

8. For each surname, display how many children have that surname.

9. Display how many children have been naughty or nice.

10. By surname, display how many children have been naughty or nice.

11. Due to increased productivity, all of the costs have decreased by 5%.  Change the price of all the gifts accordingly.

12. By chance, some children get more presents than others. Who is getting the most, and how many will they get?  Only include nice children.

    __NB.__ The result of one VIEW can be used in another VIEW.

13. Will every child get a gift?  Display how many children will get a gift.

14. Santa's elves have been watching!  Change everyone with your surname to show they've been naughty.

15. Using a sub-query, ensure that all the newly regsitered naughty children only get a `Lump of coal` that costs `50p`.  Some useful code is shwon below.

``` sql
...
    WHERE childID IN 
        (SELECT childID
             FROM 

                         );
```

{:start="16"}
16. Naugthy children get a lump of coal.  Who is getting the most, and how many lumps will they get?

17. Mrs Claus feels that Santa has been too generous again this year.  Replace the most expensive gifts with the following gift:

| gift                                   | cost |
| ----                                   | ---- |
| Squishmallows Squish-a-Longs - 14 Pack | 18.00 |


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

![ERD 1:M](../../../n5/ddd/N5-DDD-Santa-Gifts/assets/Diagrams/ERD-ChildGift.png)
