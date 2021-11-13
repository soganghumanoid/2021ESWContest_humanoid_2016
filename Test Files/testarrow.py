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

def load_labels(path='labels_arrow.txt'):
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

def main_arrow():
    labels = load_labels()
    interpreter = Interpreter('detect_arrow_1004_2.tflite')
    interpreter.allocate_tensors()
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    arrow_position = None
    corner_position = None
    time1 = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        time2 = time.time()
        timer = time2-time1
        print(timer)
        img = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), (320,320))
        res = detect_objects(interpreter, img, 0.5)
        print('run')

        for result in res:
            ymin, xmin, ymax, xmax = result['bounding_box']
            xmin = int(max(1,xmin * CAMERA_WIDTH))
            xmax = int(min(CAMERA_WIDTH, xmax * CAMERA_WIDTH))
            ymin = int(max(1, ymin * CAMERA_HEIGHT))
            ymax = int(min(CAMERA_HEIGHT, ymax * CAMERA_HEIGHT))
            center_x = int((xmin+xmax)/2)
            cv2.rectangle(frame,(xmin, ymin),(xmax, ymax),(0,255,0),3)
            cv2.putText(frame,labels[int(result['class_id'])],(xmin, min(ymax, CAMERA_HEIGHT-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)



            classid = int(result['class_id'])

            if classid == 0:
                arrow_position = center_x
            elif classid == 1:
                corner_position = center_x


        print(res)
        cv2.imshow('Pi Feed', frame)
        if corner_position != None and arrow_position != None:
            print('arrow corner exist')
            if corner_position>=arrow_position:
                arrow_direction = 0     #right
                print('right_')
                return arrow_direction

            elif corner_position<arrow_position:
                arrow_direction = 1     #left
                print('left_')
                return arrow_direction
                
        if timer>5:
            TX_data_py2(serial_port,68)
            time1 = time.time()
            




def TX_data_py2(ser, one_byte):  # one_byte= 0~255

    ser.write(serial.to_bytes([one_byte]))  #python3

if __name__ == "__main__":
    



    
    BPS =  4800  # 4800,9600,14400, 19200,28800, 57600, 115200

    #---------local Serial Port : ttyS0 --------
    #---------USB Serial Port : ttyAMA0 --------


    serial_port = serial.Serial('/dev/ttyS0', BPS, timeout=0.01)
    serial_port.flush() # serial cls
    
    arrow_direction=main_arrow()
    print('arrow_direction:', arrow_direction)
    
    '''
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
