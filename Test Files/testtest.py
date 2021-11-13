
import numpy as np
import serial
import time
import threading
import cv2
serial_port = None

threading_Time = 0.01

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
    print('1')
    return frame
        
        

print('11')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
print('22')
thread1 = ThreadWithResult(target=capread, args=(cap,))
thread1.daemon = True
thread1.start()
thread1.join()
frame = thread1.result
print(frame)
#cv2.imshow('a',frame)
#cv2.waitKey(0)
