import time
import board
import adafruit_lsm303_accel

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_lsm303_accel.LSM303_Accel(i2c)

while True:
    acc_x, acc_y, acc_z = sensor.acceleration

    print(round(acc_x, 1), round(acc_y, 1), round(acc_z, 1), "\n")
    
    time.sleep(1.0)
