import cv2
import numpy as np
import math
import time



def linedetect(cap): #determine left/right
    ret, img = cap.read()
    
    img=img[0:310,0:640]
    #img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # cvtColor BGR2HSV
    
    height = 480
    width = 640
    sum1=0       #tilt average

    sum2=0
    sumx1=0
    sumx2=0

    cnt=0
    lower_yellow = (12,30,80)#1104(14:31)edit(12, 30, 30) #'18,94,140'# hsv image to binary image , adequate value 30
    upper_yellow = (48, 255, 255) #'48,255,255'

    frame=cv2.GaussianBlur(img,(5,5),0)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yellowmask = cv2.inRange(img_hsv, lower_yellow, upper_yellow) # in range white, otherblack
    edges = cv2.Canny(yellowmask,50,150,apertureSize=3)

    #low_yellow=np.array([18, 94, 140])
    #up_yellow=np.array([48, 255, 255])
    lines = cv2.HoughLines(edges,1,np.pi/180,50)
    
    #cv2.imshow('image',img)
    #cv2.imshow('hsv',img_hsv)
    #cv2.imshow('yellowmask',yellowmask)
    #cv2.imshow('edges',edges)
    #cv2.imshow('line',img)
    #cv2.imshow('yellow',yellowmask)
    #key1=cv2.waitKey(0)
    cv2.imshow('yellow',yellowmask)
    cv2.imshow('img',img)
    key1=cv2.waitKey(10)
    if lines is not None:
        time_1=time.time()####============================
        arr2=[[0 for k in range(5)] for j in range(len(lines))]
        time_2=time.time()####============================
        #print("time_2-time_1",time_2-time_1)#===============================
        for i in range(len(lines)):
            for rho, theta in lines[i]: #dot
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*( a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*( a))

                if y1 !=y2 :
                    w=x2-x1
                    h=y2-y1
                    diago=math.sqrt(w*w+h*h)
                    acos_rec=math.asin(h/diago)
                    #print("theta: ",theta*180/3.14)
                    #print(acos_rec*180/3.14)
                arr2[i][0]=x1
                arr2[i][1]=y1
                arr2[i][2]=x2
                arr2[i][3]=y2
                #arr2[i][4]=acos_rec*180/3.14
                theta=theta*180/3.14
                if theta>90 :
                    theta=theta-180
                arr2[i][4]=theta
                #cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)#-===============================
        time_3=time.time()####============================
        #print("time_3-time_2",time_3-time_2)#===============================
        #print("len(lines)",len(lines))
        
        arr2.sort(key=lambda x:x[4])
        #print(arr2)print(avgx1)
    
        for i in range(len(arr2)):
            if i<len(arr2)-1:
                if int(arr2[i][4]+70)<int(arr2[i+1][4]):    #corner detect
                    cnt=i+1
                    x1=arr2[i][0]
                    y1=arr2[i][1]
                    x2=arr2[i][2]
                    y2=arr2[i][3]
                    
                    x3=arr2[i+1][0]
                    y3=arr2[i+1][1]
                    x4=arr2[i+1][2]
                    y4=arr2[i+1][3]
                    if ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))!=0 :   #cross point
                        Px_up=((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))
                        Px_down=((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
                        Px=Px_up/Px_down
                        Py_up=((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))
                        Py_down=((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
                        Py=Py_up/Py_down
                        cv2.circle(img,(int(Px),int(Py)),20,(0,255,0))
                        #print(Px,Py)# Px, Py point meet.
                        #print("selected")
                        
                        if Py >150:  #170       #change point#################
                            return 50 #17 left 90deg
        time_4=time.time()####============================
        #print("time_4-time_3",time_4-time_3)#===============================
        if arr2 is not None:
            if cnt!=0 :  #corner Yes
                ###1113edit###for i in range(0, cnt):     #sum
                ###    sum1=sum1+arr2[i][4]
                ###    #print(arr2[i][0])
                ###    sumx1=sumx1+(arr2[i][0]+arr2[i][2])/2
                ###avg1=sum1/cnt
                ###avgx1=sumx1/cnt     #average
                avg1=arr2[cnt-1][4]
                avgx1=(arr2[cnt-1][0]+arr2[cnt-1][2])/2
                print("arr2[cnt-1][4]:",arr2[cnt-1][4])
                print("arr2[cnt-1][0]:",(arr2[cnt-1][0]+arr2[cnt-1][2])/2)
                ###1113edit###for i in range(cnt, len(arr2)):     #sum
                ###    sum2=sum2+arr2[i][4]
                ###    sumx2=sumx2+(arr2[i][0]+arr2[i][2])/2
                avg2=arr2[cnt][4]
                avgx2=(arr2[cnt][0]+arr2[cnt][2])/2
                ###avg2=sum2/(len(arr2)-cnt)
                ###avgx2=sum2/(len(arr2)-cnt)          #average
    
                if abs(avg1)>abs(avg2):     # vertical ->avg1 , horizontal->avg2
                    tt=avg2
                    avg2=avg1
                    avg1=tt

                    kk=avgx2
                    avgx2=avgx1
                    avgx1=kk
                if abs(avg1)>75 and abs(avg2) >75:
                    avg1=0.1
                    avg2=-91
                #print(len(arr2))
                print(avgx1)
                print ("avg1 avg2 :  ",avg1, avg2)
                time_5=time.time()####============================
                #print("time_5-time_4",time_5-time_4)#===============================
            
            else :  #Corner None
                for i in range(len(arr2)):
                    sum1=sum1+arr2[i][4]
                    sumx1=sumx1+(arr2[i][0]+arr2[i][2])/2
                avg1=sum1/len(arr2)
                avgx1=sumx1/len(arr2)
                #print(avgx1)
                print("avg1: ", avg1)
                
            print("avg1: ",avg1)
            print("avgx1: ",avgx1)
            
            if (abs(avg1)<7) :
                if(avgx1>width/2+130 ):
                    print("-20,move")
                    return 20
                if(avgx1<width/2-130):
                    print("+20,move")
                    return 15
            if (abs(avg1)>7 and abs(avg1)<10) :
                if (avg1>-10 and avg1<-7):
                    print(3,"turn")
                    return 4
                if avg1<10 and avg1>7:
                    print(-3,"turn")
                    return 6
            elif (abs(avg1)>10 and abs(avg1)<20) :
                if (avg1>-20 and avg1<-10):
                    print(10,"turn")
                    return 1
                if avg1<20 and avg1>10:
                    print(-10,"turn")
                    return 3
            elif abs(avg1)>20 and abs(avg1)<30 :
                if avg1>-30 and avg1<-20:
                    print(20,"turn")
                    return 1#7
                if avg1<30 and avg1>20:
                    print(-20,"turn")
                    return 3#9
            elif abs(avg1)>30 and abs(avg1)<40 :
                if avg1>-40 and avg1<-30:
                    print(30,"turn")
                    return 1#7
                if avg1<40 and avg1>30:
                    print(-40,"turn")
                    return 3#9
            elif abs(avg1)>40 and abs(avg1)<50 :
                if avg1>-50 and avg1<-40:
                    print(45,"turn")
                    return 1#24
                if avg1<50 and avg1>40:
                    print(-45,"turn")
                    return 3#22
            elif abs(avg1)>50:
                return 711#68 horzontalline
            else:
                print('avg1:',avg1)
                print('else avgx1:',avgx1)
                return 69#1107edit###67######2
       # print("------a")
    else:
        #print('else avg1:',avg1)
        print('else')
        return 71#edit1110#68#####2
