# H DDD Aggregrate Functions

File: [Clydeview.db](../H-DDD-Clydeview/assets/Clydeview.db "Download file")


## Table: Employee

| Name          | Key | Type   | Size | Req'd | Validation |
| ----          | --- | ----   | ---- | ----- | ---------- |
| employeeID    | PK  | Number |      | Y     | |
| jobTitle      |     | Text   | 8    | Y     | |
| name          |     | Text   | 20   |       | |
| building      |     | Text   | 2    |       | |
| yearsEmployed |     | Number | Y    |       | Range: >= 0 |

Use SQL queries to display each set of required details, with appropriate aliases.

1.  Display the number of employees.
2.  List the longest and shortest service of all employees of the company.
3.  List the average years of service of all the employees.
4.  List the job titles and the average years of service for each of those job titles.
5.  List the name of each building and the number of employees who work in it.
6.  List the name of each building and the total years service of all employees who work in that building.
7.  Employees in each building are due a bonus of 100 times the shortest years of service of any employee who works in that building.  List the name of each building and the bonus due.
8.  All of the employees with the same job title are due to receive extra holiday days equivalent to half of the longest years of service for that job title.  List each job title together with the extra holiday days due for those employees.
9.  List the name of each building with the job titles of the employees who work in the building and the number of employees with these job titles.
