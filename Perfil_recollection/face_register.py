from mtcnn.mtcnn import MTCNN
import numpy as np
import cv2
import matplotlib.pyplot as plt
#tagqG60pjYb5OfMlzh0XA098
detector = MTCNN()

cap = cv2.VideoCapture(0)

print('probando')

while True:
    ret, frame = cap.read()

    detect_face = detector.detect_faces(frame)
    
    Usarname = input('Ingrese un Usarname: ')

    if len(detect_face) > 0:
        x = detect_face[0]['box'][0]
        y = detect_face[0]['box'][1]
        width = detect_face[0]['box'][2]
        height = detect_face[0]['box'][3]
        crop_face = frame[y - 14:y + height + 14, x - 6:x + width + 10]
        cv2.imwrite('./DataBase/'+Usarname+'.jpg', crop_face)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()