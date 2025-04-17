# Get extra code
from tkinter import *
import random


def pickRPS():
    # Local varaibels
    rpsChoices = ["Rock", "Paper", "Scissors"]
    colours = ["red", "blue", "green", "purple", "black"]
    
    # Pick random option
    rpsNum = random.randint(0, 2)

    # Pick random colour
    colourNum = random.randint(0, len(colours) - 1)
    
    # Display selected option
    rps["text"] = rpsChoices[rpsNum]
    
    # Set text colour
    rps["fg"] = colours[colourNum]
        

# Create an interface
root = Tk()

# Add a title
root.title("RPS")

# Create label
rps = Label(root, text = "RPS", padx=10, pady=10)

# Create buttons
play = Button(root, text="Play RPS", padx=10, pady=10, command=pickRPS)

# Add widgets to the interface
rps.pack()
play.pack()

# Display the GUI
root.mainloop()
