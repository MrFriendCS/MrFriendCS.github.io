# Create Taxi Values

fileIn = open("taxi.csv", "r")
fileOut = open("taxi.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO taxi VALUES ")
    
    fileOut.write("(" + str(data[0].strip()) + ",")  # taxi_id
    fileOut.write( "\"" + data[1].strip() + "\",")  # taxi_reg
    fileOut.write( "\"" + data[2].strip() + "\",")  # make
    fileOut.write( "\"" + data[3].strip() + "\",")  # model
    fileOut.write( "\"" + data[4].strip() + "\");\n")  # colour

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
