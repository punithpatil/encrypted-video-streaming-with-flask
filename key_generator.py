# This is used to generate two images with random pixel values.

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# Done to extract webcam image shape to get equivalent key image shape

key = np.random.randint(0,255,frame.shape).astype('uint8')
cv2.imwrite("key1.png",key)

key = np.random.randint(0,255,frame.shape).astype('uint8')
cv2.imwrite("key2.png",key)
