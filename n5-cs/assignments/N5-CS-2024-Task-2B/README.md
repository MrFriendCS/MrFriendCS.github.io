# N5 CS 2024 Task 2 Part B

File: [DinoDiscoveries.db](assets/DinoDiscoveries.db "Download file")


___2c___ 
 
___(i)___ A new fossil has been discovered.
Implement an SQL statement that will add the following fossil discovery to the database. 

``` 
fossilID: 2061 
countryFound: USA 
year: 2023 
person: Garath 
dinoID: DINO_68 
```

Print evidence of the SQL statement and evidence that clearly shows that the change has been implemented.

(__2 marks__)


____(ii)___ The group is meeting youngsters from the USA.
They want to show them the names of all the dinosaurs whose fossils were discovered after 1980 in the USA.
The data should be sorted so that the earliest discovery is shown first.  

Implement the SQL statement that will produce this list.

Print evidence of your SQL statement and the output from the query after it has been implemented.

(__4 marks__)


___(iii)___ The details of the Aardonyx have been incorrectly entered.
Implement an SQL statement that will update the record so that the length of the dinosaur is 8.0 metres and the diet is `Herbivorous`.  

Print evidence of the SQL statement and evidence that clearly shows that the change has been implemented.

(__2 marks__) 


___2d___ The following SQL statement is written to find the name, country and diet of all dinosaurs that were 
longer than 10 metres and whose fossils were discovered in the 1930s.

``` sql
SELECT dinoName, country, diet 
FROM Dinosaur, Fossil 
WHERE year = 1930  
AND length > 10;
```

Test this SQL statement and state two reasons why it does not produce the expected output.

(__2 marks__)  
