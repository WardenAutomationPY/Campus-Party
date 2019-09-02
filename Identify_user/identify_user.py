import cv2
#import matplotlib.pyplot as plt
import face_recognition 
import os
import numpy as np

def econdingFacesDB():
    #Encoding photos and create list  
    know_faces = []
    know_name = []
    path = './BaseDatos/'
    for file in os.listdir(path):
        name = file.split('.jpg')[0]
        face = face_recognition.load_image_file(path + file)
        # face_location = face_recognition.face_locations(face)
        face_encoding = face_recognition.face_encodings(face)[0]
        know_name.append(name)
        know_faces.append(face_encoding)
    return (know_faces,know_name)

def CompareFaces(newFace,knowFaces):

    new_face_encoding = face_recognition.face_encodings(newFace)[0]
    #Compare faces
    resutls = face_recognition.compare_faces(knowFaces[0],new_face_encoding)
    if resutls[0]:
        print('True')
        return True
    else:
        print('False')
        return False

 

if __name__ == "__main__":
   
    #faces = econdingFacesDB()
    # print(econdingFacesDB()[1])
    #Loading photos to compare
    obama2_image = face_recognition.load_image_file('obama2.jpeg')
    #obama2_location = face_recognition.face_locations(obama2_image)
    #obama2_face_encoding = face_recognition.face_encodings(obama2_image)[0]
    unknown_image = face_recognition.load_image_file('dalk.jpg')
    #unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    faces = econdingFacesDB()
    CompareFaces(unknown_image,faces)