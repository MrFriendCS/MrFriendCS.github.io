
``` python
# Title: Access Point / Web Server
# Author: Mr Friend
# Date: 19 Feb 2025

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
    
    html = html + addForm()
    
    html = html + addDateTime()
    
    html = html + """
    </body>
    </html>
    """
    
    return html

def addDataTable():
    
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


def addDateTime():
    
    rtc = RTC()
    
    now = rtc.datetime()
    
    time = str(now[0]) + "-" + str(now[1]) + "-" + str(now[2])
    time = time + " @ " + str(now[4]) + ":" + str(now[5]) + ":" + str(now[6])
    
    return str(str(time))


def apMode(ssid, password):
    
    # Turn on Access Point (AP)
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)

    # Wait until AP is active
    while ap.active() == False:
        time.sleep(1)
    
    # Display local IP address
    print('\nIP Address To Connect to: ' + ap.ifconfig()[0])

    # Create TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind socket to an address [ip, port]
    s.bind(('', 80))
    
    # Number of backlog connections allowed
    s.listen(5)


    while True:
        
        # Accept a connection
        conn, addr = s.accept()  # local, remote

        # Display remote IP address
        print("\nGot a connection from " + str(addr))

        # Receive data from the socket (bytes)
        request = conn.recv(1024)
        
        # Display received data
        try:
            print("\nContent = " + str(request).split()[1])
        except:
            print("\nContent = " + str(request))

        # Get web page
        response = webPage()

        # Return web page to connected device
        conn.send(response)

        # Close connection
        conn.close()


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

apMode('Pico W', 'Password')
```
