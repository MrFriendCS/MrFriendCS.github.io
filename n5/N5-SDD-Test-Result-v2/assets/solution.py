# Title: N5 SDD Test Result v2
# Author: Mr Friend
# Date: 11 Nov 2021


# start

# set score initially 0
score = 0

# get score from keyboard
score = int(input("Enter test score: "))

# is score >=0 and score <=100
while score < 0 or score >100:
    
    # display "Invalid"
    print("Invalid: 0 to 100")

    # get score from keyboard
    score = int(input("Enter test score: "))

# is score >= 60?
if score >= 60:
    # Yes
    print("Pass")
else:
    # No
    print("Fail")

# end
