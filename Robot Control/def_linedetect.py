import cv2
import numpy as np
import math



def linedetect(cap): #determine left/right
    ret, img = cap.read()
    img=img[0:350,0:640]
    #img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # cvtColor BGR2HSV
    
    height = 480
    width = 640
    sum1=0       #tilt average

    sum2=0
    sumx1=0
    sumx2=0

    cnt=0
    lower_yellow = (12, 0, 0) #'18,94,140'# hsv image to binary image , adequate value 30
    upper_yellow = (48, 255, 255) #'48,255,255'

    frame=cv2.GaussianBlur(img,(5,5),0)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yellowmask = cv2.inRange(img_hsv, lower_yellow, upper_yellow) # in range white, otherblack
    edges = cv2.Canny(yellowmask,50,150,apertureSize=3)

    #low_yellow=np.array([18, 94, 140])
    #up_yellow=np.array([48, 255, 255])

    lines = cv2.HoughLines(edges,1,np.pi/180,60)
    
    #cv2.imshow('image',img)
    #cv2.imshow('hsv',img_hsv)
    #cv2.imshow('yellowmask',yellowmask)
    #cv2.imshow('edges',edges)
    cv2.imshow('line',img)
    cv2.imshow('yellow',yellowmask)
    if lines is not None:
        arr2=[[0 for k in range(5)] for j in range(len(lines))]
        for i in range(len(lines)):
            for rho, theta in lines[i]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0+1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 -1000*(a))
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
                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
        arr2.sort(key=lambda x:x[4])
        #print(arr2)print(avgx1)

        for i in range(len(arr2)):
            if i<len(arr2)-1:
                if int(arr2[i][4]+70)<int(arr2[i+1][4]):
                    cnt=i+1
                    x1=arr2[i][0]
                    y1=arr2[i][1]
                    x2=arr2[i][2]
                    y2=arr2[i][3]
                    
                    x3=arr2[i+1][0]
                    y3=arr2[i+1][1]
                    x4=arr2[i+1][2]
                    y4=arr2[i+1][3]
                    if ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))!=0 :
                        Px_up=((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))
                        Px_down=((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
                        Px=Px_up/Px_down
                        Py_up=((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))
                        Py_down=((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
                        Py=Py_up/Py_down
                        cv2.circle(img,(int(Px),int(Py)),20,(0,255,0))
                        #print(Px,Py)# Px, Py point meet.
                        #print("selected")
                        
                        if Py >230:
                            return 50 #17 left 90deg

        if arr2 is not None:
            if cnt!=0 :  
                for i in range(0, cnt):
                    sum1=sum1+arr2[i][4]
                    #print(arr2[i][0])
                    sumx1=sumx1+(arr2[i][0]+arr2[i][2])/2
                avg1=sum1/cnt
                avgx1=sumx1/cnt
                for i in range(cnt, len(arr2)):
                    sum2=sum2+arr2[i][4]
                    sumx2=sumx2+(arr2[i][0]+arr2[i][2])/2
                avg2=sum2/(len(arr2)-cnt)
                avgx2=sum2/(len(arr2)-cnt)
                if abs(avg1)>abs(avg2):
                    tt=avg2
                    avg2=avg1
                    avg1=tt

                    kk=avgx2
                    avgx2=avgx1
                    avgx1=kk
                print(avgx1)
                print ("avg1 avg2 :  ",avg1, avg2)
            else :
                for i in range(len(arr2)):
                    sum1=sum1+arr2[i][4]
                    sumx1=sumx1+(arr2[i][0]+arr2[i][2])/2
                avg1=sum1/len(arr2)
                avgx1=sumx1/len(arr2)
                #print(avgx1)
                print("avg1: ", avg1)
                
            
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
                    return 7
                if avg1<30 and avg1>20:
                    print(-20,"turn")
                    return 9
            elif abs(avg1)>30 and abs(avg1)<40 :
                if avg1>-40 and avg1<-30:
                    print(30,"turn")
                    return 7
                if avg1<40 and avg1>30:
                    print(-40,"turn")
                    return 9
            elif abs(avg1)>40 and abs(avg1)<45 :
                if avg1>-45 and avg1<-40:
                    print(45,"turn")
                    return 24
                if avg1<45 and avg1>40:
                    print(-45,"turn")
                    return 22
            else:
                return 8
       # print("------a")
    else:
        return 8

cv2.waitKey(0)
cv2.destroyAllWindows()
