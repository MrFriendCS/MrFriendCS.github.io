
``` python
# Title: Access Point / Web Server
# Author: Mr Friend
# Date: 18 Feb 2025

# Import extra code
import network  # https://docs.micropython.org/en/latest/library/network.html
import socket   # https://docs.micropython.org/en/latest/library/socket.html
#import time


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
    
    <table>
    <thead>
    <tr><th>Date</th><th>Time</th><th>Option</th></tr>
    </thead>
    <tbody>
    
    <!-- Data from data.csv file (Python) -->"""
    
    
    file = open("data.csv", "r")
    line = file.readline()  # Ignore headers
    line = file.readline()
    
    while line:
        
        data = line.split(",")
        
        html = html + "<tr><td>" + data[0] + "</td><td>"
        html = html + data[1] + "</td><td>" + data[2].strip() + "</td></tr>"
        
        line = file.readline()
        
    file.close()
    
    html = html + """
    </tbody>
    </table>
    
    <h2>Array data</h2>
    
    <!-- Data from an array (Python) -->"""
    
    for index in range(len(days)):
        
        html = html + "<p>" + str(index + 1) + " - " + days[index] + "</p>"
        
    html = html + """
    </body>
    </html>
    """
    
    return html


def apMode(ssid, password):
    
    # Turn on Access Point (AP)
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)

    # Wait until AP is active
    while ap.active() == False:
        pass
    
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
