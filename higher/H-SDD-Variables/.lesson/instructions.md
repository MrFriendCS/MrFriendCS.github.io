# H SDD Example - Variables

## Scope

The scope of a variable, where it can be used, can either be global or local.

### Global variables

The scope of a global variable is the whole program, including subprograms.

### Local variables

The scope of a local variable is only within the subprogram where it is declared.  The memory used by a local variable is released when the subprogram is finished.

The name of a local variable can be the same as a global variable, or local variables in other subprograms.  This allows subprograms to be reused in other programs without modification.

## Global Variables in Subprograms

Global are not automatically available in subprograms.  It is possible make them available by using the `global` keyword followed by the name of the global variable.

``` python
global variableName
```

Any changes to the variable within the subprogram will affect the value of the variable in the main program.
