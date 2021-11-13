import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True: #determine left/right
    ret, img = cap.read()
    
    img=img[90:480,0:640]
    #img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # cvtColor BGR2HSV
    
    height = 480
    width = 640
    sum1=0       #tilt average

    sum2=0
    sumx1=0
    sumx2=0
    '''
    cnt=0
    lower_yellow = (0, 0, 0) #'18,94,140'# hsv image to binary image , adequate value 30
    upper_yellow = (255, 100, 200) #'48,255,255'

    frame=cv2.GaussianBlur(img,(5,5),0)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yellowmask = cv2.inRange(img_hsv, lower_yellow, upper_yellow) # in range white, otherblack
    edges = cv2.Canny(yellowmask,50,150,apertureSize=3)
    cv2.imshow('yellow',yellowmask)
    '''
    cv2.imshow('img',img)
    
    key=cv2.waitKey(1)
    if key==27:
        break

