# Based on https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/raspberry_pi/README.md
import re
import cv2
from tflite_runtime.interpreter import Interpreter
import numpy as np
import serial
import time
import sys
from threading import Thread

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

def load_labels(path='labels_abcd_1004.txt'):
  """Loads the labels file. Supports files with or without index numbers."""
  with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    labels = {}
    for row_number, content in enumerate(lines):
      pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
      if len(pair) == 2 and pair[0].strip().isdigit():
        labels[int(pair[0])] = pair[1].strip()
      else:
        labels[row_number] = pair[0].strip()
  return labels

def set_input_tensor(interpreter, image):
  """Sets the input tensor."""
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = np.expand_dims((image-255)/255, axis=0)


def get_output_tensor(interpreter, index):
  """Returns the output tensor at the given index."""
  output_details = interpreter.get_output_details()[index]
  tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
  return tensor


def detect_objects(interpreter, image, threshold):
  """Returns a list of detection results, each a dictionary of object info."""
  set_input_tensor(interpreter, image)
  interpreter.invoke()
  # Get all output details
  boxes = get_output_tensor(interpreter, 0)
  classes = get_output_tensor(interpreter, 1)
  scores = get_output_tensor(interpreter, 2)
  count = int(get_output_tensor(interpreter, 3))

  results = []
  for i in range(count):
    if scores[i] >= threshold:
      result = {
          'bounding_box': boxes[i],
          'class_id': classes[i],
          'score': scores[i]
      }
      results.append(result)
  return results

def main_abcd(cap, serial_port):
    labels = load_labels()
    interpreter = Interpreter('detect_abcd_1004_2.tflite')
    interpreter.allocate_tensors()
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

    #cap = cv2.VideoCapture(0)
    #cap.set(3,640)
    #cap.set(4,480)
    a=4
    time1 = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        time2 = time.time()
        timer = time2-time1
        img = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), (320,320))
        res = detect_objects(interpreter, img, 0.5)
        print('run')
        blue_w = 0
        red_w = 0
        for result in res:
            ymin, xmin, ymax, xmax = result['bounding_box']
            xmin = int(max(1,xmin * CAMERA_WIDTH))
            xmax = int(min(CAMERA_WIDTH, xmax * CAMERA_WIDTH))
            ymin = int(max(1, ymin * CAMERA_HEIGHT))
            ymax = int(min(CAMERA_HEIGHT, ymax * CAMERA_HEIGHT))

            cv2.rectangle(frame,(xmin, ymin),(xmax, ymax),(0,255,0),3)
            cv2.putText(frame,labels[int(result['class_id'])],(xmin, min(ymax, CAMERA_HEIGHT-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)


        
            roi_image = frame[ymin:ymax, xmin:xmax].copy()
            hsv_roi = cv2.cvtColor(roi_image, cv2.COLOR_BGR2HSV)
            
            lower_blue = np.array([110,70,30])
            upper_blue = np.array([130,255,255])
            lower_red = np.array([150, 50, 50])
            upper_red = np.array([180, 255, 255])

            bluemask_roi = cv2.inRange(hsv_roi, lower_blue, upper_blue)
            redmask_roi = cv2.inRange(hsv_roi, lower_red, upper_red)
            
            blue_w=cv2.countNonZero(bluemask_roi)
            red_w=cv2.countNonZero(redmask_roi)
            '''
            contours_blue, hierarchy_blue = cv2.findContours(bluemask_roi, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            contours_red, hierarchy_red = cv2.findContours(redmask_roi, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            
            for cnt in contours_blue:

                x_b, y_b, w_b, h_b = cv2.boundingRect(cnt)
                if(w_b>50):
                    blue_w = w_b
            for cnt in contours_red:
                x_r, y_r, w_r, h_r = cv2.boundingRect(cnt)
                if(w_r>50):
                    red_w = w_r
            '''
            




            if(blue_w>red_w):
                print('blue', blue_w, red_w)
                alphabet_color = 0 #blue

            else:
                print('red',blue_w, red_w)
                alphabet_color = 1 #red


            classid = int(result['class_id'])


            if classid == 0:
                a=0
            elif classid == 1:
                a=1
            elif classid == 2:
                a=2
            elif classid == 3:
                a=3

        print(res)
        
        #cv2.imshow('Pi Feed', frame)

        if a==0:
            print("alphabet_color(blue0 red1) : ",alphabet_color)
            return a, alphabet_color
            cap.release()
            cv2.destroyAllWindows()

        elif a==1:
            print("alphabet_color(blue0 red1) : ",alphabet_color)
            return a, alphabet_color
            cap.release()
            cv2.destroyAllWindows()

        elif a==2:
            print("alphabet_color(blue0 red1) : ",alphabet_color)
            return a, alphabet_color
            cap.release()
            cv2.destroyAllWindows()

        elif a==3:
            print("alphabet_color(blue0 red1) : ",alphabet_color)
            return a, alphabet_color
            cap.release()
            cv2.destroyAllWindows()
            
        if timer>5:
            TX_data_py2(serial_port,68)
            time1 = time.time()

def TX_data_py2(ser, one_byte):  # one_byte= 0~255

    ser.write(serial.to_bytes([one_byte]))  #python3

if __name__ == "__main__":
    alphabet_abcd, alphabet_color =main()
    print('alphabet_abcd:',alphabet_abcd, 'alphabet_color:', alphabet_color) #alphabet_abcd   0 for a/ 1 for b/ 2 for c/ 3 for d
                                                                             #alphabet_color 0 for blue/ 1 for red



    '''
    BPS =  4800  # 4800,9600,14400, 19200,28800, 57600, 115200

    #---------local Serial Port : ttyS0 --------
    #---------USB Serial Port : ttyAMA0 --------


    serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
    serial_port.flush() # serial cls
    if int(b) == 0: # e

        serial_t = Thread(target=TX_data_py2, args=(serial_port, 37))
        serial_t.daemon = True
        serial_t.start()
        serial_t.join()

    elif int(b) == 1: # n

        serial_t = Thread(target=TX_data_py2, args=(serial_port, 40))
        serial_t.daemon = True
        serial_t.start()
        serial_t.join()

    elif int(b) == 2: # s

        serial_t = Thread(target=TX_data_py2, args=(serial_port, 39))
        serial_t.daemon = True
        serial_t.start()
        serial_t.join()

    elif int(b) == 3: # w

        serial_t = Thread(target=TX_data_py2, args=(serial_port, 38))
        serial_t.daemon = True
        serial_t.start()
        serial_t.join()
    '''
    print('finish')
