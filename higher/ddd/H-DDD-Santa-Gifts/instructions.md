# H DDD - Santa Gifts

File: [Santa.db](../../../n5/ddd/N5-DDD-Santa-Gifts/assets/Santa.db "Download file")

## Introduction

For as long as anyone can remember, Santa has been keeping lists on paper.  This causes the elves no end of problems when they get nibbled by a reindeer or Mrs Claus has a tidy up and throws out an old scrap of paper that Santa still needs.

The elves have decided to modernise to help keep track of the data that's needed for such a massive operation.  They are starting with a small database, to help Santa with the transition, with just tables of who's been nice, or naughty, and the gifts that Santa will deliver.


## Tasks

Ensure that all column names are meaningful.

1. Display the number of children.

2. Display the number of gifts.

3. Calculate the total cost of the all the gifts.

4. Santa's local currency is Norwegian Kroner, and £1 = 14.079458 kr.  Display the total cost in Kroner, rounded to 0 decimal places.

5. Santa estimates that it costs £15 to make each toy, but Mrs Claus thinks it's more.  Calculate the correct value.

6. For each surname, display how many children there are with that surname.

6. Display only the most popular surname.

7. Display how many children have been naughty or nice.

8. By surname, display how many children have been naughty or nice.

9. Santa's elves have been watching!  Change everyone with your surname to show they've been naughty.

10. Ensure that all the naughty children only get a `Lump of coal` that costs `50p`.  Someuseful code is shwon below.

``` sql
...
    WHERE childID IN 
        (SELECT childID
             FROM Naughty);
```





{:start="17"}
17. Add a filter to the previous query so that it only shows what will be delivered to you.  Make any other changes that are necessary.


## Data Dictionary

### Entity: Child

| Attribute | Key   | Type    | Size  | Req'd | Validation |
| --------- | :---: | ----    | :---: | :---: | ---------- |
| childID   | PK    | Number  |       | Y     | |
| firstName |       | Text    | 20    | N     | |
| lastName  |       | Text    | 30    | N     | |
| nice      |       | Boolean |       | N     | |

### Entity: Gift

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| giftID    | PK    | Number |       | Y     | |
| childID   | FK    | Number |       | Y     | Exists in child table |
| item      |       | Text   | 50    | Y     | |
| cost      |       | Number |       | Y     | |


## ERD

![ERD 1:M](assets/Diagrams/ERD-ChildGift.png)
