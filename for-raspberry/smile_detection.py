
# importation des bibliotheques
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import imutils
import numpy as np


#inclusion des fichiers classifiers pour le smile et pour la face
cascPath = "haarcascade_frontalface_default.xml"
font = cv2.FONT_HERSHEY_SIMPLEX

faceCascade = cv2.CascadeClassifier(cascPath)


casc_smile_path = "haarcascade_smile.xml"
smile_cascade = cv2.CascadeClassifier(casc_smile_path)

 
#initialisation de la camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(640, 480))
 
time.sleep(0.1)

# on fait une capture frame par frame

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# on recupere le tableau nympy
	image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #print(" La touche q permet de quitter le programme.")
        print(" Bienvenue dans le projet de detction du sourire")
        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor= 1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=0
         )
        
        # processus de d'identification du visage avec un rectangle tracé
        for (x, y, w, h) in faces:
                cv2.rectangle(image,(x,y), (x+w, y+h), (0,255,100), 1)

                roi_gray = gray[y:y+h, x:x+w]
                roi_color = image[y:y+h, x:x+w]

                smile = smile_cascade.detectMultiScale(
                    roi_gray,
                    scaleFactor= 1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=0
                )

                # processus de d'identification du sourire avec un rectangle tracé
                for (x2, y2, w2, h2) in smile:
                    print ("Found"), len(smile), ("smiles!")
                    cv2.rectangle(roi_color, (x2, y2), (x2+w2, y2+h2), (0, 255, 100), 1)
                    time.sleep(0.01)

         
	# on afficher les frams
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear du stream pour la prochaine frame
	rawCapture.truncate(0)

	
 
	# on appuie le `q` pour quitter
	if key == ord("q"):

              break

cv2.destoryAllWindows()
for i in range(1,5):
    cv2.waitKey(1)
