# Title: N5 SDD - Result Part 3
# Author: Mr Friend
# Date: 16 Nov 2026

# Initialise variables
score: int = 0
result: str = ""

# Display header
print("Test Result")
print("-----------")
print()

# Get score from user
score = int(input("Score: "))

# Repeat until score is 0 to 100
while score < 0 or score > 100:
    
    # Blank line
    print()
    
    # Display error message
    print("Only scores from 0 to 100 can be used.")

    # Get score from user
    score = int(input("Score: "))
    
# Is score >= 50?
if score >= 50:
    
    result = "Pass"
    
else:
    
    result = "Fail"

# Blank line
print()

# Display result
print("Result: " + result)

# Display footer
print()
print("============")
