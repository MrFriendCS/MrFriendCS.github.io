# Get extra code
from tkinter import *

# Create an interface
root = Tk()

# Add a title
root.title("Label - Grid")

# Create labels
myLabel1 = Label(root, text="Hello World 1")
myLabel2 = Label(root, text="Hello World 2")

# Add the labels to the interface
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# Display the GUI
root.mainloop()
