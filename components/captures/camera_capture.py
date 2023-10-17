from components.captures.capture_interface import CaptureInterface
import cv2

class CameraCapture(CaptureInterface):
    def __init__(self, config):
        self.cap = cv2.VideoCapture(config["url"])
        self.info = config

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return ret, frame
    
    def info(self, config):
       return self.info