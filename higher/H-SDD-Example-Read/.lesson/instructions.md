# H SDD Example - Read

__NB__. Everything read from a file is a string.

## Stages

1. Open the file
2. Read from the file
3. Close the file

## File Types

Whilst `.csv` and `.txt` files have different file extensions, they are both text files.  Reading from either type is the same process.

The only difference is that the data is expected to be structured in a csv file, i.e. the values are seperated by commas, and there should be no spaces between the values.  This allows the data to be assigned to parallel arrays.


## Array Length

Arrays should be declared that are long enough to store the required amount of data, but no bigger.

It is possible to:

* Declare the arrays first, and use every element
* Declare the arrays first, and use some of the elements
* Determine how big the arrays will need to be, and then declare the arrays

The example code declares the arrays first, and then only uses some of the elements.  This will allow data in the file to increase or decrease without neededing to change the code, unless more elements are needed than initially declared.
