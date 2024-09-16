# Title: N5 CS Specimen Old Task 2
# Author: Mr Friend
# Date: 16 Sep 2024

# Initialise variables
score = 0
hits = [0] * 6
total = 0
average = 0.0
points = 0

#  Get 6 valid hits from players
for index in range(6):
    score = int(input("Player " +str(index + 1) + ". How many hits? "))

    while score < 0 or score > 30:
        print("\nHits must be from 0 to 30")
        score = int(input("Player " +str(index + 1) + ". How many hits? "))
    
    hits[index] = score

# Calculate total hits for 6 players
for index in range(6):
    total = total + hits[index]

# Calculate average hits
average = total / 6

# Round average hits to 2 decimal places
average = round(average, 2)

# Calculate points earned
if total > 50:
    points = points + 1

if average >= 10:
    points = points + 1

# 1 point earned?
if points == 1:
    # Yes - display message - 1 point was earned
    print("\n1 point was earned")

# 2 points earned?
if points == 2:
    # Yes - display message - additional point was earned
    print("Additional point was earned")

# 0 points earned?
if points == 0:
    # Yes - display message - no points were earned
    print("\nNo points were earned")

# End
