# H DDD GitHub Database

For use with DDD notes on [GitHub](https://mrfriendcs.github.io/H-CS-DDD.html).

## ER Diagram

![ER Diagram](assets/H-CS-DDD.png)

## Data Dictionary

### Table: pet

| Attribute | Key | Req'd | Type | Validation | Example |
| ------- | :---: | :---: | ---- | ---------- | ------- |
| pet_id | PK | Y | number | >= 1 | 2 |
| name | | Y | text | | Minnie |
| species | | Y | text | | Gerbil |
| dob | | | text | length = 10 | 2021-05-24 |

### Table: vaccination

| Attribute | Key | Req'd | Type | Validation | Example |
| ------- | :---: | :---: | ---- | ---------- | ------- |
| pet_id | PK/FK | Y | integer | Exists in pet table | 2 |
| vax_id | PK/FK | Y | number | Exists in vaccine table | 3 |
| vax_date | PK | Y | text | length = 10 | 2021-11-06 |
| reaction | | Y | integer | 0 or 1 | 0 |
| paid | | Y | integer | 0 or 1 | 1 |

### Table: vaccine

| Attribute | Key | Req'd | Type | Validation | Example |
| ------- | :---: | :---: | ---- | ---------- | ------- |
| vax_id | PK | Y | number | >= 1 | 2 |
| name | | Y | text | | Cat Flu |
| cost | | Y | number | >= 0 | 19.30 |
