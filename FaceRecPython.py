import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if trained_face_data.empty():
    raise Exception("Error loading haarcascade_frontalface_default.xml. Make sure the file exists.")

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    raise Exception("Error opening webcam. Make sure it is connected and available.")

while True:
    successful_frame_read, frame = webcam.read()

    if not successful_frame_read:
        print("Error reading frame from the webcam. Check if the webcam is working.")
        break

    mono_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coords = trained_face_data.detectMultiScale(mono_vid)
    
    for (x, y, w, h) in face_coords:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)
    
    cv2.imshow('FINAL DETECTOR', frame)
    key = cv2.waitKey(1)

    if key == 32:
        break

# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()




'''
mono_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_coords = trained_face_data.detectMultiScale(mono_img)
print(face_coords)
for (x, y, w, h) in face_coords:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

cv2.imshow('Modiji face detector', img)
cv2.waitKey()
print("END...")
'''

'''import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if trained_face_data.empty():
    raise Exception("Error loading haarcascade_frontalface_default.xml. Make sure the file exists.")

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()

    if not successful_frame_read:
        print("Error reading frame from the webcam.")
        break

    mono_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coords = trained_face_data.detectMultiScale(mono_vid)
    for (x, y, w, h) in face_coords:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)
    cv2.imshow('FINAL DETECTOR', frame)
    key = cv2.waitKey(1)

    if key == 32:
        break
'''