# H DDD Computed Values Part 4

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


## Entity Relationship Diagram (ERD)

The tables called `Holiday` and `Hotel` are shown below.

![ERD](assets/erd4.png)


## Tasks

Create SQL queries to display the required details. 
An alias should be used to display a meaningful heading for each computed field. 
Example output is shown for each answer.

1.  List the name of each city in Ethiopia together with the population of the city which should be displayed in thousands.

    | city        | ?    |
    | ----        | ---- |
    | Addis Ababa | 2316 |
    | Dire Dawa   | 194 |
    | Gonder      | 166 |
    | Nazret      | 147 |
    | …           | … |

{:start="2"}
2.  List the name of each country together with its country code and population density (this tells us how many people live in each square kilometre of the country). 
The only countries listed should be those with a country code that starts with the letter 'M'. 
These should be listed from highest density to lowest.

    | country  | code | ?    |
    | -------  | ---- | ---- |
    | Monaco   | MC   | 31719 |
    | Macau    | MACX | 31052 |
    | Malta    | M    | 1173 |
    | Maldives | MV   | 902 |
    | …        | …    | … |

Note:
    * population density is calculated by dividing the total population of the country by its area

{:start="3"}
3.  List the name of the capital cities that have a population of more than 2,000,000 together with the area of their countries in square miles. 
The only cities shown should be those in countries that have an area over 500,000 square miles. 
These details should be listed with the smallest area in square miles first.

    | capital     | ?    |
    | -------     | ---- |
    | Lima        | 501235.8 |
    | Tehran      | 642720.0 |
    | Jakarta     | 748581.6 |
    | Mexico City | 769294.5 |
    | …           | … |

Note:
    * the area of each country is currently in square kilometres.  To convert to square miles, multiply by 0.39

{:start="4"}
4.  List each capital city that is east of London with the name of its country and the time difference in hours between it and London. 
This first countries listed should be those that have the greatest time difference from the UK; countries with the same time difference should be listed alphabetically.

    | capital    | country     | ?    |
    | -----      | -----       | ---- |
    | Suva       | Fiji        | 12 |
    | Funafuti   | Tuvalu      | 12 |
    | Wellington | New Zealand | 12 |
    | Tarawa     | Kiribati    | 12 |
    | …          | …           | … |

Notes:
    * the UK has a longitude of 0 and all countries east of the UK have a longitude > 0
    * each degree of longitude is equivalent to 4 minutes of time
    * generate the time difference in hours by dividing the longitude by 15
    * display time difference to the nearest whole hour

{:start="5"}
5.  List the name of each European capital city north of London with its latitudinal distance north of London. 
Cities further away should be shown first.

    | capital   | ?    |
    | -------   | ---- |
    | Helsinki  | 979 |
    | Oslo      | 953 |
    | Stockholm | 887 |
    | Tallinn   | 881 |
    | …         | … |

Notes:
    * European cities have a longitude between -6·5 and 30 degrees east
    * cities north of London have a latitude between 51·5 and 61 degrees north
    * each degree of difference in latitude if equivalent to 113 kilometres
