import serial
import os
from time import sleep

if(not os.path.exists("./color.csv")):
    with open("color.csv", "w") as f:
        print("R,G,B", file=f)
com = serial.Serial("COM7", 115200)
print("Now you can send data")
while True:
    val = str(com.readline().decode("utf-8").rstrip("\n"))
    print(val)
    if(val[:-2][-1] == ','):
        with open("color.csv", "a") as f:
            print("{}".format(val), file=f)
    else:
        with open("color.csv", "a") as f:
            print("{}".format(val[:-2]), file=f)
    sleep(2)