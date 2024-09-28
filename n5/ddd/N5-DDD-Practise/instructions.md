# N5 DDD Practise


File: [Practise.db](assets/Practise.db "Download file")


## Data Dictionary

### Entity: pupil

| Attribute  | Key   | Type    | Size  | Req'd | Validation |
| ---------  | :---: | ----    | :---: | :---: | ---------- |
| pupil_id   | PK    | number  |       | Y     |            |
| address_id | FK    | number  |       | N     | Exists in address table |
| first_name |       | text    | 20    | Y     |            |
| last_name  |       | text    | 30    | Y     |            |
| dob        |       | date    |       | Y     |            |
| age        |       | number  |       | Y     | range: >= 0 |
| enrolled   |       | boolean |       | Y     |            |


### Entity: address

| Attribute  | Key   | Type   | Size  | Req'd | Validation |
| ---------  | :---: | ----   | :---: | :---: | ---------- |
| address_id | PK    | number |       | Y     |            |
| first_line |       | text   | 30    | Y     |            |
| town       |       | text   | 30    | Y     |            |
| postcode   |       | text   | 8     | Y     | length: >= 6 |
| phone      |       | text   | 12    | N     |            |


### Entity: marathon

| Attribute | Key   | Type   | Size  | Req'd | Validation |
| --------- | :---: | ----   | :---: | :---: | ---------- |
| surname   |       | text   | 30    | Y     |            |
| forename  |       | text   | 20    | Y     |            |
| country   |       | text   | 3     | N     | length = 3 |
| number    | PK    | number |       | Y     | range: > 0 |
| category  |       | text   | 10    | Y     |            |
| gender    |       | text   | 1     | Y     | restricted choice: M, F |
| half      |       | time   |       | N     |            |
| finish    |       | time   |       | N     |            |


### Entity: datatypes

| Attribute | Key   | Type    | Size  | Req'd | Validation |
| --------- | :---: | ----    | :---: | :---: | ---------- |
| rowID     | PK    | number  |       | Y     |            |
| colour    |       | text    | 10    | N     | length: >= 3 |
| score     |       | number  |       | N     | range: >= 0 and <= 100 |
| height    |       | number  |       | N     | range: >= 1.0 and <= 2.0 |
| date      |       | date    |       | N     | range: >= 1900-01-01 and <= 2023-12-31 |
| time      |       | time    |       | N     |            |
| nice      |       | boolean |       | N     |            |


### Entity: taxi

| Attribute  | Key   | Type   | Size  | Req'd | Validation |
| ---------  | :---: | ----   | :---: | :---: | ---------- |
| taxi_id    | PK    | number |       | Y     |            |
| taxi_reg   |       | text   | 8     | Y     |            |
| make       |       | text   | 20    |       |            |
| model      |       | text   | 20    |       |            |
| colour     |       | text   | 15    |       |            |


### Entity: journey

| Attribute    | Key   | Type   | Size  | Req'd | Validation |
| ---------    | :---: | ----   | :---: | :---: | ---------- |
| journey_id   | PK    | number |       | Y     |            |
| taxi_id      | FK    | number |       | Y     |            |
| pick_up_date |       | date   |       | N     |            |
| pick_up_time |       | time   |       | N     |            |
| pax          |       | number |       | N     |            |
| pick_up_loc  |       | text   | 30    | N     |            |
| drop_off_loc |       | text   | 30    | N     |            |
