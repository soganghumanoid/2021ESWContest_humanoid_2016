import cv2
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
print("2")
cap.set(3,640)
cap.set(4,480)
while True:
	ret,img = cap.read()
	cv2.imshow("img",img)
	time.sleep(1)
	key=cv2.waitKey(1)
	if key==27:
		break

print("1")
