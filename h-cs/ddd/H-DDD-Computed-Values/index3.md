# H DDD Computed Values Part 3

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


## Entity Relationship Diagram (ERD)

The tables called `Movie` and `BoxOffice` are shown below.

![ERD](assets/erd3.png)


## Tasks

Create SQL queries to display the required details.
An alias should be used to display a meaningful heading for each computed field.

1.	List the title and the profit made of any movie that made a profit with its international sales.
Display the movie with the largest profit first.

__NB__:	profit = international sales – movie budget

2.	List the name of the director of each movie with value of the combined US and international sales.
Display the details in alphabetical order of director; movies by the same director should be listed in order of total income, from least to most.
3.	List the name of each movie with the year it was released and its rating.
The international sales for each movie should be shown in millions.
Only movies with international sales over 150 million that have a rating of at least 8 should be included in the list.
4.	List the title of each movie together with its duration.
The duration should also be shown in separate hours and minutes.
For example:

| title | Hours | Minutes |
| ----- | ----- | ------- |
| Cars  | 1     | 57 |

The movies should be listed in decreasing order of hours; movies that last for the same number of hours should be listed in decreasing order of minutes.

{:start="5"}
5.	List the title of each movie, the name of each director and its rating as a percentage (the maximum rating is 10).
The movie with the highest rating should be listed first; movies with the same rating should be listed in alphabetical order of title.



