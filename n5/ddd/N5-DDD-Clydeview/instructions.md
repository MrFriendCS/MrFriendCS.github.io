# N5 DDD - Clydeview


File: [Clydeview.db](assets/Clydeview.db "Download file")

## Data dictionaries

### Customer

| Attribute      | Key   | Type    | Size  | Req'd | Validation |
| ---------      | :---: | ----    | :---: | :---: | ---------- |
| customerNo     | PK    | INT     |       | Y     | |
| forename       |       | VARCHAR | 20    | Y     | |
| surname        |       | VARCHAR | 30    | Y     | |
| street         |       | VARCHAR | 50    | Y     | |
| town           |       | VARCHAR | 20    | Y     | |
| package        |       | VARCHAR | 10    | Y     | restricted choice: Standard, Premier, Large |
| directDebit    |       | BOOLEAN |       | Y     | |       
| paymentDueDate |       | DATE    |       | N     | |

