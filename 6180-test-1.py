'''
entfernungssensor vl6180x an eps32c3 in python mit library
by de-coder@mail.de

pins
vin - 3v
grd - ground
sda - gpio 6
sdl - gpio 7

'''

import machine
from machine import I2C
from vl6180x import Sensor
from machine import Pin

i2c = machine.I2C(scl=machine.Pin(7), sda=machine.Pin(6))
sensor=Sensor(i2c)

while 1:
    x=sensor.range()
    print ('Distance', str(x)) #0-255