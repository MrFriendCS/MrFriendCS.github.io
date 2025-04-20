# https://www.youtube.com/watch?v=mop6g-c5HEY

# Get extra code
import tkinter as tk

def convert():
    km.set(str(round(miles.get() * 1.609344, 2)))

# Create GUI
window = tk.Tk()
window.title("tk Convert")
window.geometry("240x160")

# Title
mainLabel = tk.Label(master=window, text="Miles to km", font="Calibri 24 bold")
mainLabel.pack()

# Input
inputFrame = tk.Frame(master=window)

miles = tk.IntVar()
entry = tk.Entry(master=inputFrame, textvariable=miles)
entry.pack(side="left", padx=10)

button = tk.Button(master=inputFrame, text="Convert", command=convert)
button.pack(side="left", padx=10)

inputFrame.pack(pady=10)

# Output
km = tk.StringVar()
outputLabel = tk.Label(master=window, textvariable=km, font="Calibri 24")
outputLabel.pack()

# Display GUI
window.mainloop()