# N5 DDD Entity and ERD Design Part 2


## Information

MyPhotoSpace is an online photo gallery stores details of photos displayed on the site in two separate linked tables called `Album` and `Photo`.

To minimise data entry errors, MyPhotoSpace applies the following restrictions:

* Each album can store a maximum of 120 photos
* Five different categories of album are available on the gallery: animals, cars, castles, surfing, and towns

Sample data stored in each table is shown below.


### Album Table

| Album ID | Name             | Category | Description                   | Number of Photos |
| -------- | ----             | -------- | ------------                  | ---------------- |
| 121      | BMW Cars         | Cars     | Photos of BMW cars            | 25 |
| 122      | Glenrothes       | Towns    | Photos from around Glenrothes | 4 |
| 123      | Scottish Castles | Castles  | Photos of Scottish castles    | 17 |


### Photo Table

| Photo ID | Album ID | Title                  | File Name |
| -------- | -------- | -----                  | --------- |
| 23       | 122      | Thirsty Hippos         | hippos_pmckay.jpg |
| 24       | 122      | Glenrothes Irises      | irises_mharris.jpg |
| 31       | 123      | Newark Castle at Night | newark_at_night.png |
| 32       | 122      | Pond at Riverside Park | riverside_park_pong.jpg |


## Tasks

1.  Create a data dictionary for the Album entity.
2.  Create a data dictionary for the Photo entity.
3.  Create an Entity Relationship Diagram, including attributes, to represent the relationship between the Album and Photo entities.
4.  Describe the type of relationship that exists between the Album and Photo entities.
