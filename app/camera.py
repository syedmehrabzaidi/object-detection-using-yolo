# app/camera.py
import cv2
from app.yolo_model import YOLOModel

class Camera:
    def __init__(self, camera_id=0):
        self.cap = cv2.VideoCapture(camera_id)
        self.yolo = YOLOModel()

    def generate_frames(self):
        while True:
            success, frame = self.cap.read()
            if not success:
                break
            frame, _ = self.yolo.detect(frame)
            # Encode as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
