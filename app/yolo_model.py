# app/yolo_model.py
from ultralytics import YOLO
import os
import numpy as np

class YOLOModel:
    def __init__(self, model_path="yolov8n.pt"):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        try:
            self.model = YOLO(model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load YOLO model: {str(e)}")
        
        # Configuration
        self.conf_threshold = 0.25  # Confidence threshold
        self.iou_threshold = 0.45   # NMS IOU threshold

    def detect(self, frame):
        """
        Detect objects in a single frame
        Args:
            frame: numpy array of shape (H, W, C)
        Returns:
            tuple: (annotated_frame, results)
        """
        if frame is None or not isinstance(frame, np.ndarray):
            raise ValueError("Invalid frame input")

        try:
            # Run inference with configured thresholds
            results = self.model(frame, conf=self.conf_threshold, iou=self.iou_threshold)[0]
            
            # Draw bounding boxes
            annotated_frame = results.plot()
            
            return annotated_frame, results
        except Exception as e:
            print(f"Error during detection: {str(e)}")
            return frame, None  # Return original frame on error

    def update_thresholds(self, conf_threshold=None, iou_threshold=None):
        """Update detection thresholds"""
        if conf_threshold is not None:
            self.conf_threshold = float(conf_threshold)
        if iou_threshold is not None:
            self.iou_threshold = float(iou_threshold)
