# H DDD - Santa Gifts

Database file: [Santa.db](../../../n5-cs/ddd/N5-DDD-Santa-Gifts/assets/Santa.db "Download file")


## ERD

![ERD 1:M:1](../../../n5-cs/ddd/N5-DDD-Santa-Gifts/assets/erd1.png)


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
| toyID     | FK    | Number |       | Y     | Exists in Toy table |


### Entity: Toy

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| toyID     | PK    | Number |       | Y     | |
| name      |       | Text   | 50    | Y     | |
| cost      |       | Number |       | Y     | |


## Introduction

For as long as anyone can remember, Santa has been keeping lists on paper.
This causes the elves no end of problems when they get nibbled by a reindeer or Mrs Claus has a tidy up and throws out an old scrap of paper that Santa still needs.

The elves have decided to modernise to help keep track of the data that's needed for such a massive operation.
They are starting with a small database, to help Santa with the transition, with just tables of who's been nice, or naughty, and the gifts that Santa will deliver.


## Tasks

Ensure that all column names are meaningful.

1. Display the total number of children.

2. Display the number of gifts.

3. Display the full names of all children whose surnames start with `Mac` or `Mc`.
Forenames are to be alphabetical.

4. Display only the LEGO toys.

5. Calculate the total cost of all the gifts.

6. Santa's local currency is Norwegian Kroner, with £1 = 13.57 kr.
Display the cost of all the toys in Kroner, rounded to 0 decimal places.

7. Santa estimates that overall it costs about £15 to make a toy, but Mrs Claus thinks it's more.
Calculate the correct value.

8. For each surname, display how many children have that surname.

9. Display how many children have been nice, and how many have not.

10. By surname, display how many children have been naughty or nice.

11. Due to increased productivity, all of the costs have decreased by 5%.
Change the price of all the toys accordingly.

12. Show the details of all the gifts to show that this change has been made.

13. By chance, some children get more presents than others.
Who is getting the most, and how many will they get?
Only include nice children to create an output similar to the one below.

| childID | Forename | Surname | No of Presents |
| ------- | -------- | ------- | -------------- |
| 894     | Billy    | Bragg   | 7              |

__NB.__ The result of one VIEW can be used in another VIEW.

{:start="14"}
14. Will every child get a gift?
Display how many children will get a gift of some description.

15. Santa's elves have been watching!
Change everyone with your surname to show they've been naughty.

16. Ensure that all the newly regsitered naughty children only get a `Lump of coal`.

17. Display all the details from `Child` and `Gift` of the newly naughty children.
Sort forenames alphabetically, and then childID from smallest to largest.

18. Some children will get a lump of coal.
Who is getting the most, and how many lumps will they get?
Sort the names, forename and surname, alphabetically.

19. Mrs Claus feels that Santa has been too generous again this year.
Replace the most expensive gift(s) with the following gift:

| gift                                   | cost |
| ----                                   | ---- |
| Squishmallows Squish-a-Longs - 14 Pack | 18.00 |

{:start="20"}
20. Write the SQL to show the modified gift records.
