import serial
import time
from def_escape import *

def TX_data_py2(ser, one_byte):  # one_byte= 0~255

    ser.write(serial.to_bytes([one_byte]))  #python3
BPS =  4800  # 4800,9600,14400, 19200,28800, 57600, 115200

#---------local Serial Port : ttyS0 --------
#---------USB Serial Port : ttyAMA0 --------


serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
serial_port.flush() # serial cls

floor_color=[0,0,1]
room_name=[2,3,1]

escape(room_name, floor_color, serial_port)
