# Python Graphical User Interface - Tkinter


## Create a blank GUI

``` python
# Get extra code
from tkinter import *

# Create a window - First task
window = Tk()

# Set the initial height and width
window.geometry("320x240")

# Name the window
window.title("Blank GUI")


#
# Widget(s) go here
#


# Display the window - Last task
window.mainloop()
```

![Blank GUI](assets/blank.png "Blank GUI")


## Widgets

Widgets are added to the GUI in two stages:

1. Create the widget
2. Add the widget

### Creating a Widget

Widgets can be created with a number of parameters:

* `master`: what it will be added to.  Can be another widget.
* `text`: the text to be displayed.
* `font`: text style and size
* `fg`: text colour.
* `bg`: background colour.
* `command`: function to be called.

Not every parameter works with every widget.


### Adding a Widget

Widgets can be added using either the `pack()` or `grid()` method.

The `pack()` method adds the widgets in order, from top to bottom.

The `grid()` method adds widgets at a specific location, using rows and columns.

Only one method can be used to add widgets to the window.

Widgets can be added with a number of parameters:

* `padx`: extra padding to the left and right.
* `padx`: extra padding above and below.

`pack()` method parameters:

* `side`: where the widget goes - left, right, bottom, top (default)

`grid()` method parameters:

* `row`: position
* `column`: position
* `rowspan`: how many rows to be used, if more than 1.
* `columnspan`: how many columns to be used, if more than 1.

### Add a Label

``` python
# Create a Label
label = Label(master=window, text="A label", font="Calibri 24 bold")

# Add the label to the window
label.pack()
```

![Label](assets/label.png "GUI with a label")


### Add an Entry Field

``` python
# Create an entry field
entry = tk.Entry(master=window, fg="blue", bg="pink")

# Add the entry field to the window 
entry.pack()
```

![Label](assets/entry.png "GUI with entry field")

### Add a Button

``` python
# Create a button
button = Button(master=window, text="Click me!", border=5)

# Add the button to the window 
button.pack(pady=5)
```

![Label](assets/button.png "GUI with a button")

### Add an Action to the Button

Create a function.

``` python
def buttonClick():
    """Copies text from the entry field to the label."""
    
    # Get the entry field text
    text = entry.get()
    
    # Change the label text
    label["text"] = text
```

Update the button to add the function.

``` python
button = Button(master=window, text="Click me!", border=5, command=buttonClick)
```

![Label](assets/action.png "GUI with an action")
