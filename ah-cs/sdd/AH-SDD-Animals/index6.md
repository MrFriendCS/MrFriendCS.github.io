# AH SDD - Animals Part 6


## Design


### Data Dictionary


#### Entity: Animal

| Attribute   | Key   | Type    | Size  | Req'd | Validation |
| ---------   | :---: | ----    | :---: | :---: | ---------- |
| animal_id   | PK    | integer |       | Y     | Auto increment |
| name        |       | varchar | 20    | Y     | Unique |
| age         |       | integer |       | Y     | Range: >= 0 |
| weight      |       | float   |       | Y     | Range: >= 0.0 |
| alive       |       | boolean |       | Y     | |


### User Interface

```
Barra Zoo
---------

Menu:

  1 Display all animals
  2 Add a new animal
  3 Celebrate a birthday
  4 Register a death
  5 Display oldest animal
  6 Display 10 oldest animals
  
  x Exit
  
Enter choice: 
```

### UML Class Diagram

![UML clase diagram](assets/diagrams/class5.png)


### Structure Diagram


#### Top-level Design

![Structure diagram](assets/diagrams/sd.png)


##### Display all animals

![Structure diagram](assets/diagrams/sd1.png)


##### Add a new animal

![Structure diagram](assets/diagrams/sd2.png)


##### Celebrate a birthday

![Structure diagram](assets/diagrams/sd3.png)


##### Register a death

![Structure diagram](assets/diagrams/sd4.png)


##### Display oldest animal

![Structure diagram](assets/diagrams/sd5.png)


##### Display 10 oldest animals

![Structure diagram](assets/diagrams/sd6.png)


##### Update record

![Structure diagram](assets/diagrams/sd7.png)
