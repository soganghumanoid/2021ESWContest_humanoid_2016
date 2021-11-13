import platform
import numpy as np
import argparse
import cv2
import serial
import time
import sys
from threading import Thread

serial_use = 1

serial_port =  None
Read_RX =  0
receiving_exit = 1
threading_Time = 0.01

def TX_data_py2(ser, one_byte):  # one_byte= 0~255
    #ser.write(chr(int(one_byte)))          #python2.7
    ser.write(serial.to_bytes([one_byte]))  #python3
BPS =  4800  # 4800,9600,14400, 19200,28800, 57600, 115200

#---------local Serial Port : ttyS0 --------
#---------USB Serial Port : ttyAMA0 --------

   
serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
serial_port.flush() # serial cls
while True:
	a=input('type KEY(break esc):')
	TX_data_py2(serial_port,a)
	time.sleep(0.1)
	if a==27:
		break
