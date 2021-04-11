from time import perf_counter
import datetime
import serial
import csv

filenam = 'NabeelWroPos.csv' #The name of the file to write to
numtrial = 400 #The number of recorded trials
tim = []

ser = serial.Serial('COM5',9600); #Connect to the arduino ouput

start = perf_counter()
for a in range(numtrial): #Loop Through the trials and record to the file
    x = ser.readline().decode('UTF-8')
    with open(filenam, mode ='a') as file:
        if(x != " "):
            file.write(x)
    stop = perf_counter()
    remain = round((stop - start))
    tim.append(remain)
    avgtime = round(sum(tim)/len(tim)* (numtrial-a))
    start = stop
    print("Please Wait. Progress " + str(round(a/numtrial * 100)) + "% Trial Number: " + str(a) + " Estimated Time " + str(datetime.timedelta(seconds=avgtime)), end ='\r', flush=True)
ser.close()
