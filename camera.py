import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
        self.key1 = cv2.imread("key1.png")
        self.key2 = cv2.imread("key2.png")
        # Read the secret keys.
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()

       
        image = cv2.bitwise_xor(image, self.key1)
        # Encrypt image once with key1
        image = cv2.bitwise_xor(image, self.key2)
        # Encrypt imgage again with key2
        ret, jpeg = cv2.imencode('.png	', image)
        # OpenCV works on raw format however this cannot be converted to bytes and streamed.
        # PNG format is used as it is a lossless compression.
        # JPEG is lossy conversion, if performed the pixel values will change after encryption.
        # Hence the reconstructed image at the client will not be accurate.
        # Decryption will not lead to the origianl image.
        return jpeg.tobytes()
