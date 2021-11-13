from detect_ensw1026 import *
import time
import cv2
import serial
from def_linedetect0901 import *
from detect_arrow_1004 import *
from detect_abcd_1004 import *
from def_contour_1 import *
from def_linecomeback import *

from def_linedetect_b import *
from def_escape import *

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
def pixelread_yellow(cap):
    ret, img_color = cap.read()
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
#=========================================================
    frame=cv2.GaussianBlur(img_color,(5,5),0)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_yellow = (5, 0, 0) 
    upper_yellow = (48, 255, 255)
    img_mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow) 
#_================------------------------====================
    cntNotyellow=cv2.countNonZero(img_mask_yellow)
    return cntNotyellow


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
BPS =  4800  # 4800,9600,14400, 19200,28800, 57600, 115200

#---------local Serial Port : ttyS0 --------
#---------USB Serial Port : ttyAMA0 --------


serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
serial_port.flush() # serial cls
alphabet_ensw=main_ensw(cap,serial_port)
print('alphabet_ensw:',alphabet_ensw)


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
floor_color=[]
def cnt1_1(cap,serial_port,alphabet_color,floor_color,arrow_direction):
    time.sleep(2)
    if arrow_direction==right_turn:
        TX_data_py2(serial_port,30)
    elif arrow_direction==left_turn:
        TX_data_py2(serial_port,28)
    end_contour1=contour_main(cap,serial_port,alphabet_color,floor_color,arrow_direction)
    #if(end_contour1==end):
    #    break
    #while True:
    time.sleep(2.5)
    '''
    TX_data_py2(serial_port,29)     #20 rhro neck
    time.sleep(1.5)
    end_linedetectb1=def_linecomback_main(cap,serial_port)
    time.sleep(1.5)
    TX_data_py2(serial_port,57)     #30 neck
    time.sleep(1.5)
    end_linedetectb1=def_linecomback_main(cap,serial_port)
    time.sleep(1.5)
    '''
    TX_data_py2(serial_port,56)     #45 neck
    for i in range(7):
        imgsdf=cap.read()
        time.sleep(0.1)
    time.sleep(1.0)
    end_linedetectb1=def_linecomback_main(cap,serial_port,0)

    time.sleep(1.5)
    TX_data_py2(serial_port,67)
    time.sleep(2)
    TX_data_py2(serial_port,55)     #60 neck
    for i in range(7):
        imgsdf=cap.read()
        time.sleep(0.1)
    time.sleep(1.0)
    
    end_linedetectb1=def_linecomback_main(cap,serial_port,1)

    TX_data_py2(serial_port,53)     #90 enck
    time.sleep(1.5)
    #if(end_linedetectb1==end):
        #break
    #elif(end_linedetectb1==2):
        #continue
    TX_data_py2(serial_port,67)
    time.sleep(2)
    if arrow_direction== right_turn:
        TX_data_py2(serial_port,9)
        time.sleep(2)
        TX_data_py2(serial_port,9)
        time.sleep(2)
    if arrow_direction== left_turn:
        TX_data_py2(serial_port,7)
        time.sleep(2)
        TX_data_py2(serial_port,7)
        time.sleep(2)
    #TX_data_py2(serial_port,9)
    #time.sleep(1.5)
    #TX_data_py2(serial_port,9)
    #time.sleep(1.5)
    #TX_data_py2(serial_port,53)
    #time.sleep(1)
    for i in range(8):
        imgkjij=cap.read()
        time.sleep(0.1)
serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
serial_port.flush() # serial cls
#time.sleep(2)
#TX_data_py2(serial_port,53)
time.sleep(3)
TX_data_py2(serial_port,53)
time.sleep(2)
TX_data_py2(serial_port,62)
time.sleep(3)
for i in range(8):
    imgjfid=cap.read()
    time.sleep(0.01)

