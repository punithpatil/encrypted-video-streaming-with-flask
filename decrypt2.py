# Decryption algorithm PNG images are used as video feed.
import cv2
import urllib 
import numpy as np

stream=urllib.urlopen('http://0.0.0.0:5000/video_feed')
# Open the image URL
bytes=''
key1 = cv2.imread("key1.png")
key2 = cv2.imread("key2.png")

while True:
    bytes+=stream.read(92300)
    # Buffer length is set for the webcam I have, 640x480.
    # PNG images were found to have an approximate size of 92300 bytes.
    # 1024 bytes can also be used as buffer length, but this introduces lag.
    
    a = bytes.find('\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')
    # All PNG images have "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a" as the starting header.
    
    next = bytes[a+8:]
    # Skip the found 8 bytes.
    
    b = next.find('\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')
    # Find the next sequence which represents the next frame.
   
    if a!=-1 and b!=-1:
        png = bytes[a:b+8]
        # Extract the bytes representing one frame.

        bytes= bytes[b+8:]
        # Disguard the extrated bytes.

        image = cv2.imdecode(np.fromstring(png, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        # Convert bytes back into array image.
        
        image = cv2.bitwise_xor(image, key2)
        image = cv2.bitwise_xor(image, key1)
        # Decrypt in reverse order of encryption.
        
        cv2.imshow('Decrypted Feed',image)
        if cv2.waitKey(1) ==27:
            exit(0)
