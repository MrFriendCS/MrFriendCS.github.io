# Title: N5 Test Result v4
# Author: Mr Friend
# Date: 12 Nov 2021

# Initialise variables
score = 0
total = 0
average = 0.0
grade = ""

# Repeat 3 times
for counter in range(3):

    # get score from keyboard
    score = int(input("Enter test score: "))

    # Get valid score
    while score < 0 or score >100:
        
        print("Invalid: 0 to 100")
        score = int(input("Enter test score: "))

    # Add score to total
    total = total + score

# Calculate average
average = total / 3

# Round average to 0 dp
average = round(average)

# Calculate grade
if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "No Award"

# Display average grade
print("Average: " + str(average))
print("Grade: " + grade)
