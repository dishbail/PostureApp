import serial

def readdata():
    ser = serial.Serial('COM5',9600); #Connect to the arduino ouput
    x = ser.readline().decode('UTF-8')
    ser.close()
    return x
