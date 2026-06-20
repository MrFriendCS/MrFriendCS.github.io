# AH SDD - Animals Part 6


## Design

### UML Class Diagram

![UML clase diagram](assets/diagrams/class5.png)


### Data Dictionary

#### Entity: animal

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

  1 Add a new animal
  2 Register a death
  3 Display oldest animal
  4 Display 10 oldest animals
  5 Display all animals
  
  x Exit
  
Enter choice: 
```


### Structure Diagram


#### Top-level Design

![Structure diagram](assets/diagrams/sd.png)


##### Add a new animal

![Structure diagram](assets/diagrams/sd1.png)


##### Register a death

![Structure diagram](assets/diagrams/sd2.png)


##### Display 10 oldest animals

![Structure diagram](assets/diagrams/sd4.png)
