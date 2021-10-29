from detect_ensw1026 import *
import time
import cv2
import serial
from def_linedetect0901 import *
from detect_arrow_1004 import *
from detect_abcd_1004 import *
from def_contour_1 import *
from def_linecomeback import *
def TX_data_py2(ser, one_byte):  # one_byte= 0~255

    ser.write(serial.to_bytes([one_byte]))  #python3

serial_use = 1
end=0
serial_port =  None
Read_RX =  0
receiving_exit = 1
threading_Time = 0.01
t=21
def RX_data(ser):

    if ser.inWaiting() > 0:
        result = ser.read(1)
        RX = ord(result)
        return RX
    else:
        return 0


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
alphabet_ensw=main_ensw(cap)
print('alphabet_ensw:',alphabet_ensw)

BPS =  4800  # 4800,9600,14400, 19200,28800, 57600, 115200

#---------local Serial Port : ttyS0 --------
#---------USB Serial Port : ttyAMA0 --------


serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
serial_port.flush() # serial cls
if int(alphabet_ensw) == 0: # e

    TX_data_py2(serial_port,37)

elif int(alphabet_ensw) == 1: # n

    TX_data_py2(serial_port,40)

elif int(alphabet_ensw) == 2: # s

    TX_data_py2(serial_port,39)

elif int(alphabet_ensw) == 3: # w

    TX_data_py2(serial_port,38)

print('finish')


time.sleep(1)
#==============================================================
print("1")
print("2")

BPS =  4800
serial_use = 1
serial_port =  None
Read_RX =  0
receiving_exit = 1
threading_Time = 0.01
t=21
cnt1=0
left_turn=1
right_turn=0
room_name =[]
room_color=[]


serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
serial_port.flush() # serial cls
#time.sleep(2)
#TX_data_py2(serial_port,53)
time.sleep(3)
TX_data_py2(serial_port,53)
time.sleep(2)
TX_data_py2(serial_port,62)
time.sleep(3)



while True:
    serial_port.flush() # serial cls
    #contour_object(img)
    #print("3")

    t=linedetect(cap)

    print("t: ",t)
    
    if t!=50:   #corner none

        if cnt1==0 and t==2:
            t=65
        TX_data_py2(serial_port,t)
        #if t==4 or t==6 or t==1 or t==2:
            #time.sleep(0.5)
            #for i in range(8):
                #imgkk, ret=cap.read()
        
    if t==50:   #corner 
        if cnt1==0:
            time.sleep(3)
            TX_data_py2(serial_port,44)
            time.sleep(2)
            #TX_data_py2(serial_port,59)
            arrow_direction=main_arrow(cap)
            print(arrow_direction)
            if arrow_direction==left_turn:
                TX_data_py2(serial_port,53)
                time.sleep(1)
                TX_data_py2(serial_port,7)
                time.sleep(1)
                TX_data_py2(serial_port,7)
                time.sleep(1)
                TX_data_py2(serial_port,7)
                time.sleep(1)
                TX_data_py2(serial_port,7)
                time.sleep(1)
                TX_data_py2(serial_port,7)
                time.sleep(2)
            if arrow_direction==right_turn:
                TX_data_py2(serial_port,53)
                time.sleep(1)
                TX_data_py2(serial_port,9)
                time.sleep(1)
                TX_data_py2(serial_port,9)
                time.sleep(1)
                TX_data_py2(serial_port,9)
                time.sleep(1)
                TX_data_py2(serial_port,9)
                time.sleep(1)
                TX_data_py2(serial_port,9)
                time.sleep(2)
                print(9)
        
        if cnt1==1: 
            time.sleep(5)
            TX_data_py2(serial_port,44)
            time.sleep(3)
            alphabet_abcd, alphabet_color=main_abcd(cap)
            room_name.append(alphabet_abcd)
            room_color.append(alphabet_color)
            
            #while True:
            end_contour1=contour_main(cap,serial_port)
            #if(end_contour1==end):
            #    break
            #while True:
            time.sleep(2.5)
            TX_data_py2(serial_port,29)     #20 rhro neck
            time.sleep(1.5)
            end_linedetectb1=def_linecomback_main(cap,serial_port)
            time.sleep(1.5)
            TX_data_py2(serial_port,57)     #30 neck
            time.sleep(1.5)
            end_linedetectb1=def_linecomback_main(cap,serial_port)
            time.sleep(1.5)
            TX_data_py2(serial_port,56)     #45 neck
            time.sleep(1.5)
            end_linedetectb1=def_linecomback_main(cap,serial_port)
            time.sleep(1.5)
            TX_data_py2(serial_port,55)     #60 neck
            time.sleep(1.5)
            end_linedetectb1=def_linecomback_main(cap,serial_port)
            
            TX_data_py2(serial_port,53)     #90 enck
            time.sleep(1.5)
            #if(end_linedetectb1==end):
                #break
            #elif(end_linedetectb1==2):
                #continue
            TX_data_py2(serial_port,59)
            time.sleep(1)
            TX_data_py2(serial_port,9)
            time.sleep(1)
            TX_data_py2(serial_port,9)
            time.sleep(1)
            TX_data_py2(serial_port,9)
            time.sleep(1)
            TX_data_py2(serial_port,53)
            time.sleep(1)
            break
                    
        
            
        if cnt1==2:
            break
            
        cnt1=cnt1+1
            
        '''
        if cnt==0:
            for i in range(4):  #turn 4
                linedetect(cap)
                time.sleep(0.5)
                print("cornercornercornercornercornercornercornercorner")
                print("wait 1.5sec")
                TX_data_py2(serial_port,50)
                print("wait 1.5sec")
                time.sleep(1)

                if i<2:
                    TX_data_py2(serial_port,15)
                    time.sleep(1)
                TX_data_py2(serial_port,15)
                time.sleep(1)
                TX_data_py2(serial_port,15)
                time.sleep(1)

            cnt=cnt+1
            time.sleep(3)
        '''
        


    #TX_data_py2(serial_port,11)
    #time.sleep(3)
    #time.sleep(2)
    key=cv2.waitKey(1)
    if key ==27:
        break

print('roomname',room_name)
print('roomcolor',room_color)
cv2.waitKey(0)
cv2.destroyAllWindows()






