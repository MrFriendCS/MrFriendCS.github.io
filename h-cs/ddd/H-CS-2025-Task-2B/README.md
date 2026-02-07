# H CS 2025 - Task 2 Part B


File: [NorasComics.db](assets/NorasComics.db "Download")


An entity-relationship diagram for the database was created and is shown below.


___2b___ Explain why Nora had to include the ‘ComicCharacter’ entity in the final design.  (__1 mark__)


___2c___ Nora would like to work out the average value of all the comics in the collection 
and those that are above this average.

Implement the SQL statement(s) to display a list of the comic title, issue, publisher name, 
and valuation for comics that are valued at least £300 above this average. 

The expected output is shown below.  (__3 marks__)

| comicTitle              | issue | publisherName      | valuation |
| ----------              | ----- | -------------      | --------- |
| Duckguy Chronicles      | 4     | Panel Pals         | 558 |
| Falconer Fusion         | 4     | Kapow Publications | 589 |
| Green Lamplight Avenged | 18    | Epic Doddles       | 580 |
| Nightcrawlerly          | 6     | Kapow Publications | 601 |
| Silver Surface          | 5     | Epic Doddles       | 590 |
| Superdude               | 11    | Kapow Publications | 840 |
| The Incredible Sulk     | 6     | Epic Doddles       | 579 |
| The Incredible Sulk     | 20    | Epic Doddles       | 528 |

Print evidence of the implemented SQL statement(s) and the output produced. 


___2d___ Nora wants to see the total value of comics where the main character's name contains 'Duck'.

Implement the SQL statement to display the total values by character name with the highest value first.

The expected output is shown below. (__5 marks__)

| characterName | Total Valuation |
| ------------- | --------------- |
| Dare-Duck     | 1497 |
| Duckguy       | 1153 |
| Duck Gal      | 431 |
| Doctor Duck   | 370 |

Print evidence of the implemented SQL statement and the output produced.


___2e___ A comic book collector contacts Nora saying he would like to purchase any 
comics from the series 'The OK Seven' that feature the character named 'Starlordly'. 
He is willing to pay double what they are worth to ensure he gets them.

Nora creates the following SQL statement to find any comics that match this description, 
showing the title of the comic, the issue, the publisher name, and the comic's valuation 
after being doubled.

``` sql
SELECT comicTitle, issue, publisherName, valuation AS [Double Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE Series.seriesName = "The OK Seven"
AND characterName = "Starlordly"
AND Comic.publisherID = Publisher.publisherID
AND Comic.seriesID = Series.seriesID
AND CharacterInfo.characterID = ComicCharacter.characterID;
```

The query to test the above SQL is provided with the database.
When run, the output appears to be incorrect.

Amend the query by making the required changes to produce the correct output.

Print evidence of the amended SQL query and the output produced.  (__2 marks__)

The expected output is shown below.

| comicTitle     | issue | publisherName | Double Price |
| ----------     | ----- | ------------- | ------------ |
| Silver Surface | 5     | Epic Doddles  | 1180 |


___2f___ A full list of functional requirements for the database is shown below.

- A query to calculate the total value of comics that include specific characters
- A query to calculate how much a comic has increased in value since it was purchased
- A query to calculate the average value of the comics in the collection
- A query to find and display a list of all the comics valued below the average value
- A query to find and display a list of all the comics valued at £300 or more above the average value
- A query to find all the comics from a series that started in the 1980s


___2f(i)___ Identify the functional requirement that cannot be met using the current 
database structure.  (__1 mark__)


___2f(ii)___ Explain, with reference to the database structure, what additional data would 
be required to allow this requirement to be met.  (__1 mark__)
