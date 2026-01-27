# H CS 2024 - Task 2 Part B


[Swimming Association database](assets/SwimmingAssociation.db)


## Introduction

The National Swimming Association (NSA) collects data of multiple events, races, teams,
and swimmers.


## NSA database

| Event          | Race               | Result              | Swimmer           | Team |
| -----          | ----               | ------              | -------           | ---- |
| <u>eventID</u> | <u>raceNumber </u> | <u>raceNumber* </u> | <u>swimmerID </u> | <u>teamRef </u> |
| eventDate      | raceCategory       | position            | initial           | teamName |
| city           | stroke             | lane                | surname           | headCoach |
| venue          | distance           | <u>swimmerID* </u>  | swimCategory      | assistantCoach |
|                | eventID*           | raceTime            | teamRef*          | |


___2c___  The NSA would like to know the total number of races won by individual swimmers.

Implement the SQL statement to produce the output shown in the table below.

(__4 marks__)

| initial | surname  | swimCategory | teamName         | Races won |
| ------- | -------  | ------------ | -------          | --------- |
| A       | Jackson  | Intermediate | England          | 2 |
| C       | Jones    | Advanced     | Wales            | 1 |
| D       | Chaudhry | Intermediate | England          | 1 |
| F       | Adams    | Advanced     | England          | 4 |
| I       | Arthur   | Intermediate | Scotland         | 2 |
| L       | Kelly    | Advanced     | Northern Ireland | 3 |
| M       | Abbott   | Intermediate | England          | 2 |
| V       | Rose     | Advanced     | Scotland         | 3 |
| W       | Hudson   | Advanced     | Wales            | 2 |

Print evidence of the implemented SQL statement and the output produced.


___2d___  They want to identify the swimmer who swam in lanes 1 or 8 with the fastest time 
from any race. 
 
Implement the SQL statement(s) to produce the result below.

(__4 marks__)


| initial | surname | teamName | city    | eventDate |
| ------- | ------- | -------- | ----    | --------- |
| L       | Bishop  | Scotland | Glasgow | 2024-01-06 |

Print evidence of the implemented SQL statement(s) and the output produced.


___2e___  All swimmers who finish in positions 1, 2 and 3 are awarded medals. 
 
The medal total for each team is shown below.

| teamName         | Total medals won |
| --------         | ---------------- |
| England          | 18 |
| Scotland         | 16 |
| Northern Ireland | 14 |
| Wales            | 12 |

The following query is designed to count and display the number of medals won by each team.

```
SELECT teamName, COUNT(position) AS [Total medals won]
FROM Result, Swimmer, Team
WHERE Result.swimmerID = Swimmer.swimmerID AND Swimmer.teamRef = Team.teamRef
GROUP BY teamName;
```

The query to test the above SQL statement is provided with the database.
When run, the actual output does not match the expected output.

Amend the query to produce the expected output.

(__2 marks__)

Print evidence of the amended SQL statement and the output produced.


__2f__ The end-user requirement below could not be met.

"I need to know the total number of days each city has hosted an event."

Explain, with reference to the database structure, what additional data would be required.

(__1 mark__)
