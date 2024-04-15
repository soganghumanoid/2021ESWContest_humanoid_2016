import numpy as np
import serial
import time
import threading

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


def distance_check():
    TX_data_py2(serial_port, 61)
    thread1 = ThreadWithResult(target=RX_data, args=(serial_port,))
    thread1.daemon = True
    thread1.start()
    time.sleep(0.1)
    # this sleep must be longer than threadingtime
    print(thread1.result)
    return thread1.result
    
    #if thread1.result > 130:
    #    break
    
# ---------------------------

if __name__ == "__main__":
    while True:
        distance_check()
