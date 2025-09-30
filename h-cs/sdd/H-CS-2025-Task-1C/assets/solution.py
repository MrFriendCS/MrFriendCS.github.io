# Title: H CS 2025 Task 1 Part C
# Author: Mr Friend
# Date: 24 Jan 2025

# Get extra code
from dataclasses import dataclass

@dataclass
class Order:
    """A record to represent an order."""
    orderNum: str = ""
    date: str = ""
    email: str = ""
    option: str = ""
    cost: float = 0.0
    rating: int = 0


def getData():
    """Read from file into array of records."""
    # OUT orders(orderNum,date,email,option,cost,rating) 
    
    # Intilise local variables
    orders = [Order() for index in range(505)]
    data = [""] * 6
    line = ""

    # Make a connection to the file
    file = open("orders.txt" ,"r" )

    # Loop for each line in the file
    for index in range(len(orders)):

        # Read a line from the file
        line = file.readline()

        # Split the line at the commas
        data = line.split(",")

        # Remove non-printing characters, cast as appropriate, assign to data structure
        orders[index].orderNum = data[0].strip()
        orders[index].date = data[1].strip()
        orders[index].email = data[2].strip()
        orders[index].option = data[3].strip()
        orders[index].cost = float(data[4].strip())
        orders[index].rating = int(data[5].strip())

    # Close the connection to the file
    file.close()
    
    # Return array of records
    return orders
    

def findRating(orders):
    """Find the position of the customer who gave the first 5-star rating in a given month."""
    # IN orders(orderNum,date,email,option,cost,rating) 
    # OUT position
    
    # Intilise local variables
    target = ""
    month = ""
    rating = 0
    
    # 2.1 Set position to -1
    position = -1
    
    # 2.2 Set index to 0
    index = 0
    
    # 2.3 Ask user to enter month to search for
    target = input("Enter the first three letters of the month to search: ")
    
    # Input validation - not in design (See 2018 Specimen)
    while len(target) != 3:
        
        #Error message
        print("Please enter exactly 3 letters.")
        
        # Ask user to re-enter month to search for
        target = input("Enter the first three letters of the month to search: ")
        
    # 2.4 While position is -1 and index is less than the length of the array
    while position == -1 and index < len(orders):
        
        # 2.5 If current month is equal to searched month and current rating is 5 then
        month = orders[index].date[3:6]
        rating = orders[index].rating
        
        if month == target and rating == 5:
        
            # 2.6 Set position to index
            position = index
            
        # 2.7 End if
        
        # 2.8 Add 1 to index
        index = index + 1
        
    # 2.9 End while
        
    # 2.10 Return position
    return position


def writeWinner(orders, position):
    """Write details of the winning customer, or ‘no winner’ message, to a text file."""
    # IN orders(orderNum,date,email,option,cost,rating), position

    # 3.1 Open new file ‘winningCustomer.txt’
    file = open("winningCustomer.txt", "w")
    
    # 3.2 If position is 0 or above then
    if position >= 0:
    
        # 3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
        file.write(orders[position].orderNum + ",")
        file.write(orders[position].email + ",")
        file.write(str(orders[position].cost) + "\n")
        
    # 3.4 Else
    else:
    
        # 3.5 Write ‘No winner’ to ‘winningCustomer.txt’
        file.write("No winner.\n")
        
    # 3.6 End if
    
    # 3.7 Close ‘winningCustomer.txt’
    file.close()


def deliveredCollected(orders):
    """Display the total number of orders delivered and the total number of orders collected."""
    # IN orders(orderNum,date,email,option,cost,rating)
    
    # Intialise local variable
    delivered = 0
    collected = 0
    
    # 4.1 Call countOption function to return the number of orders delivered
    delivered = countOption(orders, "Delivery")
    
    # 4.2 Call countOption function to return the number of orders collected
    collected = countOption(orders, "Collection")

    # 4.3 Output the total number of orders delivered
    print("Total number of orders delivered to date: " + str(delivered))
    
    # 4.4 Output the total number of orders collected
    print("Total number of orders collected to date: " + str(collected))


def countOption(orders, option):
    """Count the number of orders delivered or ordered."""
    
    # Initialise local variable
    count = 0
    
    # Loop for each order
    for order in orders:
        
        # Count delivered
        if order.option == option:
            
            # Increment count
            count = count + 1
    
    # Return count
    return count       
        

#
# Main program
#

def main():
    
    # Intilise global variables
    orders = [Order() for index in range(505)]
    position = 0
    
    # 1 Read from file into array of records.
    # OUT orders(orderNum,date,email,option,cost,rating) 
    orders = getData()
    

    # 2 Find the position of the customer who gave the first 5-star rating in a given month.
    # IN orders(orderNum,date,email,option,cost,rating)
    # OUT position
    position = findRating(orders)


    # 3 Write details of the winning customer, or ‘no winner’ message, to a text file.
    # IN orders(orderNum,date,email,option,cost,rating), position
    writeWinner(orders, position)


    # 4 Display the total number of orders delivered and the total number of orders collected.
    # IN orders(orderNum,date,email,option,cost,rating)
    deliveredCollected(orders)


main()