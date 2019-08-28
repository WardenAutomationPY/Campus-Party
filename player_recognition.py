from mtcnn.mtcnn import MTCNN
import numpy as np
import cv2
import matplotlib.pyplot as plt
#tagqG60pjYb5OfMlzh0XA098
detector = MTCNN()

cap = cv2.VideoCapture(0)

print('probando')

def get_pixels(image):
    r, g, b = 0, 0, 0
    count = 0
    for img in image:
        colors = image[img]
        r += colors[0]
        g += colors[1]
        b += colors[2]
        count += 1

    return (r/count), (g/count), (b/count), count

while False:
    ret, frame = cap.read()

    detect_face = detector.detect_faces(frame)

    if len(detect_face) > 0:
        x = detect_face[0]['box'][0]
        y = detect_face[0]['box'][1]
        width = detect_face[0]['box'][2]
        height = detect_face[0]['box'][3]
        crop_face = frame[y - 14:y + height + 14, x - 6:x + width + 10]
        cv2.imwrite('Rostro.jpg', crop_face)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([235,173,127],np.uint8)

rostro = cv2.imread("Rostro.jpg")
rostroYCrCb = cv2.cvtColor(rostro,cv2.COLOR_BGR2YCR_CB)
pielYCrCb = cv2.inRange(rostroYCrCb,min_YCrCb,max_YCrCb)

pielYCrCb = cv2.bitwise_and(rostro, rostro, mask = pielYCrCb)

color = ('r','g','b')
for i,col in enumerate(color):
    histr = cv2.calcHist([pielYCrCb],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.ylim([0,500])
#plt.show()

import scipy.misc
print(scipy.misc.imread('ycrcb.png').mean(axis=(0,1)))


#cv2.imwrite("ycrcb.png", np.hstack([pielYCrCb]))