while True:
    serial_port.flush() # serial cls
    #contour_object(img)
    #print("3")

    t=linedetect(cap)

    print("t: ",t)
    
    if t!=50:   #corner none

        if cnt1==0 and t==69:###1107editt==67:
            t=70##1107edit#t=65
        if t==1 or t==3 or t==59:
            if t!=711 and t!=71:
                TX_data_py2(serial_port,t)
            elif t==71 and (cnt1==1 or cnt1==3 or cnt1==5):
                time.sleep(2)
                TX_data_py2(serial_port,28)#leftneck 45degree
                for i in range(15):
                    left_yellow=pixelread_yellow(cap)
                    time.sleep(0.1)
                time.sleep(0.5)
                TX_data_py2(serial_port,30)#rightneck 45degree
                for i in range(20):
                    right_yellow=pixelread_yellow(cap)
                    time.sleep(0.1)
                if left_yellow>right_yellow:
                    TX_data_py2(serial_port,15)
                    time.sleep(1)
                    TX_data_py2(serial_port,15)
                    time.sleep(1)
                else:
                    TX_data_py2(serial_port,20)
                    time.sleep(1)
                    TX_data_py2(serial_port,20)
                    time.sleep(1)
                TX_data_py2(serial_port,53)
                time.sleep(0.5)
            time.sleep(0.5)
            if t==59:
                time.sleep(0.8)
            for i in range(8):
                imgjfid=cap.read()
                time.sleep(0.01)
            key=cv2.waitKey(1)
        elif t!=200:############################3IF no?
            if t!=711 and t!=71:
                TX_data_py2(serial_port,t)
            elif t==71 and (cnt1==1 or cnt1==3 or cnt1==5):
                print("1")
                #TX_data_py2(serial_port,71)
        #if t==4 or t==6 or t==1 or t==2:
            #time.sleep(0.5)
            #for i in range(8):
                #imgkk, ret=cap.read()
        if cnt1==0 and t==200:# when horizontal line only detected
            TX_data_py2(serial_port,20)######TX_data_py2(serial_port,68) for test_contour1104_(03:08)
        
        elif cnt1>0 and t==200:# when left right turn selected
            if arrow_direction==left_turn:
                TX_data_py2(serial_port,15)
            elif arrow_direction==right_turn:
                TX_data_py2(serial_port,20)
        
    if t==50:   #corner
        ''' 
        time.sleep(0.2)
        TX_data_py2(serial_port,53)
        for i in range(7):
            imgkkkk=cap.read()
            time.sleep(0.2)
        
        def_linecomback_main(cap,serial_port,1)
        '''
            #TX_data_py2(serial_port,tx)
            #if tx==2:
                #break
        print("cnt 1:" ,cnt1)
        if cnt1==0:##########cnt1==0:
            #=====================================
            time.sleep(3)
            TX_data_py2(serial_port,44)
            time.sleep(2)
            TX_data_py2(serial_port,67)
            time.sleep(2)
            arrow_direction=main_arrow(cap,serial_port)
            print(arrow_direction)
            #=====================================
            
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
        
        if cnt1==1:#1107edit#cnt1==0: ###########cnt1==1: 
            #========================================
            time.sleep(2.5)#3
            TX_data_py2(serial_port,44)
            time.sleep(1.5)
            alphabet_abcd, alphabet_color=main_abcd(cap,serial_port)
            room_name.append(alphabet_abcd)
            room_color.append(alphabet_color)#blue 0 red 1
            #=========================================
            #while True:
            cnt1_1(cap,serial_port,alphabet_color,floor_color,arrow_direction)
                    
        
        if cnt1==2:###when T balgun
            time.sleep(3)
            TX_data_py2(serial_port,2)
            time.sleep(1)
            for i in range(8):
                imgkjij=cap.read()
                time.sleep(0.1)
        if cnt1==3:
            time.sleep(2.5)#3
            TX_data_py2(serial_port,44)
            time.sleep(1.5)
            alphabet_abcd, alphabet_color=main_abcd(cap,serial_port)
            room_name.append(alphabet_abcd)
            room_color.append(alphabet_color)#blue 0 red 1
            #=========================================
            cnt1_1(cap,serial_port,alphabet_color,floor_color,arrow_direction)
            
        #====================================================
        
        
        if cnt1==5:######cnt1==1:
            print("cnt111:",cnt1)
            break
        if cnt1==4:#cnt==6: #when go out
            time.sleep(2)
            TX_data_py2(serial_port,67)
            time.sleep(1)
            for i in range(5):
                time.sleep(1)
                if arrow_direction==left_turn:
                    TX_data_py2(serial_port,7)
                if arrow_direction==right_turn:
                    TX_data_py2(serial_port,9)
            time.sleep(2.5)
            TX_data_py2(serial_port,69)
            time.sleep(1.5)
            for i in range(8):
                imgkjij=cap.read()
                time.sleep(0.1)
            print("cnt1:",cnt1)
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
print('floorcolor',floor_color)

escape(room_name, floor_color, serial_port)
cv2.waitKey(0)
cv2.destroyAllWindows()






