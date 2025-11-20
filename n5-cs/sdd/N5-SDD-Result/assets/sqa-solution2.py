# Title: N5 SDD SQA Result Part 2
# Author: Mr Friend
# Date: 23 Oct 2025

# Start

# Initialise Variables
percentage = 0
grade = ""


# Display header
print("SQA Result Calculator")
print("---------------------")


# Get percentage
print()
percentage = int(input("Percentage: "))


# Is percentage >= 70?
if percentage >= 70:
    
    # Set grade to A
    grade = "A"

# Is percentage >= 60?
elif percentage >= 60:
    
    # Set grade to B
    grade = "B"

# Is percentage >= 50?
elif percentage >= 50:

    # Set grade to C
    grade = "C"

# Is percentage >= 40?
elif percentage >= 40:

    # Set grade to D
    grade = "D"

else:
    
    # set grade to No Award
    grade = "No Award"


# Display grade
print()
print("Grade: " + grade)


# Display footer
print()
print("=====================")
