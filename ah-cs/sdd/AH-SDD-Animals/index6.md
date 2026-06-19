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


### Structure Diagram

![Structure diagram](assets/diagrams/sd.png)

![Structure diagram](assets/diagrams/sd1.png)


### UI

```
Barra Zoo
---------

Menu:

  1 Add an animal
  2 Register a death
  3 Display oldest animal
  4 Display 10 oldest animals
  5 Display all animals
  
  x Exit
  
Enter choice: 
```
