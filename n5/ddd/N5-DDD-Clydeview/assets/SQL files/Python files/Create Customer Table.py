# Create Customer Table

fileIn = open("Customer.csv", "r")
fileOut = open("Customer.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

tableCustomer = """CREATE TABLE Customer (
    customerNo INT NOT NULL,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    street VARCHAR(50) NOT NULL,
    town VARCHAR(20) NOT NULL,
    package VARCHAR(10) NOT NULL CHECK (package IN 
        ("Standard", "Large", "Premier")),
    directDebit BOOL NOT NULL,
    paymentDueDate DATE,
    PRIMARY KEY (customerNo)
);"""

fileOut.write(tableCustomer + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Customer VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # customerNo
    fileOut.write( "\"" + data[1].strip() + "\",")  # forename
    fileOut.write( "\"" + data[2].strip() + "\",")  # surname
    fileOut.write( "\"" + data[3].strip() + "\",")  # street
    fileOut.write( "\"" + data[4].strip() + "\",")  # town
    fileOut.write( "\"" + data[5].strip() + "\",")  # package
    if bool(int(data[6].strip())):  # directDebit
        fileOut.write("TRUE,")
    else:
        fileOut.write("FALSE,")
    fileOut.write( "\"" + data[7].strip() + "\");\n")  # paymentDueDate

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
