import cv2
import numpy as np
import sys

facePath = "haarcascade_frontalface_default.xml"
smilePath = "haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

sF = 1.05
print("Bienvenue au projet ---Real Time Smile Detection--")
print("Appuyer sur la touche Q pour quitter à tout moment")
print("**************************************************")
while True:
    ret, frame = cap.read() # on capture frame par frame
    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor= sF,
        minNeighbors=8,
        minSize=(55, 55),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # ---- On trace un rectangle aux environs du visages

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.7,
            minNeighbors=22,
            minSize=(25, 25),
            flags=cv2.CASCADE_SCALE_IMAGE
            )

        # points d'interets du sourire
        for (x, y, w, h) in smile:
            print ("Sourire capturé"), len(smile), ("sourires!")
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
    
       
    cv2.imshow('Real Time Smile Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
