# https://www.youtube.com/watch?v=mop6g-c5HEY

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Convert")

mainLabel = ttk.Label(master=root, text="Hello", font="Calibri 24 bold")
mainLabel.pack()

inputFrame = ttk.Frame(master=root)

entryInt = tk.IntVar()
entry = ttk.Entry(master=inputFrame, textvariable=entryInt)

button = ttk.Button(master=inputFrame, text="Convert")

entry.pack(side="left", padx=10)
button.pack(side="left", padx=10)

inputFrame.pack()

outputLabel = ttk.Label(master=root, text="Output", font="Calibri 24")
outputLabel.pack()

root.mainloop()