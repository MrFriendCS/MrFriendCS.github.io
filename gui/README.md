# Python Graphical User Interface - Tkinter


## Create a blank GUI

``` python
# Get extra code
from tkinter import *

# Create a window - First task
window = Tk()


#
# Widget(s) go here
#


# Display the window - Last task
window.mainloop()
```

![Blank GUI](assets/window.png "Blank GUI")


## Widgets

Widgets are added to the GUI in two stages:

* Create the widget
* Add the widget

### Creating a Widget

Widgets are created with a number of parameters:

* master: what it will be added to.  Can be another widget.
* text: the text to be displayed.
* padx: extra padding to left and right.
* padx: extra padding above and below.
* fg: text colour.
* bg: background colour.
* width: widget width.
* borderwidth: border width.
* command: function to be called.

Not every parameter work with every widget.


### Adding a Widget

Widgets can be added using either the `pack()` or `grid()` method.

The `pack()` method adds the widgets in order, working down the screen.

The `grid()` method adds widgets at a specific location, using rows and columns.

The same method must be used to add widgets to the window.

### Add a Label

``` python
# Create a Label
label = Label(master=window, text="A label")

# Add the label to the window
label.pack()
```

![Label](assets/label.png "GUI with a label")

