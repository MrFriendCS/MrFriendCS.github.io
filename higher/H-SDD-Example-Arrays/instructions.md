# H SDD Example - Arrays

__NB__. Python lists are used as pretend arrays for the purpose of SQA qualifications.

## Scope

The scope of an array, where it can be used, can either be global or local.

### Global arrays

The scope of a global variable is the whole program, including subprograms.

### Local arrays

The scope of a local array is only within the subprogram where it is declared.  The memory used by a local array is released when the subprogram is finished.

The name of a local array can be the same as a global array, or local arrays in other subprograms.  This allows subprograms to be reused in other programs without modification.

## Global Arrays in Subprograms

Global arrays are automatically available in subprograms.

Any changes to the array within the subprogram will affect the value of the array in the main program.
