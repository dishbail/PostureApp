import serial

def readdata():
    ser = serial.Serial('COM5',9600); #Connect to the arduino ouput
    x = list(map(int,ser.readline().decode('UTF-8').split(", ")))
    ser.close()
    if len(x) <256:
        x = readdata()
    return x
