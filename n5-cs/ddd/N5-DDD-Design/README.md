# N5 DDD Entity and ERD Design


## Information

SurfScotland is a blog used by members to share information about surfing in Scotland.
A relational database is used to store details of members and blog posts in two related tables called Member and Post.

* Members must register with SurfScotland and provide an email address before they are allowed to add posts to the blog
* Members must be aged 18 or over
* The number of words in each post is restricted to between 20 and 250 words

Sample data stored in each table is shown below.


### Member Table

    | Member ID | Last Name | First Name | Age in Years | Email |
    | --------- | --------- | ---------- | ------------ | ----- |
    | 1         | Davies    | Jim        | 27           | jimbo31@scotmail.co.uk |
    | 2         | McKay     | Ann        | 28           | mckaya218@hotmail.com |
    | 3         | Roberts   | Carol      | 35           | croberts123@teachers.com |
    | 4         | Singh     | Hardeep    | 24           | singh832@scotmail.co.uk |


### Post Table

    | Post ID | Title                            | Date       | Member ID | Number of Words |
    | ------- | -----                            | ----       | --------- | --------------- |
    | 1       | Welcome to the SurfScotland blog | 2016/08/01 | 1         | 228 |
    | 2       | Belhaven Bay Dunbar              | 2016/08/08 | 1         | 176 |
    | 3       | Coldingham Bay Scottish Borders  | 2016/08/13 | 1         | 58 |
    | 4       | Hebridean Surf Lewis             | 2016/08/15 | 2         | 145 |
    | 5       | Broch Open Surf Competition      | 2016/08/15 | 4         | 73 |


## Design

### Member entity

1.  Complete the data dictionary for the Member entity.

    | Field | Key  | Type | Size | Req’d | Validation |
    | ----- | ---- | ---- | ---- | ----- | ---------- |
    |       |      |      |      |       | |
    |       |      |      |      |       | |
    |       |      |      |      |       | |
    |       |      |      |      |       | |
    |       |      |      |      |       | |


### Post entity

2.  Complete the data dictionary for the Post entity.

    | Field | Key  | Type | Size | Req’d | Validation |
    | ----- | ---- | ---- | ---- | ----- | ---------- |
    |       |      |      |      |       | |
    |       |      |      |      |       | |
    |       |      |      |      |       | |
    |       |      |      |      |       | |
    |       |      |      |      |       | |

3.  Create an Entity Relationship Diagram, including attributes, to represent the relationship between the Member and Post entities.

4.  Describe the type of relationship that exists between the Member and Post entities.
