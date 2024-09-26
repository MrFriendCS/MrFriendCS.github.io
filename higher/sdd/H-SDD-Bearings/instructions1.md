# H SDD - Bearings Part 1


## Introduction

Horve Engineering Ltd produce ball bearings to exacting requirements.  The quality assurance is carried out manually as so few ball bearings fail to meet the standard.  If too many are too big or too small the batch is melted down and the batch remade.

Unfortunately, there is a blip each year when pupils from the local school undertake a week's work experience.  The number of failures increases and it has become too time consuming to do the quality assurance manually.


## Analysis

Batches of 1,000 ball bearings are now electronically measured, and the results of each ball bearing are stored in a csv file called [bearingsData.csv](assets/bearingsData.csv "Download file").

A batch of ball bearings fails when:

* 2% or more are too small
* 2% or more are too big
* 3% or more are too big or too small

The ball bearing specification is 3 cm ± 0.01 cm.

The sizes of the smallest and largest bearings are to be included in the results.

The results of the batch are to be written to `batchResult.txt`.  An example is shown below:

```
Batch Result
------------

Min: 2.089 cm
Max: 3.102 cm

Too small: 1.6%
Too big:   1.5%
Total:     3.1%

FAIL
====
```


### Assumptions

* The csv file contains the data for 1,000 bearings.
* All values in the csv file are in cm.
* The csv file is correctly formatted.
* The global variable `result` is Boolean.


## Top level design (Pseudocode)

```
1.  Read bearings sizes from file           OUT: sizeData()

2.  Determine size of smallest bearing      IN: sizeData()
                                            OUT: min

3.  Determine size of largest bearing       IN: sizeData()
                                            OUT: max
											   
4.  Count how many bearings are too small   IN: sizeData()
                                            OUT: small
											   
5.  Count how many bearings are too big     IN: sizeData()
                                            OUT: big
												
6.  Calculate percentage of small bearings  IN: small
      to 2 decimal places                   OUT: smallPercent
											
7.  Calculate percentage of big bearings    IN: big
      to 2 decimal places                   OUT: bigPercent
												
8.  Calculate batch result                  IN: smallPercent, bigPercent
                                            OUT: result
											  
9.  Write data to file                      IN: min, max, smallPer, bigPer, result					  
```


## Task

Using the program analysis and the design, implement the program in a language of your choice.


## Testing

Run the file [Bearings1-Test.py](assets/Bearings1-Test.py "Download file"). The file must be in the same folder as `bearings1.py`.
