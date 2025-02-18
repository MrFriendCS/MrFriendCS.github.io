# Connect to WLAN

Use MicroPython on RPi Pico W to connect to WLAN.

## Code

``` python
# Import modules
import network
from time import sleep

# Wireless network details
ssid = "networkName"
password = "networkPassword"

# Configure Pico W as a client
wlan = network.WLAN(network.STA_IF)

# Ensure interface is active
wlan.active(True)

# Start connection
wlan.connect(ssid, password)

# Wait for connection
while wlan.isconnected() == False:
    print("Waiting for connection...")
    sleep(1)

# Connected
print("Connected\n")

# IP-level network interface parameters
print("IP address:", wlan.ifconfig()[0])
print("Subnet mask:", wlan.ifconfig()[1])
print("Gateway mask:", wlan.ifconfig()[2])
print("DNS Server:", wlan.ifconfig()[3], "\n")

# Disconnect from WLAN
wlan.disconnect()

# Wait for disconnection
while wlan.isconnected() == True:
    print("Waiting for disconnection...")
    sleep(1)

# Disconnected
print("Disconnected\n")
```
