# N5 SDD - Animals

The Higher Psychology pupils want a program that will give a quick answer to a couple of questions.  Unfortunately, they didn't pick wisely with their choices and don't know how to do it themselves.

## Program Analysis

A program is required that will ask the user their name and age.  It will then ask if they like cats, and then ask if they like dogs.

The answers to all of the questions are to be displayed.  The type of person they are will then be displayed

### Input

* name: must not be left blank
* age: only secondary ages are allowed
* like cats: only ___yes___ or  ___no___ allowed
* like dogs: only ___yes___ or  ___no___ allowed

### Process

* determine the type of person

### Output

* display a data summary
* display the person type

## Type of Person

The program will use someone's answers about whateher they like cats and dogs to determine what type of person they are, as shown in the table below.

| Cats | Dogs | Type |
| :--: | :--: | :--: |
| Yes  | Yes  | Good |
| Yes  | No   | Ok   |
| No   | Yes  | Ok   |
| No   | No   | Evil |


## User Interface

### Example 1

```
Hi!  What is your name? Eli

Hi Eli how old are you? 11

Eli, do you like cats? yes

Eli, do you like dogs? yes

Data Summary
------------
Name: Eli
Age: 11
Like cats: yes
Like dogs: yes

From your answers about animals
I think you're a good person!
```

### Example 2

```
Hi!  What is your name? Bob

Hi Bob how old are you? 18

Bob, do you like cats? no 

Bob, do you like dogs? no

Data Summary
------------
Name: Bob
Age: 18
Like cats: no
Like dogs: no

From your answers about animals
I think you're an evil person!
```

### Example 3

```
Hi!  What is your name? 
Are you shy?

Hi!  What is your name? Jo 

Hi Jo how old are you? 10
Jo! This quiz is only for secondary pupils.

Hi Jo how old are you? 19
Jo! This quiz is only for secondary pupils.

Hi Jo how old are you? 15

Jo, do you like cats? yes

Jo, do you like dogs? maybe
Jo! It's a yes or no question.

Data Summary
------------
Name: Jo
Age: 15
Like cats: yes
Like dogs: no

From your answers about animals
I think you're an ok person!
```

## Assumptions

* All ___yes___ / ___no___ answers will be lower case.
* All ages will be integers.
