import numpy as np
import serial
import time
import threading
import cv2
from detect_ensw1026 import *
serial_port = None

threading_Time = 0.01


def TX_data_py2(ser, one_byte):  # one_byte= 0~255

    ser.write(serial.to_bytes([one_byte]))  # python3


def RX_data(ser):
    time.sleep(threading_Time)
    #print(ser.inWaiting())
    result = ser.read(1)
    RX = ord(result)
    return RX


class ThreadWithResult(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.result = target(*args, **kwargs)

        super().__init__(group=group, target=function, name=name, daemon=daemon)


BPS = 4800  # 4800,9600,14400, 19200,28800, 57600, 115200

# ---------local Serial Port : ttyS0 --------
# ---------USB Serial Port : ttyAMA0 --------

serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
serial_port.flush()  # serial cls


def capread(cap):

    ret, frame = cap.read()
    return frame

# ---------------------------

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    while True:
        
        thread1 = ThreadWithResult(target=capread, args=(cap,))
        thread1.daemon = True
        thread1.start()
        thread1.join()
        frame = thread1.result
        thread2 = ThreadWithResult(target=main_ensw, args=(frame,))
        thread2.daemon = True
        thread2.start()
        thread2.join()
        alphabet_ensw = thread2.result
        if int(alphabet_ensw) == 0: # e

            serial_t = Thread(target=TX_data_py2, args=(serial_port, 37))
            serial_t.daemon = True
            serial_t.start()
            serial_t.join()
            break

        elif int(alphabet_ensw) == 1: # n

            serial_t = Thread(target=TX_data_py2, args=(serial_port, 40))
            serial_t.daemon = True
            serial_t.start()
            serial_t.join()
            break

        elif int(alphabet_ensw) == 2: # s

            serial_t = Thread(target=TX_data_py2, args=(serial_port, 39))
            serial_t.daemon = True
            serial_t.start()
            serial_t.join()
            break

        elif int(alphabet_ensw) == 3: # w

            serial_t = Thread(target=TX_data_py2, args=(serial_port, 38))
            serial_t.daemon = True
            serial_t.start()
            serial_t.join()
            break
    print('finish')
