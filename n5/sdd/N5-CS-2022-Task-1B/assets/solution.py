# Title: N5 CS 2022 Task 1B
# Date: 16 Sep 2023
# Author: Mr Friend

# Initialise variable and arrays
foodWeight = 0.0
foodWeights = [0.0] * 5
averageWeight = 0.0
message = ""

# 1 Enter valid weight of food in each container and calculate total weight

# 1.1 totalWeight = 0
totalWeight = 0.0

# 1.2 start fixed loop 5 times
for index in range(5):
    
    # 1.3 enter the foodWeight
    foodWeight = float(input("Weight " + str(index + 1) + ": "))

    # 1.4 while the foodWeight < 0 or foodWeight > 200
    while foodWeight < 0 or foodWeight > 200:

        # 1.5 display “Invalid, a single container can only hold up to 200g”
        print("Invalid, a single container can only hold up to 200g")
    
        # 1.6 re-enter the foodWeight
        foodWeight = float(input("Weight " + str(index + 1) + ": "))
    
    # 1.7 end while

    # 1.8 totalWeight = totalWeight + foodWeight
    totalWeight = totalWeight + foodWeight

    # Store food weight
    foodWeights[index] = foodWeight
    
# 1.9 end fixed loop


# 2 Enter size of dog
# 2.1 display “Please enter the size of your dog: small, medium or large”
# 2.2 enter size of dog
dogSize = input("\nPlease enter the size of your dog: small, medium or large: ")
    
# 3 Store a message that states if the total weight of food is
#   within the recommended range for the size of dog entered

# 3.1 if dog size = small and totalWeight is from 110 to 140 then
if dogSize == "small" and totalWeight >= 110 and totalWeight <= 140:
    
    # 3.2 store message “This weight of food is suitable for your small dog.”
    message = "This weight of food is suitable for your small dog."

# 3.3 else
else:

    # 3.4 if dog size = medium and totalWeight is from 330 to 440 then
    if dogSize == "medium" and totalWeight >= 330 and totalWeight <= 440:

        # 3.5 store message “This weight of food is suitable for your medium dog.”
        message = "This weight of food is suitable for your medium dog."
    
    # 3.6 else
    else:

        # 3.7 if dog size = large and totalWeight is from 690 to 900 then 
        if dogSize == "large" and totalWeight >= 690 and totalWeight <= 900:

            # 3.8 store message “This weight of food is suitable for your large dog.”
            message = "This weight of food is suitable for your large dog."
        
        # 3.9 else
        else:
            
            # 3.10 store message “This weight of food is not recommended for the size of your dog”
            message = "This weight of food is not recommended for the size of your dog."

        # 3.11 end if
    # 3.12 end if
# 3.13 end if

# 4 Calculate average weight of food
# 4.1  averageWeight = totalWeight / 5
averageWeight = totalWeight / 5

# 4.2  round averageWeight to 1 decimal place
averageWeight = round(averageWeight, 1)

# 5 Display output messages
print()  # Blank line

# 5.1  start fixed loop 5 times
for index in range(5):
    
    # 5.2 display next foodWeight
    print("Weight " + str(index + 1) + ": " + str(foodWeights[index]))
          
# 5.3  end fixed loop
    
# 5.4  display total weight message
print("\nTotal weight: " + str(totalWeight))

# 5.5  display average weight message
print("Average weight: " + str(averageWeight))

# 5.6  display stored recommendation message
print("\n" + message)
