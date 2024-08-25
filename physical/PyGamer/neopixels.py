# Title: Control Neopixels
# Date: 26 Jun 2022

import time
import board
import neopixel

# 5 Neopixels
led = neopixel.NeoPixel(board.NEOPIXEL, 5)

# Set brightness
led.brightness = 0.3

while True:
    
    # Turn on Neopixels
    led[0] = (255, 0, 0)
    time.sleep(0.2)

    led[1] = (255, 255, 0)
    time.sleep(0.2)

    led[2] = (255, 255, 255)
    time.sleep(0.2)

    led[3] = (0, 255, 255)
    time.sleep(0.2)

    led[4] = (0, 0, 255)
    time.sleep(0.2)
    
    # Turn off Neopixels
    for counter in range(5):
        led[counter] = (0, 0, 0)
        time.sleep(0.2)
