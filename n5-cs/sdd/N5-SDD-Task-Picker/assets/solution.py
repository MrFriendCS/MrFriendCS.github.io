# Title: N5 SDD Task Picker
# Author: Mr Friend
# Date: 12 Nov 2026

# Get extra code
import random

# Initialise variables
names: list[str] = ["Ann", "Bob", "Cara", "Dave"]
tasks: list[str] = ["empty the bins.", "wash the car.", "tidy the living room.",
         "feed the cats.", "go food shopping.", "empty the dishwasher"]
numOfTasks: int = 0
name: str = ""
task: str = ""

# Display header
print("Task Picker")
print("-----------")

# Get number of tasks
numOfTasks = int(input("How many tasks? "))

print()

# Loop for each task
for counter in range(numOfTasks):
    
    # Pick a job
    task = tasks[random.randint(0, len(tasks)-1)]
    
    # Pick a name
    name = names[random.randint(0, len(names)-1)]
    
    # Display result
    print(name + " will " + task)

# Display footer
print()
print("Enjoy!")
print("======")
