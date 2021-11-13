import time
import cv2
import numpy as np
import serial
cap=cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,640)
def TX_data_py2(ser, one_byte):  # one_byte= 0~255

    ser.write(serial.to_bytes([one_byte]))  #python3
serial_port =  None
serial_use = 1
threading_Time = 0.01
BPS=4800
serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
serial_port.flush() # serial cls
for i in range(3):
	ret, img2=cap.read()
	cv2.imshow('img2',img2)
	key=cv2.waitKey(1)
	TX_data_py2(serial_port,59)#1
	time.sleep(1.2)
	for i in range(7):
		img1, ret=cap.read()
		time.sleep(0.01)
	cv2.imshow('img1',img1)
	key1=cv2.waitKey(1)
		
	
	
	if key==27:
		break
