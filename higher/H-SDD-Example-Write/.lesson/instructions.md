# H SDD Example - Write

__NB__. Everything written to a file must be a string.

## Stages

1. Create the file
2. Write to the file
3. Close the file

## File Types

Whilst `.csv` and `.txt` files have different file extensions, they are both text files.  Writing to either type is exactly the same process.

The only difference is that the data is expected to be structured in a csv file, i.e. the values are seperated by commas.  There should be no spaces between the values.

A `.csv` file can be opened by a spreadsheet (Excel), whilst a word processor (Word) can open a `.txt` file.

## Newline

Lines of data or text are completed using the newline escape character:

``` python
"\n"
```
