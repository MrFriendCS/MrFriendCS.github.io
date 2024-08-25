# Scan for Network(s)

Use MicroPython on RPi Pico W to scan for network(s).

## Code

``` python
# Import module
import network

# Configure Pico W as a client
wlan = network.WLAN(network.STA_IF)

# Turn on Pico W Wifi
wlan.active(True)

# Scan for networks
networks = wlan.scan()  # List of tuples

# Display results for each network
for network in networks:
    print("SSID:", network[0])
    print("bSSID:", network[1])
    print("Channel:", network[2])
    print("RSSI:", network[3])
    print("Security:", network[4])
    print("Hidden:", network[5], "\n")
```
