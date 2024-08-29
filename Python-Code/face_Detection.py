import serial 
import time
import numpy as np 
import cv2 

arduinoData = serial.Serial('COM5', 9600) #Change this based on your serial port

def send_coordinates_to_arduino(x, y, w, h):
    # Convert the coordinates to a string and send it to Arduino
    coordinates = f"{x},{y}\r"
    arduinoData.write(coordinates.encode())
    print(f"X{x}Y{y}\n")

capture = cv2.VideoCapture(0) 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    isTrue, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minSize=(80, 80), minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
        send_coordinates_to_arduino(x, y, w, h)

    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
