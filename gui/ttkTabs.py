# https://www.youtube.com/watch?v=mop6g-c5HEY

# Get extra code
import tkinter as tk
from tkinter import ttk


def convertm2km():
    """Convert miles to kilometres, to 2 decimal places."""
    
    # Get miles value
    miles = milesInput.get()
    
    # Calculate result
    if len(miles) > 0:
        km = str(round(float(miles) * 1.609344, 2))
    else:
        km = 0
    
    # Display result
    kmOutput["text"] = km


def convertkm2m():
    """Convert kilometres to miles, to 2 decimal places."""
    
    # Get km value
    km = kmInput.get()
    
    # Calculate result
    if len(km) > 0:
        miles = str(round(float(km) / 1.609344, 2))
    else:
        miles = 0
    
    # Display result
    milesOutput["text"] = miles


# Create window
window = tk.Tk()
window.title("ttk Tabs")

# Create notebook
notebook = ttk.Notebook(master=window)
notebook.pack(side="left")

# Create tab 1
tab1 = ttk.Frame(master=notebook)
notebook.add(tab1, text="m2km")


title1 = ttk.Label(master=tab1,
                   text="Miles to km",
                   font="Calibri 24 bold")
title1.pack()

inputArea1 = ttk.Frame(master=tab1)
inputArea1.pack()

milesInput = ttk.Entry(master=inputArea1)
milesInput.pack(side="left")

button1 = ttk.Button(master=inputArea1,
                     text="Convert",
                     command=convertm2km)
button1.pack(side="left")

kmOutput = ttk.Label(master=tab1,
                     text="0",
                     font="Calibri 18")
kmOutput.pack()


# Create tab 2
tab2 = ttk.Frame(master=notebook)
notebook.add(tab2, text="km2m")

title2 = ttk.Label(master=tab2,
                   text="km to Miles",
                   font="Calibri 24 bold")
title2.pack()

inputArea2 = ttk.Frame(master=tab2)
inputArea2.pack()

kmInput = ttk.Entry(master=inputArea2)
kmInput.pack(side="left")

button2 = ttk.Button(master=inputArea2,
                     text="Convert",
                     command=convertkm2m)
button2.pack(side="left")

milesOutput = ttk.Label(master=tab2,
                        text="0",
                        font="Calibri 18")
milesOutput.pack()


# Display GUI
window.mainloop()
