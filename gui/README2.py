# Title: Tkinter - Grid
# Author: Mr Friend
# Date: 23 Apr 2025

# Get extra code
import tkinter as tk


def convertC():
    """Convert centigrade to Fahrenheit to 1 dp."""
    
    # Get the entry field text
    degC = float(entry.get())
    
    # Convert C to F
    degF = round(degC * (9/5) + 32, 1)
    
    # Change the label text
    label["text"] = degF


def convertF():
    """Convert Fahrenheit to centigrade to 1 dp."""
    
    # Get the entry field text
    degF = float(entry.get())
    
    # Convert C to F
    degC = round((degF - 32) * (5/9), 1)
    
    # Change the label text
    label["text"] = degC


# Create a window - First task
window = tk.Tk()

# Set the initial position: x and y
window.geometry("+400+300")

# Name the window
window.title("Convert")


# Create a Label
label = tk.Label(master=window, text="?", font="Calibri 24 bold")

# Add the label to the window
label.grid(row=0, column=0, columnspan=2)

# Create an entry field
entry = tk.Entry(master=window, fg="blue", bg="pink", font="Consolas 14")

# Add the entry field to the window 
entry.grid(row=1, column=0, columnspan=2)



# Create C to F button
buttonC = tk.Button(master=window,
                    text="C to F",
                    border=5,
                    width=12, 
                    command=convertC)

# Add the button to the window 
buttonC.grid(row=2, column=0, padx=5, pady=5)

# Create F to C button
buttonF = tk.Button(master=window,
                    text="F to C",
                    border=5,
                    width=12,
                    command=convertF)

# Add the button to the window 
buttonF.grid(row=2, column=1, padx=5, pady=5)


# Display the window - Last task
window.mainloop()
