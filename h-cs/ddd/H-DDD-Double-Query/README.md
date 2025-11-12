# H DDD Double Query Part 2

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


## Entity Relationship Diagram (ERD)

The tables called `Country` and `City` are shown below.

![ERD](assets/erd2.png)


## Tasks

Create SQL queries to display the required details.
An alias should be used to display a meaningful heading for any computed values displayed.

1.  Display the name, capital city and total population of the country with the largest total population.
2.  Display details the name, country and population of any city that has a population which is at least 5,000,000 more than the average population of all the cities.
3.  Display the name of any city that is further north than Reykjavik (the latitude of these cities is greater than the latitude of Reykjavik).  The query should show the name of each relevant city, its latitude and country name.  The city that is furthest north should be listed first.
4.  Display the name and population of any city in the United Kingdom that has a population which is more than the average population of all the cities in Bolivia.  Arrange these details from smallest to largest population.
5.  Display the total number of countries with an area less than 1% of that of the country with the largest area.
