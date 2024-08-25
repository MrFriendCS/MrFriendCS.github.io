# Title: Read Light Sensor Value
# Date: 26 Jun 2022

import time
import board
import analogio

light = analogio.AnalogIn(board.LIGHT)

while True:
    
    print(light.value)
    
    time.sleep(0.5)
