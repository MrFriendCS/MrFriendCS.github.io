``` python
# Title: Access Point / Web Server
# Author: Mr Friend
# Date: 22 Feb 2025

# Import extra code
# https://docs.micropython.org/
from machine import RTC
import network
import socket
import time


def webPage():
    """Create web page content."""      
    
    html = """
    <!DOCTYPE html>
    <html lang="en-gb">
    
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Pico W</title>
    
    <style>
    * {
        font-family: sans-serif;
        }
    table, th, td {
        border: 1px solid, black;
        }
    </style>
    
    </head>
    
    <body>
    <h1>Pico W</h1>
    <h2>CSV file data</h2>
    
    <!-- Data from data.csv file (Python) -->
    """
    
    html = html + addDataTable()
    
    #html = html + addForm()
    
    html = html + getDateTime()
    
    html = html + """
    </body>
    </html>
    """
    
    return html

def addDataTable():
    """Read data from file to create HTML table."""
    table = """
    <table>
    <thead>
    """
    
    file = open("data.csv", "r")
    line = file.readline()  # Get headers
    
    data = line.split(",")

    table = table + "<tr><th>" + data[0] + "</th><th>"
    table = table + data[1] + "</th><th>" + data[2].strip() + "</th></tr>"
    
    table = table + """
    </thead>
    <tbody>
    """
    
    line = file.readline()
    
    while line:
        
        data = line.split(",")
        
        table = table + "<tr><td>" + data[0] + "</td><td>"
        table = table + data[1] + "</td><td>" + data[2].strip() + "</td></tr>"
        
        line = file.readline()
        
    file.close()
    
    table = table + """
    </tbody>
    </table>
    """

    return table


def addForm():
    """HTML form."""
    
    form = """
    <form action="/rtc?"><br>
    <label for="year">Year:</label>
    <input type="number" id="year" name="year" value="2025" min="2025" max="2035"><br>
    <label for="month">Month:</label>
    <input type="number" id="month" name="month" value="6" min="1" max="12"><br>
    <label for="day">Day:</label>
    <input type="number" id="day" name="day" value="15" min="1" max="31"><br><br>
    <label for="day">Hour:</label>
    <input type="number" id="hour" name="hour" value="13" min="0" max="23"><br>
    <label for="minute">Minute:</label>
    <input type="number" id="minute" name="minute" value="30" min="0" max="59"><br>
    <label for="second">Second:</label>
    <input type="number" id="second" name="second" value="00" min="0" max="59"><br><br>
    <input type="submit" value="Submit">
    </form>
    """

    return form


def getDateTime():
    """Get RTC value and create HTML."""
    
    rtc = RTC()
    
    now = rtc.datetime()
    
    time = "<br>" + str(now[0]) + "-" + str(now[1]) + "-" + str(now[2])
    time = time + " @ " + str(now[4]) + ":" + str(now[5]) + ":" + str(now[6])
    
    return str(str(time))


def apMode(ssid, password):
    
    # Turn on Access Point (AP)
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)

    # Wait until AP is active
    while ap.active() == False:
        print("AP starting.")
        time.sleep(1)
    
    # Display local IP address
    print('\nIP Address To Connect to:', ap.ifconfig()[0])

    # Create TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind socket to an address [ip, port]
    s.bind(('', 80))
    
    # Allow socket to accept connections - backlog connections not specified
    s.listen()

    # Forever
    while True:
        
        # Wait to accept a connection
        conn, addr = s.accept()  # socket object: rx, tx, remote address

        # Display remote IP address
        print("\nGot a connection from", str(addr))

        # Receive data from the socket (bytes)
        request = conn.recv(1024).decode("utf-8")
        
        data = request.split()
 
        # Example: http://192.168.4.1/rtc?y=2020&m=1&d=2&h=18&m=45
           
        if len(data) > 1 and data[1][0:4] == "/rtc":
            
            field = data[1].split("?")[1]
            fields = field.split("&")
            
            if len(fields) == 5:
                
                v = [0] * 5
                
                for index in range(5):
                    
                    v[index] = int(fields[index].split("=")[1])
                
                try:
                    
                    rtc = RTC()
                    
                    # [y,m,d], day of week, [h,m], seconds, microseconds
                    rtc.datetime((v[0], v[1], v[2], 0, v[3], v[4], 0, 0))
                    
                    print("RTC updated.")
        
                except:
                    
                    print("RTC update failed:", request)
    

        # Get web page
        response = webPage()

        # Return web page to connected device
        conn.send(response)

        # Close connection
        conn.close()


def main():
    
    apMode('Pico W', 'Password')


main()
```