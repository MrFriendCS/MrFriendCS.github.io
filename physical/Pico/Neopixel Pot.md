# Neopixel with Potentiometer

## Code

``` python
# Title: Neopixel with Pot Example
# Author: Mr Friend
# Date: 11 Nov 2024

# Note: Kitronik ZIP Stick, 35129 - 5 LEDS

# Get extra code
import machine
from neopixel import NeoPixel
from picozero import Pot

# Neopixel values
gpio = machine.Pin(28)
numOfPixels = 5

# Setup Neopixel strip
pixels = NeoPixel(gpio, numOfPixels)


# Pot reference voltage:
#   Pin 36: 3V3(OUT)

# GPIO pin for pot reading
dial = Pot(26)  # ADC0


# Repeat forever
while True:
    
    # Scale pot level: 0-255
    level = round(255 * dial.value)
    
    # Set LED brightness
    red =    (level, 0, 0)
    green =  (0, level, 0)
    blue =   (0, 0, level)
    yellow = (level, level, 0)
    cyan =   (0, level, level)
    
    # Set individual LED colours
    pixels[0] = blue
    pixels[1] = yellow
    pixels[2] = green
    pixels[3] = cyan
    pixels[4] = red
    
    # Display LEDs
    pixels.write()
```
