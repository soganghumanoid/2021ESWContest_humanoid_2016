import cv2
import numpy as np
import math
#from def_linedetect09172 import *
from def_linedetect_b import *
import time
import serial
#cap = cv2.VideoCapture(0)
#cap.set(3,640)
#cap.set(4,480)
#BPS =  4800
def TX_data_py2(ser, one_byte):  # one_byte= 0~255

    ser.write(serial.to_bytes([one_byte]))  #python3

#serial_use = 1
##Read_RX =  0
##receiving_exit = 1
##threading_Time = 0.01
##t=21
##corner_chatatda=0
##right_left=1
##cnt=0
##print(3333)
##global cnt_neck
##cnt_neck=0
def def_linecomback_main(cap,serial_port):
    corner_chatatda=0
    time.sleep(3)
    #TX_data_py2(serial_port,29)
    time.sleep(1)
    cnt_neck1=0
    while True:
        
        #TX_data_py2(serial_port,58)
        #contour_object(cap)
        tr=linedetect_b(cap,corner_chatatda)
        print("tr :",tr)
        print("corner_chatatda: " ,corner_chatatda)
        if tr!=4:
            corner_chatatda=1
        if tr==4 and corner_chatatda==0:
            TX_data_py2(serial_port,tr)
        if tr!=2 and corner_chatatda==1: 
            TX_data_py2(serial_port,tr)

            if tr==4:
                #return 2 # continue
                continue
        if tr==2:
            if cnt_neck1==0:
                time.sleep(1)
                TX_data_py2(serial_port,2)
                time.sleep(3)
                
                
                for i in range(7):
                    imgi,ret=cap.read()
                    time.sleep(0.01)
    
                
            elif cnt_neck1==1:

                break    #end of while
            cnt_neck1=cnt_neck1+1
        
        '''
        
        elif tr==45 or tr==53 or tr==55 or tr==56 or tr==57 :
            contour_object(cap)
            TX_data_py2(serial_port,8)
            time.sleep(1)
            TX_data_py2(serial_port,8)
            time.sleep(1)
            TX_data_py2(serial_port,8)
            time.sleep(1)
            TX_data_py2(serial_port,8)
            time.sleep(1)
            TX_data_py2(serial_port,8)
            time.sleep(2)
            TX_data_py2(serial_port,45)
            contour_object(cap)
        
            '''
        #print(tr)
        #print("cnt_neck_main",cnt_neck)
        #if tr==44:
         #   break
        key=cv2.waitKey(1)
#TX_data_py2(serial_port,58)
#cap.release()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
