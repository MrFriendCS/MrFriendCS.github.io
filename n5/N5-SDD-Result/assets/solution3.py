# Title: N5 Test Result v3
# Author: Mr Friend
# Date: 12 Nov 2021

# declare variables
score = 0
grade = ""

# get score from keyboard
score = int(input("Enter test score: "))

# is score >=0 and score <=100
while score < 0 or score >100:
    
    # display "Invalid"
    print("Invalid: 0 to 100")

    # get score from keyboard
    score = int(input("Enter test score: "))

# grade the score
if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "No Award"

# display score
print("Grade: " + grade)
