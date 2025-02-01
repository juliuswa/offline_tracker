import serial 
import time 

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1) 

while True: 
    value = arduino.readline() 
    print(value)