# N5 DDD Query Implementation - Equi-join

File: [Clydeview.db](../N5-DDD-Clydeview/assets/Clydeview.db "Download file")


## Introduction

ClydeVet veterinary practice uses a relational database store details pets and their owners in two separate tables called `Owner` and `Pet`.


## Entity Relationship Diagram (ERD)

The structure of the tables is shown below.

![ERD](assets/erd1.png)


## Tasks

1.  List the full name and address, and name of their pets, for all of the cat owners.
2.  List the full name and contact telephone number, with the codes of their pets, for all tortoise owners.
3.  List the full name and address, and the name of their pets, of all owners who have pets that have not yet received their vaccinations.
4.  List the name, type of each pet and town of any pet whose owner lives in Greenock.
5.  List the name, vaccination details and contact telephone number of their owner, of all pets whose owners live in Gourock.
6.  Display the full names of all of the owners with the name and type of their pets.
These details should be displayed in alphabetical order of owner surname.
7.  Display the name and full address (inc town) of each pet.
These details should be arranged in alphabetical order of town; pets who live in the same town should be arranged in alphabetical order of pet type.
8.  Display name, pet type, town and dateOfBirth of all the cats; details of the youngest pet should be displayed first.
