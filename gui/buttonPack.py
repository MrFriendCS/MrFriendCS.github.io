# Get extra code
from tkinter import *


def myClick():
    # Create a label
    myLabel = Label(root, text="Hello again!", bg="blue", padx=10, pady=10)
    
    # Add the label to the interface
    myLabel.pack()


# Create an interface
root = Tk()

# Add a title
root.title("Button")

# Create a button
myButton = Button(root, text="Hello World!", fg="red", padx=10, pady=10, command=myClick)

# Add the button to the interface
myButton.pack()

# Display the GUI
root.mainloop()
