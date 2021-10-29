import math
#from def_linedetect09172 import *
#from def_contour_object1004 import *
import serial
import cv2
import numpy as np
import time
key=0
#img = cv2.imread('../img/shapes.png')
#cap = cv2.VideoCapture(0)
#ret, img=cap.read()
#print(1)
#height, width, ch=img.shape

width=640
height=380
cnt_neck=0
cnt_obj=0
#----------------------------------------------------
t=21
right_left=1
end_contour=0
def TX_data_py2(ser, one_byte):  # one_byte= 0~255

    ser.write(serial.to_bytes([one_byte]))  #python3


def capread_blue(cap):
        #global cnt_neck
    ret, img_color = cap.read()
    imgcopy=img_color.copy()
    img_color=img_color[100:480,0:640]
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
#=========================================================
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) 
    lower_blue = (110, 70, 30) 
    upper_blue = (130, 255, 255)
    img_mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue) 
#_================------------------------====================
    ret, img_binary = cv2.threshold(img_mask_blue, 127, 255, 0)
    contours, hierarchy = cv2.findContours(img_mask_blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow("img_color", img_color)
    for cnt in contours:
        cv2.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)   
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if(w>80):
            print("h: ",h)
            cv2.rectangle(img_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(img_color, (int(x+w/2), int(y+h/2)), 10, (0,0,255))
            x_1= x+w/2-width/2
            y_1= height-(y+h/2)
            #print("x: ",(int(x+w/2), "y: ",int(y+h/2)))
            print("x_1:",x_1,"y_1",y_1)
    
   
    #print("cnt_neck:",cnt_neck)
    print("x: ",x_1,"y: ",y_1)
    
    cv2.imshow("contour_object1", img_color)
    key=cv2.waitKey(1)
    if key == 27:
        return
    return x_1, y_1
    
def capread_green(cap):
    
    #global cnt_neck
    ret, img_color = cap.read()
    imgcopy=img_color.copy()
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
    w=0
    h=0
#=========================================================
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) 
    lower_green = (50, 30, 30) 
    upper_green = (70, 255, 255)
    img_mask_green = cv2.inRange(img_hsv, lower_green, upper_green) 
