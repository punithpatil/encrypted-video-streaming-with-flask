# Decryption algorithm when JPEG frames ae used.
# The image is only partialy decrypted.
import cv2
import urllib 
import numpy as np

stream=urllib.urlopen('http://0.0.0.0:5000/video_feed')
bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        key1 = cv2.imread("key1.png")
        key2 = cv2.imread("key2.png")
        i = cv2.bitwise_xor(i, key2)
        i = cv2.bitwise_xor(i, key1)
        cv2.imshow('i',i)
        if cv2.waitKey(1) ==27:
            exit(0)   
