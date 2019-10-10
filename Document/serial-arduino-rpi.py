#!/usr/bin/env python2
import serial, datetime

arduino=serial.Serial('/dev/ttyACM0',115200,timeout=1)
rawdata=str(arduino.readline())
count=1
f=open("data.txt",mode="w")

while count<10:
    rawdata=str(arduino.readline())
    f.write("\n data ke %d\r" % count + " " +
            rawdata + " " +
            str(datetime.datetime.now()) + '\n')
    count+=1
    print(rawdata)
f.close()
