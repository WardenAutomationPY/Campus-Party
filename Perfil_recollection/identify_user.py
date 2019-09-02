import cv2
import matplotlib.pyplot as plt
import face_recognition 
import os
import numpy as np
# def capturePhoto():
#     print("We need to take a picture of you. Pleas write 'continue' if you want to take a photo or 'no' if you don't want.")
#     click = input("Write here: ").lower()
#     print(click)
#     if click == "continue":
#         cap = cv2.VideoCapture(0)
#         if cap.isOpened():
#             ret,frame = cap.read()
#         else:
#             ret = False
#         image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

#         plt.imshow(image)
#         plt.title("Your Photo")
#         plt.xticks([])
#         plt.yticks([])
#         plt.show()

#         cap.release()
#def readFolder():
    
	#if os.path.isdir(os.path.join(carpeta,archivo)):
	#	devolverArchivos(os.path.join(carpeta,archivo))

    



#resutls = face_recognition.compare_faces(bd['faceCoding'],unknown_face_encoding)
if __name__ == "__main__":
    know_faces = []
    know_name = []
    path = './DataBase/'
    for file in os.listdir(path):
        name = file.split('.jpg')[0]
        face = face_recognition.load_image_file(path + file)
        face_encoding = face_recognition.face_encodings(face)[0]
        know_name.append(name)
        know_faces.append(face_encoding)
    

    #readFolder()
    #Loading photos to compare
    # obama_image = face_recognition.load_image_file('obama.jpg')
    # obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    print(know_name)
    print(know_faces)
    # unknown_image = face_recognition.load_image_file('dalk.jpg')
    # unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    
    #Compare faces
    # resutls = face_recognition.compare_faces(know_faces,obama_image)
    # if resutls[0]:
    #     print("Is Obama")
    # else:
    #     print("Is not Obama")
    