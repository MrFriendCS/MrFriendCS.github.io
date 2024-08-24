# N5 DDD - Salon

## Data Dictionary

### Entity: Hairdresser

| Attribute     | Key   | Type   | Size  | Req'd | Validation |
| ---------     | :---: | ----   | :---: | :---: | ---------- |
| hairdresserid | PK    | number |       | Y     |            |
| firstname     |       | text   | 20    | N     |            |
| lastname      |       | text   | 30    | N     |            |
| contactnumber |       | text   | 13    | Y     | length: >= 11 |
| salon         |       | text   | 30    | N     |            |

### Entity: Client

| Attribute     | Key   | Type   | Size  | Req'd | Validation |
| ---------     | :---: | ----   | :---: | :---: | ---------- |
| clientid      | PK    | number |       | Y     |            |
| hairdresserid | FK    | number |       | Y     | Exists in Hairdresser table |
| firstname     |       | text   | 20    | N     |            |
| lastname      |       | text   | 30    | N     |            |
| contactnumber |       | text   | 13    | Y     | length: >= 11 |

## Tasks

1. Display all the information in the Hairdresser table.

2. Add a Barra / Vatersay hairdresser to the table.

3. Create a query that will show what you have added to the hairdresser table.

4. Display all the information in the Client table.

5. Add yourself as a client of the Barra / Vatersay hairdresser.  Use a false phone number.

6. Create a query that will show you have been added to the client table.

7. Create a query that connects hairdressers to their clients.  It will display:

    * Hairdressers' forenames, surnames, and contact numbers

    * Clients' forenames, surnames, and contact numbers

8. Add two more people as clients of the Barra / Vatersay hairdresser.  Use false phone numbers.

9. Create a query that has the same columns as Question 6 but only show the information for the Barra / Vatersay hairdresser that you added.

