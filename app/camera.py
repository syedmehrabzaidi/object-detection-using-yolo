# app/camera.py
import cv2
from app.yolo_model import YOLOModel

class Camera:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.cap = None
        self.yolo = YOLOModel()
        self._initialize_camera()

    def _initialize_camera(self):
        if self.cap is not None:
            self.cap.release()
        self.cap = cv2.VideoCapture(self.camera_id)
        if not self.cap.isOpened():
            raise RuntimeError(f"Failed to open camera {self.camera_id}")

    def generate_frames(self):
        if not self.cap.isOpened():
            self._initialize_camera()
        
        try:
            while True:
                success, frame = self.cap.read()
                if not success:
                    self._initialize_camera()
                    continue
                
                frame, _ = self.yolo.detect(frame)
                # Encode as JPEG
                ret, buffer = cv2.imencode('.jpg', frame)
                if not ret:
                    continue
                    
                frame_bytes = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        except Exception as e:
            print(f"Error in generate_frames: {str(e)}")
            if self.cap is not None:
                self.cap.release()
            raise

    def __del__(self):
        if self.cap is not None:
            self.cap.release()
