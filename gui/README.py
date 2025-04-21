# Get extra code
from tkinter import *

def buttonClick():
    """Copies text from the entry field to the label."""
    
    # Get the entry field text
    text = entry.get()
    
    # Change the label text
    label["text"] = text
    

# Create a window - First task
window = Tk()

# Set the initial height and width
window.geometry("220x100")

# Name the window
window.title("Action")


# Create a Label
label = Label(master=window, text="A label", font="Calibri 24 bold")

# Add the label to the window
label.pack()

# Create an entry field
entry = Entry(master=window)

# Add the entry field to the window 
entry.pack()

# Create a button
button = Button(master=window, text="Click me!", border=5, command=buttonClick)

# Add the button to the window 
button.pack(pady=5)


# Display the window - Last task
window.mainloop()
