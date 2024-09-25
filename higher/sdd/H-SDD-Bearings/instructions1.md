# H SDD - Ball Bearings v1


## Introduction

Horve Engineering Ltd produce bearings to exacting requirements.  The quality assurance is carried out manually as so few ball bearnings fail to meet the standard.  If too many of the ball bearings are too big or too small the batch is melted down and the batch is remade.

Unfortunately, there is a blip each year when pupils from the local school undertake a week's work experience.  The number of failures increases and it has become too time consuming to do the quality assurance manually.


## Analysis

Batches of 1,000 ball bearings are now electronically measured, and the results of each ball bearing are stored in a csv file called [bearingsData.csv](assets/earingsData.csv "Download file").

A batch of ball bearings fails when:

    • 5% or more are too big
    • 5% or more are too small
    • 7% or more are too big or too small

The ball bearing specification is 3 cm ± 0.01 cm.


### Assumptions

* The csv file contains the data for 1000 bearings.
* All values in the csv file are in cm.
* The csv file is correctly formatted.


## Top level design (Pseudocode)

```
1.  Read bearings sizes from file              OUT: sizeData()

2.  Calculate how many bearings are too big    IN: sizeData()
                                               OUT: tooBig 

3.  Calculate how many bearings are too small  IN: sizeData()
                                               OUT: tooSmall
											  
4.  Calculate the result and write to file         IN: tooBig, tooSmall							  
```

## Task

Using the program analysis and the design, implement the program in a language of your choice.
