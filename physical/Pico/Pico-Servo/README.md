# Servo

Using picozero to control a servo.


## Install picozero library

[Instructions](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico/4 "RPi website"). 


## Layout

![Servo layout](assets/servo.png)


## Code

``` python
from picozero import Servo
from time import sleep

# Kitronik Clippable Servo 25105
# Vcc to Vbus (5V)
# Pulse width: 500 - 2500 μS

# GPIO pin for servo
servo = Servo(22, min_pulse_width=0.0005, max_pulse_width=0.0025)

# Set the servo to its minimum position
servo.min()
sleep(1)

# Set the servo to its mid position
servo.mid()
sleep(1)

# Set the servo to its maximum position
servo.max()
sleep(1)

# Turn the servo “off” by setting the value to None
servo.off()
```
