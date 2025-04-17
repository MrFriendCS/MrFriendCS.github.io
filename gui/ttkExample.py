# https://www.youtube.com/watch?v=mop6g-c5HEY

# Get extra code
import tkinter as tk
from tkinter import ttk

def convert():
    km.set(str(miles.get() * 1.61))

# Create GUI
window = tk.Tk()
window.title("Convert")
window.geometry("240x160")

# Title
mainLabel = ttk.Label(master=window, text="Miles to km", font="Calibri 24 bold")
mainLabel.pack()

# Input
inputFrame = ttk.Frame(master=window)

miles = tk.IntVar()
entry = ttk.Entry(master=inputFrame, textvariable=miles)
entry.pack(side="left", padx=10)

button = ttk.Button(master=inputFrame, text="Convert", command=convert)
button.pack(side="left", padx=10)

inputFrame.pack(pady=10)

# Output
km = tk.StringVar()
outputLabel = ttk.Label(master=window, textvariable=km, font="Calibri 24")
outputLabel.pack()

# Display GUI
window.mainloop()