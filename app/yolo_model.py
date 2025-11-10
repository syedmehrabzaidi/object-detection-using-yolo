# app/yolo_model.py
from ultralytics import YOLO

class YOLOModel:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        """
        Detect objects in a single frame
        Returns annotated frame
        """
        results = self.model(frame)[0]  # YOLOv8 returns a list of results
        annotated_frame = results.plot()  # Draw bounding boxes
        return annotated_frame, results
