# Flash Pico W LED

Use MicroPython on RPi Pico W to flash the green LED.

## Code

``` python
# Title: Flash Green LED - Pico W
# Date: 04 Jun 2023

# MicroPython - Pico W

from machine import Pin
import time

# Use green LED
led = Pin("LED", Pin.OUT)

while True:
    # On
    led.on()
    time.sleep(0.5)
    
    # Off
    led.off()
    time.sleep(0.5)
```
