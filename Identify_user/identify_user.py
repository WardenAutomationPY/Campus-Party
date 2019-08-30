import cv2
import matplotlib.pyplot as plt
import face_recognition 
import os
import numpy as np


if __name__ == "__main__":

    #Encoding photos and create arrays   
    know_faces = []
    know_name = []
    path = './BaseDatos/'
    for file in os.listdir(path):
        name = file.split('.jpg')[0]
        face = face_recognition.load_image_file(path + file)
        face_encoding = face_recognition.face_encodings(face)[0]
        know_name.append(name)
        know_faces.append(face_encoding)
    
   
 
    #Loading photos to compare
    obama_image = face_recognition.load_image_file('obama.jpg')
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    #unknown_image = face_recognition.load_image_file('dalk.jpg')
    #unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    
    #Compare faces
    resutls = face_recognition.compare_faces(know_faces,obama_face_encoding)
    if resutls[0]:
        print("Is Obama")
    else:
        print("Is not Obama")
    