# smile-detection

Simple project based on smile detection.

We build a smile detector using OpenCV which takes in live feed from webcam or Raspberry Pi Camera.
To detect the smile, first one has to use OpenCV to detect the face of a person. 
Secondly, Haar-cascades classifiers are used to detect features (of face in this case) by superimposing predefined patterns over face segments and are used as XML files.

In our model, we shall use face, eye and smile haar-cascades, which after downloading need to be placed in the working directory.

This project is done on Pycharm IDE using Python language.
