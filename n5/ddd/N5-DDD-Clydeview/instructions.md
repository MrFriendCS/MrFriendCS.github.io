# N5 DDD - Clydeview


File: [Clydeview.db](assets/Clydeview.db "Download file")

## Data dictionaries

### Customer

| Attribute      | Key   | Type    | Size  | Req'd | Validation |
| ---------      | :---: | ----    | :---: | :---: | ---------- |
| customerNo     | PK    | Number  |       | Y     | |
| forename       |       | Text    | 20    | Y     | |
| surname        |       | Text    | 30    | Y     | |
| street         |       | Text    | 50    | Y     | |
| town           |       | Text    | 20    | Y     | |
| package        |       | Text    | 10    | Y     | Restricted choice: Standard, Premier, Large |
| directDebit    |       | Boolean |       | Y     | |       
| paymentDueDate |       | Date    |       | N     | |

