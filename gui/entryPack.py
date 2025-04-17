# Get extra code
from tkinter import *


def myClick():
    # Get input field value
    myValue = myInput.get()
     
    # Create a label
    myLabel = Label(root, text="Hello "+myValue, bg="blue", padx=10, pady=10)
    
    # Add the label to the interface
    myLabel.pack()


# Create an interface
root = Tk()

# Add a title
root.title("Input Field")

# Create an input field
myInput = Entry(root, width=20, borderwidth=10)

# Add the input field to the interface
myInput.pack()

# Create a button
myButton = Button(root, text="Enter Your Name", fg="red", padx=10, pady=10, command=myClick)

# Add the button to the interface
myButton.pack()

# Display the GUI
root.mainloop()
