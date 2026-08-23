# Title: N5 SDD Youth Club
# Author: Mr Friend
# Date: 23 Aug 2026

# Initialise variables
name: str = ""
names: list[str] = []

# Header
print("Activity Registration")
print("---------------------\n")


# Get names
while name != "x":
    
    # Get name from user
    name = input("Enter a name or 'x' to exit: ")

    # Check value
    if len(name) < 3 and name != "x":
        
        # Display error message
        print("Name must be at least 3 letters long or 'x'.")
    
        # Get name from user
        name = input("Enter a name or 'x' to exit: ")
    
    # Add name to list of names
    if name != "x":
        
        # Concatenate name to array
        names = names + [name]
        

# Display names
print("\nThe following have signed up:\n")

# Loop for each name in array
for name in names:
    
    # Display name
    print("  " + name)

# Footer
print("\n=====================")

