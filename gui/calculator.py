# Get extra code
from tkinter import *


def getValues():
    # Get values
    num1 = int(value1.get())
    num2 = int(value2.get())
    
    return num1, num2


def displayAnswer(sign, answer):
    # Display symbol
    symbol["text"] = sign
    
    # Display result
    result["text"] = answer


def add():
    # Get values
    num1, num2 = getValues()
    
    # Calculate answer
    answer = num1 + num2
    
    # Display answer
    displayAnswer("+", answer)


def sub():
    # Get values
    num1, num2 = getValues()
    
    # Calculate answer
    answer = num1 - num2
    
    # Display answer
    displayAnswer("-", answer)


def multi():
    # Get values
    num1, num2 = getValues()
    
    # Calculate answer
    answer = num1 * num2
    
    # Display answer
    displayAnswer("×", answer)
    
    
def share():
    # Get values
    num1, num2 = getValues()
    
    # Calculate answer
    answer = num1 / num2
    
    # Display answer
    displayAnswer("÷", answer)


# Create an interface
root = Tk()

# Add a title
root.title("Basic Calculator")

# Create input fields
value1 = Entry(root, width=10, borderwidth=10)
value2 = Entry(root, width=10, borderwidth=10)

# Create labels
symbol = Label(root, text = "   ", padx=10)
result = Label(root, text = "")

# Create buttons
plus = Button(root, text="+", padx=10, pady=10, command=add)
minus = Button(root, text="-", padx=10, pady=10, command=sub)
times = Button(root, text="×", padx=10, pady=10, command=multi)
divide = Button(root, text="÷", padx=10, pady=10, command=share)

# Add widgets to the interface
value1.grid(row=0 , column=0)
symbol.grid(row=0 , column=1)
value2.grid(row=0 , column=2)

result.grid(row=1, column=0, columnspan=3)

plus.grid(row=2, column=0)
minus.grid(row=2, column=2)

times.grid(row=3, column=0)
divide.grid(row=3, column=2)

# Display the GUI
root.mainloop()
