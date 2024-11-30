# Create Journey Values

def adjustTime(time):
    """Ensure 24-hour format is used"""
    
    if len(time) == 7:
        time = "0" + time
        
    return time


fileIn = open("journey.csv", "r")
fileOut = open("journey.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    data[3] = adjustTime(data[3])
    
    fileOut.write("INSERT INTO journey VALUES ")
    
    fileOut.write("(" + str(data[0].strip()) + ",")  # journey_id
    fileOut.write(      str(data[1].strip()) + ",")  # taxi_id
    fileOut.write(  "\"" + data[2].strip() + "\",")  # pick_up_date
    fileOut.write(  "\"" + data[3].strip() + "\",")  # pick_up_time
    fileOut.write(      str(data[4].strip()) + ",")  # pax
    fileOut.write(  "\"" + data[5].strip() + "\",")  # pick_up_loc
    fileOut.write(  "\"" + data[6].strip() + "\");\n")  # drop_off_loc

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
