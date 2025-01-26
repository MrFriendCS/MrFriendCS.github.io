# Title: N5 CS 2019 Task 2B
# Date: 23 Jan 2025
# Author: Mr Friend

# Getr extra code
import random

# Initialise variables
endingsIndex = 0
noOfStudents = 0
studentName = ""
studentUsername = ""

# 1. Store the endings
endings = ["ing", "end", "axe", "gex", "goh"]

# 2. Enter the number of students
noOfStudents = int(input("Enter the number of students: "))

# 3. Start fixed loop for each student
for student in range(noOfStudents):

    # Ensure student's name is empty
    studentName = ""
    
    # 4. Enter first three letters of student’s name

    # 4.1. Start conditional loop
    while len(studentName) != 3:
        
        # 4.2. Get the first three letters of student’s name
        studentName = input("\nEnter first 3 letters: ")
    
        # 4.3. If the length of the name is not equal to 3 then
        if len(studentName) != 3:
            
            # 4.4. Display an error message
            print("Must be exactly 3 letters!")

        # 4.5. End If

        # 4.6. Repeat until the name entered is 3 characters long
    
    # 5. Generate random number
    endingsIndex = random.randint(0, 4)
    
    # 6. Generate username

    # 6.1. If the first random number
    if endingsIndex == 0:
        studentUsername = studentName + endings[0]

    # 6.2. If the second random number
    if endingsIndex == 1:
        studentUsername = studentName + endings[1]

    # 6.3. If the third random number
    if endingsIndex == 2:
        studentUsername = studentName + endings[2]

    # 6.4. If the fourth random number
    if endingsIndex == 3:
        studentUsername = studentName + endings[3]

    # 6.5. If the fifth random number
    if endingsIndex == 4:
        studentUsername = studentName + endings[4]
    
    # 7. Display the username
    print("Username: " + studentUsername)

# 8. End Loop
