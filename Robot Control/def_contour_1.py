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
def pixelread_green(cap):
    ret, img_color = cap.read()
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
#=========================================================
    frame=cv2.GaussianBlur(img_color,(5,5),0)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_green = (50, 30,30) 
    upper_green = (80, 255, 255)
    img_mask_green = cv2.inRange(img_hsv, lower_green, upper_green) 
#_================------------------------====================
    cntNotgreen=cv2.countNonZero(img_mask_green)
    return cntNotgreen
def pixelread_black(cap):
    ret, img_color = cap.read()
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
#=========================================================
    frame=cv2.GaussianBlur(img_color,(5,5),0)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_black = (0, 0, 0) 
    upper_black = (255, 100, 100)
    img_mask_black = cv2.inRange(img_hsv, lower_black, upper_black) 
#_================------------------------====================
    cntNotblack=cv2.countNonZero(img_mask_black)
    return cntNotblack
    
def pixelread_red(cap):
    ret, img_color = cap.read()
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
#=========================================================
    frame=cv2.GaussianBlur(img_color,(5,5),0)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = (150, 50, 50) 
    upper_red = (180, 255, 255)
    img_mask_red = cv2.inRange(img_hsv, lower_red, upper_red) 
#_================------------------------====================
    cntNotred=cv2.countNonZero(img_mask_red)
    return cntNotred
def pixelread_blue(cap):
    ret, img_color = cap.read()
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
#=========================================================
    frame=cv2.GaussianBlur(img_color,(5,5),0)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = (110, 70, 30) 
    upper_red = (130, 255, 255)
    img_mask_red = cv2.inRange(img_hsv, lower_red, upper_red) 
#_================------------------------====================
    cntNotred=cv2.countNonZero(img_mask_red)
    return cntNotred    
def capread_black(cap):
        #global cnt_neck
    ret, img_color = cap.read()
    imgcopy=img_color.copy()
    img_color=img_color[100:480,0:640]
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
    w=0
    h=0
    xavg=0
    yavg=0
    xsum=0
    ysum=0
    wsum=0
    hsum=0
    wavg=0
    havg=0
    cnt_sum=0
#=========================================================
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) 
    lower_blue = (0, 0, 0) 
    upper_blue = (255, 100, 100)
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
            xsum=xsum+x_1
            ysum=ysum+y_1
            wsum=wsum+w
            hsum=hsum+h
            cnt_sum=cnt_sum+1
    if cnt_sum!=0:
        xavg=xsum/cnt_sum
        yavg=ysum/cnt_sum
        wavg=wsum/cnt_sum
        havg=hsum/cnt_sum
    elif cnt_sum==0:
        xavg=0
        yavg=0
        wavg=0
        havg=0
    #print("cnt_neck:",cnt_neck)
    print("x: ",x_1,"y: ",y_1)
    
    cv2.imshow("contour_object1", img_color)
    key=cv2.waitKey(1)
    if key == 27:
        return
    return w,h,x_1,y_1
def capread_blue(cap):
        #global cnt_neck
    ret, img_color = cap.read()
    imgcopy=img_color.copy()
    img_color=img_color[100:480,0:640]
    x=0
    y=0
    w=0
    h=0
    x_1=0
    y_1=0
    tr=0
    xavg=0
    yavg=0
    xsum=0
    ysum=0
    wsum=0
    hsum=0
    wavg=0
    havg=0
    cnt_sum=0
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
            xsum=xsum+x_1
            ysum=ysum+y_1
            wsum=wsum+w
            hsum=hsum+h
            cnt_sum=cnt_sum+1
    if cnt_sum!=0:
        xavg=xsum/cnt_sum
        yavg=ysum/cnt_sum
        wavg=wsum/cnt_sum
        havg=hsum/cnt_sum
    elif cnt_sum==0:
        xavg=0
        yavg=0
        wavg=0
        havg=0
   
    #print("cnt_neck:",cnt_neck)
    print("x: ",x_1,"y: ",y_1)
    
    cv2.imshow("contour_object1", img_color)
    key=cv2.waitKey(1)
    if key == 27:
        return
    return w,h, xavg,yavg
def capread_red(cap):
    
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
    xavg=0
    yavg=0
    xsum=0
    ysum=0
    wsum=0
    hsum=0
    wavg=0
    havg=0
    cnt_sum=0
    div_safe=1
    div_danger=0
