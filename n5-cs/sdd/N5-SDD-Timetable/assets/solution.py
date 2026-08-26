# Title: N5 SDD Barra Airport Express
# Author: Mr Friend
# Date: 26 Aug 2026

# Initialise variables
start: int = 0
stop: int = 0
step: int = 0

# Header
print("Barra Airport Express")
print("---------------------\n")

# Get earliest departure time
start = int(input("Earliest departure time: "))

while start < 0 or start > 58:
    
    # Display error message
    print("\nThe earliest departure time must be between 0 and 58.")
    
    # Get earliest departure time
    start = int(input("Earliest departure time: "))


# Get latest departure time
stop = int(input("\nLatest departure time: "))

while stop <= start or stop > 59:
    
    # Display error message
    print("\nThe latest departure time must be between " + str(start) + " and 59.")
    
    # Get latest departure time
    stop = int(input("Latest departure time: "))


# Get interval between departures
step = int(input("\nInterval between departures: "))

while step <= 0 or step > 30:
    
    # Display error message
    print("\nThe interval between departure times must be between 1 and 30.")
    
    # Get interval between departures
    step = int(input("\nInterval between departures: "))

# Sub-header
print("\nDeparture times:\n")

# Loop for each bus departure
for time in range(start, stop + step, step):
    
    if time < 10:
        print("\t09:0" + str(time))
        
    else:
        print("\t09:" + str(time))

# Footer
print("\n====================")
