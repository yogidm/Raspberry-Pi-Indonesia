#!/usr/bin/env python2

import serial,time
arduino=serial.Serial('/dev/ttyACM0',115200,timeout=0.5)

i=0
while(1):
    arduino.write('y')
    arduino.write(str(i))
    arduino.write('x')
    arduino.write(str(500))
    time.sleep(.01)
    i=i+1

