# Title: Read Joystick Values
# Date: 26 Jun 2022

import time
import board
import analogio

x = analogio.AnalogIn(board.JOYSTICK_X)
y = analogio.AnalogIn(board.JOYSTICK_Y)

while True:
    
    print(x.value, y.value)
    
    time.sleep(0.5)