#_================------------------------====================
    ret, img_binary = cv2.threshold(img_mask_green, 127, 255, 0)
    contours, hierarchy = cv2.findContours(img_mask_green, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow("img_color", img_color)
    for cnt in contours:
        cv2.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)   
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if(w>100):
            print("h: ",h)
            cv2.rectangle(img_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(img_color, (int(x+w/2), int(y+h/2)), 10, (0,0,255))
            x_1= x+w/2-width/2
            y_1= height-(y+h/2)
            #print("x: ",(int(x+w/2), "y: ",int(y+h/2)))
            print("x_1:",x_1,"y_1",y_1)
    
   
    #print("cnt_neck:",cnt_neck)
    print("x: ",x_1,"y: ",y_1)
    
    cv2.imshow("contour_object1", img_color)
    key=cv2.waitKey(1)
    if key == 27:
        return
    return w,h
def contour_main(cap,serial_port):
    cnt_obj=0
    while True:
        print("def_contourpoint1")
        x_1,y_1=capread_blue(cap)
        #cv2.imshow("contour_object1", imgcopy)
        print("def_contourpoint2")
        if x_1>70:
            tr=48
        elif x_1<-70:
            tr= 47
        elif x_1<=70 and x_1>=-70 and x_1!=0:
            if y_1<100 and y_1>0:
                '''
                if cnt_neck==0 :
                    cnt_neck=cnt_neck+1
                    return 57
                elif cnt_neck==1 :
                    cnt_neck=cnt_neck+1
                    return 56
                elif cnt_neck==2 :
                    cnt_neck=cnt_neck+1
                    return 55
                elif cnt_neck==3 :
                    cnt_neck=cnt_neck+1
                    return 53
                elif cnt_neck==4 :
                    cnt_neck=cnt_neck+1
                    return 45
                else :
                    return 44
                    '''
                tr= 57
            else:
                tr=59
        else :
            tr=3
        #==================================================
        print(tr)
        TX_data_py2(serial_port,58)
        print(333)
        #contour_object(cap)
        #tr=contour_object(cap)
        print("cap")
        time.sleep(0.1)
        if tr!=45 and tr!=53 and tr!=55 and tr!=56 and tr!=57: 
            TX_data_py2(serial_port,tr)
            if tr==3:
                time.sleep(0.1)
                for i in range(7):
                    img1, ret=cap.read()
                    time.sleep(0.01)
            print(tr, "missioncomplete?")
        if tr==57 and cnt_obj==0:
            cnt_obj=cnt_obj+1
            print("turnturnturnturnturnturnturnturnturnturnturtrnturnturnt")
            time.sleep(1)
            TX_data_py2(serial_port,2)
            time.sleep(3)
            TX_data_py2(serial_port,2)
            time.sleep(3)
            TX_data_py2(serial_port,59)
            time.sleep(3)
            
            area=[0,0,0,0,0]
            for k in range(2):
                TX_data_py2(serial_port,17) # neck left90
                w,h=capread_green(cap)
                time.sleep(1)
                
                key=cv2.waitKey(1)
                if key == 27:
                    break
                    
                print("w,h",w,h)
                area[0]=w*h
                time.sleep(1)
                TX_data_py2(serial_port,28) # neck left90
                w,h=capread_green(cap)
                area[0]=w*h
                time.sleep(1)
                TX_data_py2(serial_port,21) # neck left90
                w,h=capread_green(cap)
                area[1]=w*h
                time.sleep(1)
                TX_data_py2(serial_port,30) # neck left90
                w,h=capread_green(cap)
                area[2]=w*h
                time.sleep(1)
                TX_data_py2(serial_port,27) # neck left90
                w,h=capread_green(cap)
                area[3]=w*h
                time.sleep(1)
            time.sleep(0.5)# neck left90
            w,h=capread_green(cap)
            time.sleep(1)
            area[4]=w*h
            max=area[0]
            max_i=0
            for i in range(5):
                if max<area[i]:
                    max=area[i]
                    max_i=i
            print("max : ", max)
            print("max_i : " ,max_i)
            TX_data_py2(serial_port,21)
            t=21
            time.sleep(1)
            TX_data_py2(serial_port,53)
            time.sleep(1)
            x_1=0
            y_1=0
            
            while True:
                x_1,y_1=capread_blue(cap)
                key=cv2.waitKey(1)
                if key==27:
                    break
                if x_1>50:
                    TX_data_py2(serial_port,48)
                elif x_1<-70:
                    TX_data_py2(serial_port,47)
                elif x_1==0:
                    continue
                else:
                    break
            time.sleep(1)
            TX_data_py2(serial_port,45)
            time.sleep(3)
            if max_i==0:    #turn left45
                time.sleep(1)
                TX_data_py2(serial_port,22)
                time.sleep(1)
                TX_data_py2(serial_port,22)
                time.sleep(1)
                TX_data_py2(serial_port,22)
                time.sleep(2.5)
                TX_data_py2(serial_port,64)
                time.sleep(2)
                TX_data_py2(serial_port,64)
                time.sleep(2)
                TX_data_py2(serial_port,46)
                time.sleep(3)
            if max_i==1:    #turn left20
                time.sleep(1)
                TX_data_py2(serial_port,7)
                time.sleep(1)
                TX_data_py2(serial_port,7)
                time.sleep(1)
                TX_data_py2(serial_port,7)
                time.sleep(2.5)
                
                TX_data_py2(serial_port,64)
                time.sleep(2)
                TX_data_py2(serial_port,64)
                time.sleep(2)
                TX_data_py2(serial_port,46)
                time.sleep(3)
            if max_i==2:    #turn 0
                time.sleep(1)
                TX_data_py2(serial_port,46)
                time.sleep(3)
            if max_i==3:    #turn right 20
                time.sleep(1)
                TX_data_py2(serial_port,9)
                time.sleep(1)
                TX_data_py2(serial_port,9)
                time.sleep(1)
                TX_data_py2(serial_port,9)
                time.sleep(2.5)
                TX_data_py2(serial_port,64)
                time.sleep(2)
                TX_data_py2(serial_port,64)
                time.sleep(2)
                
                TX_data_py2(serial_port,46)
                time.sleep(3)
            if max_i==4:    #turn right 45
                time.sleep(1)
                TX_data_py2(serial_port,24)
                time.sleep(1)
                TX_data_py2(serial_port,24)
                time.sleep(1)
                TX_data_py2(serial_port,24)
                time.sleep(2.5)
                TX_data_py2(serial_port,64)
                time.sleep(2)
                TX_data_py2(serial_port,64)
                time.sleep(2)
                TX_data_py2(serial_port,46)
                time.sleep(3)
            #TX_data_py2(serial_port,45)
            break
        #cv2.imshow("contour_object1", imgcopy)
            
            
            
            
            TX_data_py2(serial_port,45)
            time.sleep(3)

        print(tr,"asdasdqw-wefjawfkljwqeoifjweriofja;sdifjsd;klfjqwiojfl;aekjf")
        #=====================================================   
        #cv2.imshow("result", img_mask_green)
        
        
     #-------------------------------------------------------


