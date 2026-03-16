# Title: Rock, Paper, Scissors
# Date: 8 Oct 2022
# Author: Mr Friend

#
# Import modules
#

import tkinter as tk
from tkinter import ttk
import random

#
# Functions and Procedures
#

def play(choice):
    
    # Declare local variables
    computerChoice = 0
    computer = ""
    result = ""
    
    # Update human label text
    lblHuman2["text"] = choice
    
    # Computer
    computerChoice = random.randint(0, 2)
    computer = choices[computerChoice]
    
    # Update computer label text
    lblComputer2["text"] = computer
    
    result = whoWon(choice, computer)
    
    lblResult["text"] = result
    

def whoWon(human, computer):
    # Declare local variable
    result = ""
    h = ""
    c = ""
    
    # Get first letter of each choce    
    h = human[0]
    c = computer[0]
    
    # Decide result
    
    # Calculate results
    if h == c:
        result = "Draw!"

    elif h == "R" and c == "P":
        result = "Computer wins!"

    elif h == "R" and c == "S":
        result = "Human wins!"

    elif h == "P" and c == "R":
        result = "Computer wins!"

    elif h == "P" and c == "S":
        result = "Human wins!"

    elif h == "S" and c == "R":
        result = "Computer wins!"

    else:
        result = "Human wins!"
    
    # Return the result
    return result

#
# Main Program
#    

# Declare global array
choices = ["Rock", "Paper", "Scissors"]

# Create root window
root = tk.Tk()
#root.geometry("275x150")
root.title("Rock, Paper, Scissors")
root.resizable(False, False)

# Rock button
btnRock = ttk.Button(root, text="R", command=lambda: play("Rock"))
btnRock.grid(column=0, row=0, padx=5, pady=5)

# Paper button
btnPaper = ttk.Button(root, text="P", command=lambda: play("Paper"))
btnPaper.grid(column=1, row=0, padx=5, pady=5)

# Scissors button
btnScissors = ttk.Button(root, text="S", command=lambda: play("Scissors"))
btnScissors.grid(column=2, row=0, padx=5, pady=5)

# Your choice labels
lblHuman1 = ttk.Label(root, text="You: ")
lblHuman1.grid(column=0, row=1, padx=5, pady=5)

lblHuman2 = ttk.Label(root, text="")
lblHuman2.grid(column=1, row=1, padx=5, pady=5)

# My choice labels
lblComputer1 = ttk.Label(root, text="Me: ")
lblComputer1.grid(column=0, row=2, padx=5, pady=5)

lblComputer2 = ttk.Label(root, text="")
lblComputer2.grid(column=1, row=2, padx=5, pady=5)

# Result Frame
frmResult = ttk.Frame(root, borderwidth=10)
frmResult["relief"] = "ridge"
frmResult.grid(columnspan=3, row=3)

# Result label
lblResult = ttk.Label(frmResult, text="???")
lblResult.pack(fill=tk.BOTH)


# Display GUI
root.mainloop()