#=========================================================
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) 
    lower_red = (150, 50, 50) 
    upper_red = (180, 255, 255)
    img_mask_red = cv2.inRange(img_hsv, lower_red, upper_red) 
#_================------------------------====================
    ret, img_binary = cv2.threshold(img_mask_red, 127, 255, 0)
    contours, hierarchy = cv2.findContours(img_mask_red, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
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
            xsum=xsum+x_1
            ysum=ysum+y_1
            wsum=wsum+w
            hsum=hsum+h
            cnt_sum=cnt_sum+1
    if cnt_sum!=0:
        xavg=xsum/cnt_sum
        yavg=ysum/cnt_sum
        wavg=wsum/cnt_sum
        havg=hsum/cnt_sum
    elif cnt_sum==0:
        xavg=0
        yavg=0
        wavg=0
        havg=0
    
   
    #print("cnt_neck:",cnt_neck)
    print("x: ",x_1,"y: ",y_1)
    
    cv2.imshow("contour_object1", img_color)
    key=cv2.waitKey(1)
    if key == 27:
        return
    return w,h,xavg,yavg

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
    xavg=0
    yavg=0
    xsum=0
    ysum=0
    wsum=0
    hsum=0
    wavg=0
    havg=0
    cnt_sum=0
    
#=========================================================
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) 
    #lower_green = (50, 30, 30) 
    #upper_green = (70, 255, 255)
    lower_green = (45, 30,30) 
    upper_green = (80, 255, 255)
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
            xsum=xsum+x_1
            ysum=ysum+y_1
            wsum=wsum+w
            hsum=hsum+h
            cnt_sum=cnt_sum+1
    if cnt_sum!=0:
        xavg=xsum/cnt_sum
        yavg=ysum/cnt_sum
        wavg=wsum/cnt_sum
        havg=hsum/cnt_sum
    elif cnt_sum==0:
        xavg=0
        yavg=0
        wavg=0
        havg=0
   
    #print("cnt_neck:",cnt_neck)
    print("x: ",x_1,"y: ",y_1)
    
    cv2.imshow("contour_object1", img_color)
    key=cv2.waitKey(1)
    if key == 27:
        return
    return w,h,xavg,yavg
def capread_red_wallnone(cap):
    
    #global cnt_neck
    ret, img_color = cap.read()
    imgcopy=img_color.copy()
    img_color=img_color[90:480,0:640]
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
    w=0
    h=0
    xavg=0
    yavg=0
    xsum=0
    ysum=0
    wsum=0
    hsum=0
    wavg=0
    havg=0
    cnt_sum=0
    div_safe=1
    div_danger=0
#=========================================================
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) 
    lower_red = (150, 50, 50) 
    upper_red = (180, 255, 255)
    img_mask_red = cv2.inRange(img_hsv, lower_red, upper_red) 
