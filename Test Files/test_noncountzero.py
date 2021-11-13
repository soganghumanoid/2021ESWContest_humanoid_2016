import math
#from def_linedetect09172 import *
#from def_contour_object1004 import *
import serial
import cv2
import numpy as np
import time
key=0

width=640
height=480
cnt_neck=0
cnt_obj=0
#----------------------------------------------------
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
BPS =  4800
while True:
    ret, img_color = cap.read()
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
#=========================================================
    frame=cv2.GaussianBlur(img_color,(5,5),0)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_blue = (0, 0, 0) 
    upper_blue = (255, 100, 100)
    lower_red = (150, 50, 50) 
    upper_red = (180, 255, 255)
    img_mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue) 
    #lower_green = (50, 30,30) #green
    #upper_green = (80, 255, 255)
    #lower_green = (5, 0,0) #yellow
    #upper_green = (48, 255, 255)
    lower_green = (110, 70, 30) 
    upper_green = (130, 255, 255)
    img_mask_green = cv2.inRange(img_hsv, lower_green, upper_green) 
#_================------------------------====================
    cntNotBlack_left=cv2.countNonZero(img_mask_green)
    print(cntNotBlack_left)
    '''
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
    '''
   
    #print("cnt_neck:",cnt_neck)
    #print("x: ",x_1,"y: ",y_1)
    
    cv2.imshow("contour_object1", img_color)
    cv2.imshow("img_mask_green",img_mask_green)
    key=cv2.waitKey(1)
    if key == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
