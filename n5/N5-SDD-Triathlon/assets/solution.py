# Title: N5 SDD Triathlon
# Author: Mr Friend
# Date: 6 Sep 2024

# Initialise variables and array
min = 0
sec = 0
stages = ["Swim", "T1", "Cycle", "T2", "Run"]
totalTime = 0

# Display header
print("\nBarra Triathlon")
print("---------------")

print("\nEnter times for each stage:")

# Loop for each stage
for index in range(len(stages)):
    
    # Get valid time - minutes
    min = int(input("\n" + stages[index] + " time (min): "))
    
    while min < 0:
        # Display error message
        print("\nNo negative minutes allowed!")
        
        # Get valid time - minutes
        min = int(input("\n" + stages[index] + " time (min): "))

    # Get valid time - seconds
    sec = int(input(stages[index] + " time (sec): "))
    
    while sec < 0 or sec >= 60:
        # Display error message
        print("\nSeconds must be 0 to 59")
        
        # Get valid time - seconds
        sec = int(input(stages[index] + " time (sec): "))
    
    # Update total time in seconds
    totalTime = totalTime + (min * 60 + sec)

# Convert total time to minutes - round to nearest minute
timeMins = round(totalTime / 60)

# Display result
print("\nTotal: " + str(timeMins) + " mins")
print("==============")