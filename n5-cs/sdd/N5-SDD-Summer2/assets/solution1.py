# Title: N5 SDD Summer Tasks
# Author: Mr Friend
# Date: 24 Jun 2026

# Initilise variables
number: float = 0.0
root: float = 0.0
result: str = ""

# Header
print("Square Rooter")
print("-------------")


# Get valid value
while number <= 0.0:
    
    # Get value from user
    number = float(input("\nEnter a number: "))

    # Chack value
    if number <= 0.0:
        
        # Display error message
        print("number must be more than zero.")

# Calculate result
root = number ** 0.5

# Round to 3 dp
root = round(root,3)
   
# Display result
print("The square root is " + str(root))

# Footer
print("\n=============")

