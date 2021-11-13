import cv2
import uuid
import os

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('frame', frame)


    if cv2.waitKey(2) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

    elif cv2.waitKey(2) & 0xFF == ord('s'):
        # Save the current frame
        
        imgname = os.path.join('{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
