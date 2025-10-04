# Title: N5 SDD SQA Result
# Author: Mr Friend
# Date: 4 Oct 2025

# Start

# Initialise Variables
percentage = 0
grade = ""


# Display header
print("SQA Result Calculator")
print("---------------------")


# Get percentage from keyboard
print()
percentage = int(input("Percentage: "))


# is percentage >= 70?
if percentage >= 70:
    
    # set grade to A
    grade = "A"
    
else:
    
    if percentage >= 60:
    
        # set grade to B
        grade = "B"
    
    else:
        
        if percentage >= 50:
        
            # set grade to C
            grade = "C"
        
        else:
            
            if percentage >= 40:
            
                # set grade to D
                grade = "D"
            
            else:
                
                # set grade to No Award
                grade = "No Award"


# display grade
print()
print("Grade: " + grade)


# Display footer
print()
print("=====================")
