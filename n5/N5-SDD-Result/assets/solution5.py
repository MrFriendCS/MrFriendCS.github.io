# Title: N5 Test Result v5
# Author: Mr Friend
# Date: 12 Nov 2021

# Initialise variables and array
score = 0
total = 0
average = 0.0
grade = ""
scores = [0] * 3

# Repeat 3 times
for index in range(len(scores)):

    # get score from keyboard
    score = int(input("Enter test score: "))

    # Get valid score
    while score < 0 or score >100:
        
        print("Invalid: 0 to 100")
        score = int(input("Enter test score: "))

    # store score
    scores[index] = score
    
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

print()
print("Valid scores entered")
print()

# Display scores
for index in range(len(scores)):
    print("Score " + str(index + 1) + ": " + str(scores[index]))

# Display average grade
print("Average: " + str(average))
print("Grade: " + grade)