#_================------------------------====================
    ret, img_binary = cv2.threshold(img_mask_red, 127, 255, 0)
    contours, hierarchy = cv2.findContours(img_mask_red, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
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
            xsum=xsum+x_1
            ysum=ysum+y_1
            wsum=wsum+w
            hsum=hsum+h
            cnt_sum=cnt_sum+1
    if cnt_sum!=0:
        xavg=xsum/cnt_sum
        yavg=ysum/cnt_sum
        wavg=wsum/cnt_sum
        havg=hsum/cnt_sum
    elif cnt_sum==0:
        xavg=0
        yavg=0
        wavg=0
        havg=0
    
   
    #print("cnt_neck:",cnt_neck)
    print("x: ",x_1,"y: ",y_1)
    
    cv2.imshow("contour_object1", img_color)
    key=cv2.waitKey(1)
    if key == 27:
        return
    return w,h,xavg,yavg
def capread_blue_wallnone(cap):
    
    #global cnt_neck
    ret, img_color = cap.read()
    imgcopy=img_color.copy()
    img_color=img_color[90:480,0:640]
    x=0
    y=0
    x_1=0
    y_1=0
    tr=0
    w=0
    h=0
    xavg=0
    yavg=0
    xsum=0
    ysum=0
    wsum=0
    hsum=0
    wavg=0
    havg=0
    cnt_sum=0
    div_safe=1
    div_danger=0
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
        if(w>100):
            print("h: ",h)
            cv2.rectangle(img_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(img_color, (int(x+w/2), int(y+h/2)), 10, (0,0,255))
            x_1= x+w/2-width/2
            y_1= height-(y+h/2)
            xsum=xsum+x_1
            ysum=ysum+y_1
            wsum=wsum+w
            hsum=hsum+h
            cnt_sum=cnt_sum+1
    if cnt_sum!=0:
        xavg=xsum/cnt_sum
        yavg=ysum/cnt_sum
        wavg=wsum/cnt_sum
        havg=hsum/cnt_sum
    elif cnt_sum==0:
        xavg=0
        yavg=0
        wavg=0
        havg=0
    
   
    #print("cnt_neck:",cnt_neck)
    print("x: ",x_1,"y: ",y_1)
    
    cv2.imshow("contour_object1", img_color)
    key=cv2.waitKey(1)
    if key == 27:
        return
    return w,h,xavg,yavg
def contour_main(cap,serial_port,alphabet_color,floor_color,arrow_direction):
    cnt_obj=0
    div_safe=1
    div_danger=0
    div_in=0
    div_out=1
    div_inout_inblack_object=3
    left_turn=1
    right_turn=0
    time_break=4
    time_break270=3
    time_break_none=4
    #===================================when corner, after alphabet
    print("def_contourpoint1")
    time.sleep(2)
    #TX_data_py2(serial_port,24)
    #time.sleep(2)
    #TX_data_py2(serial_port,9)#turn 45
    #time.sleep(2)
    TX_data_py2(serial_port,58)#neck_under23
    time.sleep(1)
    #====================================danger,safe classification
    for kkk in range(9):
        imgdf=cap.read()
        time.sleep(0.2)
        key2=cv2.waitKey(1)
    for k in range(9):#div danger,safe
        # neck left90
        time.sleep(0.2)
        #w_green,h_green,qqq,qqqq=capread_green(cap)
        area_black=pixelread_black(cap)
        time.sleep(0.2)
        area_green=pixelread_green(cap)
        #w_black,h_black,qqq,qqqq=capread_black(cap)
        key=cv2.waitKey(1)
        if key == 27:
            break
        #area_green=w_green*h_green   #frame-> change
        #area_black=w_black*h_black
        
        print("area_black: ",area_black)
        print("area_green: ",area_green)
        
    time.sleep(0.5)
    time.sleep(0.5)# neck left90
    if area_green>area_black:#div by if 
        div_gb=div_safe
        floor_color.append(div_gb)
        TX_data_py2(serial_port,41) #say safe
        
        time.sleep(0.5)
        print('safesafesafesafesafesafe')
    else:
        div_gb=div_danger
        floor_color.append(div_gb)
        TX_data_py2(serial_port,42) #say danger
        time.sleep(0.5)
        print('dangerdangerdangerdangerdanger')
    time.sleep(1)
    if div_gb==div_danger:# when danger, to turn and 
        ##########################edit 1110
        time.sleep(1)
        for i in range(8):
            if alphabet_color==1: #red
                pixel_red=pixelread_red(cap)
            elif alphabet_color==0: #blue
                pixel_red=pixelread_blue(cap)
            time.sleep(0.11)
        
            
    TX_data_py2(serial_port,21)
    turn_break270_time1=time.time()
    while True:
        if div_gb==div_danger:
            if pixel_red>=12000:
                div_inout_inblack_object=div_in
                div_inout=div_in
            elif pixel_red<12000:#edti 1110
                div_inout_inblack_object=div_out
                div_inout=div_out
                break
        #==================================turn, detect object, go, pick
        if(alphabet_color==0):#blue
            if div_gb==div_safe:
                qqq,qqqq,x_1,y_1=capread_blue(cap) #qqq,qqqq useless
            elif div_gb==div_danger:
                qqq,qqqq,x_1,y_1=capread_blue_wallnone(cap)
        elif(alphabet_color==1):#red
            if div_gb==div_safe:
                qqq,qqqq,x_1,y_1=capread_red(cap) #qqq,qqqq useless
            elif div_gb==div_danger:
                qqq,qqqq,x_1,y_1=capread_red_wallnone(cap)
        #cv2.imshow("contour_object1", imgcopy)
        print("def_contourpoint2")
        if x_1>70:#detect object and go by if / tr=xx ->Txdata
            tr=48
        elif x_1<-70:
            tr= 47
        elif x_1<=70 and x_1>=-70 and x_1!=0:
            if y_1<100 and y_1>0:
                tr= 57
            else:
                tr=67
        else :
            tr=3
        #==================================================
        if tr==3 and arrow_direction==left_turn:
            tr=1
        print(tr)
        if div_gb==div_danger:####edit 1110
            TX_data_py2(serial_port,58)
        else:    
            TX_data_py2(serial_port,57)
        print(333)
        #contour_object(cap)
        #tr=contour_object(cap)
        time.sleep(0.1)
        
        turn_break270_time2=time.time()#edit1110
        print("turn_break_tim(): ",turn_break270_time2-turn_break270_time1)
        if (turn_break270_time2-turn_break270_time1)>32:
            time_break=time_break270
            time.sleep(2)
            TX_data_py2(serial_port,53)
            time.sleep(2)
            break
        if tr!=45 and tr!=53 and tr!=55 and tr!=56 and tr!=57: #if not detect or detecting left, right
            TX_data_py2(serial_port,tr)
            if tr==3:
                time.sleep(0.1)
                for i in range(7):
                    img1, ret=cap.read()
                    time.sleep(0.01)
            print(tr, "missioncomplete?")
        if tr==57 and cnt_obj==0:# when detect blue or red object
            '''
            if(div_gb==div_safe):#blue
                qqq,qqqq,x_1,y_1=capread_blue(cap) #qqq,qqqq useless
            elif(alphabet_color==1):#red
                qqq,qqqq,x_1,y_1=capread_red(cap) 
            '''
            cnt_obj=cnt_obj+1
            #print("turnturnturnturnturnturnturnturnturnturnturtrnturnturnt")
            time.sleep(1)
            TX_data_py2(serial_port,2)#go 6
            time.sleep(3)
            '''
            TX_data_py2(serial_port,2)
            time.sleep(3)
            '''
            if div_gb==div_danger:
                TX_data_py2(serial_port,2) # go 6 edit 1110
            time.sleep(3)
            TX_data_py2(serial_port,67)#go 2
            time.sleep(3)
            TX_data_py2(serial_port,67)#go 2
            time.sleep(3)
            TX_data_py2(serial_port,67)#go 2
            time.sleep(3)
            
            area=[0,0,0,0,0]
            if div_gb==div_safe:
                for k in range(2):# neck 5times and div where to go
                    TX_data_py2(serial_port,17) # neck left90
                    if div_gb==div_safe :
                        w,h,qqq,qqqq=capread_green(cap) #qqq,qqqq useless
                        
                        time.sleep(0.5)
                    elif div_gb==div_danger:
                        w,h,qqq,qqqq=capread_black(cap)
                        time.sleep(1)
                        
                        time.sleep(0.5)
                    time.sleep(1)
                    
                    key=cv2.waitKey(1)
                    if key == 27:
                        break
                        
                    print("w,h",w,h)
                    area[0]=w*h
                    time.sleep(1)
                    TX_data_py2(serial_port,28) # neck left90
                    if div_gb==div_safe :
                        w,h,qqq,qqqq=capread_green(cap) #qqq,qqqq useless
                    elif div_gb==div_danger:
                        w,h,qqq,qqqq=capread_black(cap)
                    area[0]=w*h
                    time.sleep(1)
                    TX_data_py2(serial_port,21) # neck left90
                    if div_gb==div_safe :
                        w,h,qqq,qqqq=capread_green(cap) #qqq,qqqq useless
                    elif div_gb==div_danger:
                        w,h,qqq,qqqq=capread_black(cap)
                    area[1]=w*h
                    time.sleep(1)
                    TX_data_py2(serial_port,30) # neck left90
                    if div_gb==div_safe :
                        w,h,qqq,qqqq=capread_green(cap) #qqq,qqqq useless
                    elif div_gb==div_danger:
                        w,h,qqq,qqqq=capread_black(cap)
                    area[2]=w*h
                    time.sleep(1)
                    TX_data_py2(serial_port,27) # neck left90
                    if div_gb==div_safe :
                        w,h,qqq,qqqq=capread_green(cap) #qqq,qqqq useless
                    elif div_gb==div_danger:
                        w,h,qqq,qqqq=capread_black(cap)
                    area[3]=w*h
                    time.sleep(1)
            time.sleep(0.5)# neck left90
            if div_gb==div_safe :
                w,h,qqq,qqqq=capread_green(cap) #qqq,qqqq useless
            elif div_gb==div_danger:
                w,h,qqq,qqqq=capread_black(cap)
            time.sleep(1)
            area[4]=w*h
            max=area[0]
            max_i=0
            for i in range(5):# by neck 5tiems, choose where to go by if max<area
                if max<area[i]:
                    max=area[i]
                    max_i=i
            print("max : ", max)
            print("max_i : " ,max_i)
            TX_data_py2(serial_port,21)#head left right mid
            t=21
            time.sleep(1)
            TX_data_py2(serial_port,53)#head 75
            time.sleep(1)
            x_1=0
            y_1=0
            
            while True:# when dochak, 5times -> moving to go center object 
                if(alphabet_color==0):#blue
                    qqq,qqqq,x_1,y_1=capread_blue(cap) #qqq,qqqq useless
                elif(alphabet_color==1):#red
                    qqq,qqqq,x_1,y_1=capread_red(cap)
                key=cv2.waitKey(1)
                if key==27:
                    break
                if x_1>70:
                    TX_data_py2(serial_port,48)#right moving 20
                elif x_1<-70:
                    TX_data_py2(serial_port,47)#left moving20
                elif x_1<=500 and x_1>=-50 and x_1!=0:
                    if y_1<100 and y_1>0:
                        TX_data_py2(serial_port,59)#left moving20
                    else:
                        break
                elif x_1==0:
                    continue
                else:
                    continue
            time.sleep(1)
            #=========================================pixel read to div in out
            for i in range(7):
                if div_gb==div_safe:
                    pixel_green=pixelread_green(cap)
                    print('pixel_green:',pixel_green)
                if div_gb==div_danger:
                    pixel_black=pixelread_black(cap)
                    print('pixel_black:',pixel_black)
                time.sleep(0.1)
            #=========================================div in out
            if div_gb==div_safe:#div in out
                if pixel_green>90000:
                    div_inout=div_in
                else:
                    div_inout=div_out
            ###edit1113###
            #elif div_gb==div_danger:
                #if pixel_black>90000:
                #    div_inout=div_in
                #else:
                #    div_inout=div_out
            #============================================pick and go
            if div_inout==div_out and div_gb==div_safe:# safe , green ,out(pick)
                TX_data_py2(serial_port,45)#pick 
                time.sleep(3)
                if max_i==0:    #turn left45
                    time.sleep(1)
                    TX_data_py2(serial_port,22)#left turn 45
                    time.sleep(1)
                    TX_data_py2(serial_port,22)#left turn 45
                    time.sleep(1)
                    TX_data_py2(serial_port,22)#left turn 45
                    time.sleep(2.5)
                    TX_data_py2(serial_port,64)#junjin6
                    time.sleep(2)
                    TX_data_py2(serial_port,65)#junjin6
                    time.sleep(2)
                    TX_data_py2(serial_port,46)#pick off
                    time.sleep(3)
                if max_i==1:    #turn left20
                    time.sleep(1)
                    TX_data_py2(serial_port,7)#left turn 20
                    time.sleep(1)
                    TX_data_py2(serial_port,7)#left turn 20
                    time.sleep(1)
                    TX_data_py2(serial_port,7)#left turn 20
                    time.sleep(2.5)
                    
                    TX_data_py2(serial_port,64)#junjin6
                    time.sleep(2)
                    TX_data_py2(serial_port,65)#junjin6
                    time.sleep(2)
                    TX_data_py2(serial_port,46)#pick off
                    time.sleep(3)
                if max_i==2:    #turn 0
                    time.sleep(1)
                    TX_data_py2(serial_port,64)
                    time.sleep(2.5)
                    TX_data_py2(serial_port,65)#junjin6
                    time.sleep(2)
                    TX_data_py2(serial_port,46)
                    time.sleep(3)
                if max_i==3:    #turn right 20
                    time.sleep(1)
                    TX_data_py2(serial_port,9)#right turn 20
                    time.sleep(1)
                    TX_data_py2(serial_port,9)#right turn 20
                    time.sleep(1)
                    TX_data_py2(serial_port,9)#right turn 20
                    time.sleep(2.5)
                    TX_data_py2(serial_port,64)#junjin6
                    time.sleep(2)
                    TX_data_py2(serial_port,65)#junjin6
                    time.sleep(2)
                    
                    TX_data_py2(serial_port,46)#pick off
                    time.sleep(3)
                if max_i==4:    #turn right 45
                    time.sleep(1)
                    TX_data_py2(serial_port,24)#right turn 45
                    time.sleep(1)
                    TX_data_py2(serial_port,24)#right turn 45
                    time.sleep(1)
                    TX_data_py2(serial_port,24)#right turn 45
                    time.sleep(2.5)
                    TX_data_py2(serial_port,64)#junjin6
                    time.sleep(2)
                    TX_data_py2(serial_port,65)#junjin6
                    time.sleep(2)
                    TX_data_py2(serial_port,46)#pick off
                    time.sleep(3)
            elif div_inout==div_in and div_gb==div_safe:# safe, green ,in
                print("no mission")
                
            elif div_inout==div_out and div_gb==div_danger:# danger,black,out,break
                print("no mission")
                break
            elif div_inout==div_in and div_gb==div_danger:# danger,black,in(pick),break
                TX_data_py2(serial_port,45)#pick 
                time.sleep(3)
                for i in range(9):
                    TX_data_py2(serial_port,22)#back6
                    time.sleep(2)
                TX_data_py2(serial_port,64)#junjin6
                time.sleep(2.5)
                #TX_data_py2(serial_port,64)
                #time.sleep(2.5)
                TX_data_py2(serial_port,22)
                time.sleep(2)
                TX_data_py2(serial_port,46)
                time.sleep(3)
                TX_data_py2(serial_port,24)
                time.sleep(2)
                break
                
            #TX_data_py2(serial_port,45)
            #======================================go back/ green,out
            '''###edit1113###
            if div_gb==div_safe : #pick inside of green
                for i in range(10):
                    TX_data_py2(serial_port,22)#back6
                    time.sleep(2)
                TX_data_py2(serial_port,2)
                time.sleep(2.5)
                TX_data_py2(serial_port,2)
                time.sleep(2.5)
                TX_data_py2(serial_port,2)
                time.sleep(2.5)
            '''
            ###edit 11113###
            '''
            #=================================================turn and little go
            if div_gb==div_safe and div_inout==div_out:
                if max_i==0:
                    TX_data_py2(serial_port,24)#right turn 45
                    time.sleep(1)
                    TX_data_py2(serial_port,24)#right turn 45
                    time.sleep(2.5)
                elif max_i==1:
                    TX_data_py2(serial_port,9)#right turn 20
                    time.sleep(1)
                    TX_data_py2(serial_port,9)#right turn 20
                    time.sleep(2.5)
                elif max_i==2:
                    time.sleep(1)
                    TX_data_py2(serial_port,7)#left turn 20
                    time.sleep(1)
                    TX_data_py2(serial_port,7)#left turn 20
                    time.sleep(2.5)
                elif max_i==3:
                    TX_data_py2(serial_port,22)#left turn 45
                    time.sleep(1)
                    TX_data_py2(serial_port,22)#left turn 45
                    time.sleep(2.5)
                #TX_data_py2(serial_port,67)
                #TX_data_py2(serial_port,2)
                #time.sleep(2)
            '''
            break
            
        #cv2.imshow("contour_object1", imgcopy)
            
            
            
            
            TX_data_py2(serial_port,45)
            time.sleep(3)
        
        #print(tr,"asdasdqw-wefjawfkljwqeoifjweriofja;sdifjsd;klfjqwiojfl;aekjf")
        #=====================================================   
        #cv2.imshow("result", img_mask_green)
        
        
     #-------------------------------------------------------

    if div_gb==div_danger:
        if pixel_red<12000:#when no red => break (ui e su hae jum) and turn and next level #edit1110
            if arrow_direction==right_turn:
                time.sleep(2)
                TX_data_py2(serial_port,22)
                time.sleep(2)
                TX_data_py2(serial_port,7)
                time.sleep(1)
            if arrow_direction==left_turn:
                time.sleep(2)
                TX_data_py2(serial_port,24)
                time.sleep(2)
                TX_data_py2(serial_port,9)
                time.sleep(1)
    return div_gb,div_inout_inblack_object,time_break
