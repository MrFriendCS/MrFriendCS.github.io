# Pico - Internal LED - SOS

Uses the picozero library to control the onboard LED.


## Install picozero library

Install the picozero library, if not already installed:
[Instructions](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico/4 "RPi website").


## Task

Use the Pico's internal LED to send the international distress code of __SOS__ in Morse code.


### Morse


#### Time Units

Dot: 1 unit

Dash: 3 units

Dot/Dash pause: 1 unit

Letter pause: 3 units

Word pause: 7 units


#### SOS

![SOS in Morse Code](assets/SOS.png)


## Starter Code

``` python
# Get extra code
from picozero import pico_led
from time import sleep


# Loop forever
while True:
    
    
    # Loop - Dot x 3
    
        # Turn LED on
        
        # Pause
        
        # Turn LED off
        
        # Pause
        
    # Letter pause
    
    
    # Loop - Dash x 3
    
    
    # Letter pause
        
    
    # Loop - Dot x 3
        
        
    # Word pause
 ```
