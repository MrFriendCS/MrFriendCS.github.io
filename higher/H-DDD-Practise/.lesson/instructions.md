# H DDD Practise

## Data Dictionary 1

### Table: datatypes

| Attribute | Key | Req'd | Type | Validation |
| ------- | :---: | :---: | ---- | ---------- |
| rowID | PK | Y | text | |
| integer | | | number | range: >= 1 and <= 100 |
| real | | | number | range: >= 1 and <= 100 |
| date | | | date | range: >= 1900 and <= 2023 |
| time | | | time | |
| boolean | | | Boolean | |

### Table: marathon

| Attribute | Key | Req'd | Type | Validation |
| ------- | :---: | :---: | ---- | ---------- |
| forename | | Y | text | |
| surname | | Y | text | |
| country | | | text | length = 3 |
| number | PK | Y | number | > 0 |
| gender | | Y | text | restricted choice: Men, Women |
| half | | Y | time | |
| finish | | Y | time | |

## Data Dictionary 2

### Table: pupil

| Attribute | Key | Req'd | Type | Validation |
| ------- | :---: | :---: | ---- | ---------- |
| pupil_id | PK | Y | number | > 0 |
| home_id | FK | | number | Exists in address table |
| first_name | | Y | text | |
| last_name | | Y | text | |
| dob | | Y | date | |
| age | | Y | number | >= 0 |
| enrolled | | Y | Boolean | |

### Table: address

| Attribute | Key | Req'd | Type | Validation |
| ------- | :---: | :---: | ---- | ---------- |
| address_id | PK | Y | integer | |
| first_line | | Y | text | |
| town | | Y | text | |
| postcode | | Y | text | |
| phone | | | text | length = 12 |

### Table: staff

| Attribute | Key | Req'd | Type | Validation |
| ------- | :---: | :---: | ---- | ---------- |
| staff_id | PK | Y | number | |
| title | | Y | text | |
| last_name | | Y | text | |
| role | | Y | text | |

### Table: subject

| Attribute | Key | Req'd | Type | Validation |
| ------- | :---: | :---: | ---- | ---------- |
| subject_id | PK | Y | number | |
| subject | | Y | text | |

### Table: teacher

| Attribute | Key | Req'd | Type | Validation |
| ------- | :---: | :---: | ---- | ---------- |
| staff_id | PK / FK | Y | number | Exists in staff table |
| subject | PK / FK | Y | text | Exists in subject table |


## Data Dictionary 3

### Table: port

| Attribute | Key | Req'd | Type | Validation |
| ------- | :---: | :---: | ---- | ---------- |
| port_code | PK | Y | text | length = 3 |
| port_name | | Y | text | |
| local_authority | | Y | text | |
| marine_region | | Y | text | |
| service_type | | Y | text | |

### Table: route

| Attribute | Key | Req'd | Type | Validation |
| ------- | :---: | :---: | ---- | ---------- |
| route_id | PK | Y | text | |
| depart_code | FK | Y | text | Exists in port table |
| arrive_code | FK | Y | text | Exists in port table |
| route | | Y | text | |
| service | | Y | text | |
| ferry_type | | Y | text | |
| seasonal | | Y | text | |
| operator | | Y | text | |
| service_id | | Y | text | |
| service_code | | Y | text | |
| operator_url | | | text | |
| subsidy_type | | | text | |
| subsidy_provider | | | text | |
| distance_miles | | | number | |
| duration_hours | | | number | |
