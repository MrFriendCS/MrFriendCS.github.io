# Title: N5 SDD Triathlon
# Author: Mr Friend
# Date: 6 Sep 2024


# Initialise variables and array
min = 0
sec = 0
stages = ["Swim", "T1", "Cycle", "T2", "Run"]
total = 0

# Display header
print("Barra Triathlon")
print("---------------")

# Loop for each stage
for index in range(len(stages)):
    
    min = int(input("\n" + stages[index] + " time (min): "))
    
    sec = int(input(stages[index] + " time (sec): "))
    
    total = total + (min * 60 + sec)
    

print("\nTotal: " + str(round(total / 60)) + " mins")
print("==============")