# Title: Dice Roller
# Author: Mr Friend
# Date: 11 Oct 2022

# Import modules
import tkinter as tk
from tkinter import ttk
from random import randint

#
# Function
#

def rollDice():
    '''Picks a random number and displays it'''
    #lblDice.config(text = "?")
    
    # Pick a random number
    dice = randint(1, 6)
    diceText = str(dice)
    
    # Update text
    lblDice.config(text = diceText)

#
# Main program
#
    
# Create root window
root = tk.Tk()

# Set up root window
root.geometry("300x200")
root.resizable(False, False)
root.title("Dice Roller")
root.iconbitmap("assets/Dice.ico")

# Label for the dice value
lblDice = ttk.Label(root, text='???', font = ("Arial", 60))
lblDice.pack(ipadx=0, ipady=20)

# Button to roll dice
btnRoll = ttk.Button(root, text="Roll", command=rollDice)
btnRoll.pack(ipadx=0, ipady=5)

# Start the GUI
root.mainloop()
