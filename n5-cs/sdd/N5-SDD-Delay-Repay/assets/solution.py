# Title: N5 SDD Delay Repay
# Author: Mr Friend
# Date: 26 Oct 2026

# Initialise Variables
price: float = 0.0
rate: int = 0
arrHour: int = 0
arrMins: int = 0
actHour: int = 0
actMins: int = 0
minsArr: int = 0
minsAct: int = 0
delay: int = 0
compensation: float = 0.0

# Header
print("BUTL Delay Repay")
print("----------------")

# Get ticket price
print()
price = float(input("Ticket price: £"))

# Timetabled arrival time
print()
print("Timetabled arrival time:")
arrHour = int(input("  Hour: "))
arrMins = int(input("  Mins: "))

# Timetabled actual time
print()
print("Actual arrival time:")
actHour = int(input("  Hour: "))
actMins = int(input("  Mins: "))

# Convert to minutes
minsArr = (arrHour * 60) + arrMins
minsAct = (actHour * 60) + actMins

# Calculate delay
delay = minsAct - minsArr

# Determine compensation rate
if delay >= 60:
    rate = 100
    
elif delay >= 30:
    rate = 50
    
elif delay >= 15:
    rate = 25

# Calculate compensation
compensation = price * (rate / 100)

# Round compensation
compensation = round(compensation, 2)

# Display delay
print()
print("Delay: " + str(delay) + " mins")

# Display compensation rate
print("  Rate: " + str(rate) + "%")

# Display compensation
print("  Compensation: £" + str(compensation))

# Footer
print("================")
