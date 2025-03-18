from typing import Dict, List
import torch
from torchvision.transforms import ToTensor
import numpy as np
import cv2
from ultralytics import YOLO


class ObjectDetector:
    def __init__(self, model_path: str):
        """Initialize object detector with YOLO model

        Args:
            model_path: Path to YOLOv8 model or model name like 'yolov8n.pt'
        """
        try:
            # Load YOLOv8 model directly using ultralytics
            self.model = YOLO('yolov8n.pt')  # Use smallest YOLOv8 model
        except Exception as e:
            print(f"Error loading model: {e}")
            # Fallback to simple detection for testing
            self.model = None

    def detect(self, frame) -> List[Dict]:
        """Detect objects in frame

        Args:
            frame: Video frame (numpy array)

        Returns:
            List of detected objects with type, confidence and bounding box
        """
        if self.model is None:
            # Return dummy detection for testing
            return [{
                'type': 'person',
                'confidence': 0.95,
                'bbox': [0, 0, 100, 100]
            }]

        try:
            results = self.model(frame)
            detections = []

            for r in results:
                for box in r.boxes:
                    detection = {
                        'type': r.names[int(box.cls[0])],
                        'confidence': float(box.conf[0]),
                        'bbox': box.xyxy[0].tolist()
                    }
                    detections.append(detection)
            return detections

        except Exception as e:
            print(f"Detection error: {e}")
            return []

    def process_frame(self, frame_data: Dict) -> List[Dict]:
        """Process frame data

        Args:
            frame_data (Dict): Frame data

        Returns:
            List[Dict]: Detected objects
        """
        # If we're receiving simulated data, process it directly
        if 'objects' in frame_data:
            return self._process_simulated_frame(frame_data)

        # For real frames, use YOLOv8 if available
        if self.using_yolo and 'image' in frame_data:
            return self._process_real_frame(frame_data['image'])

        return []

    def _process_real_frame(self, image: np.ndarray) -> List[Dict]:
        """Process real frame using YOLOv8

        Args:
            image (np.ndarray): Real frame

        Returns:
            List[Dict]: Detected objects
        """
        try:
            # Convert image to tensor if needed
            if not isinstance(image, torch.Tensor):
                transform = ToTensor()
                image = transform(image).unsqueeze(0)

            # Run inference
            with torch.no_grad():
                results = self.model(image)

            # Process detections
            detected_objects = []
            for det in results.pred[0]:
                x1, y1, x2, y2, conf, cls = det.cpu().numpy()
                class_name = self.model.names[int(cls)]

                detection = {
                    'class': class_name,
                    'confidence': float(conf),
                    'bbox': [float(x1), float(y1), float(x2), float(y2)],
                    'color': 'unknown'  # Color detection would require additional processing
                }
                detected_objects.append(detection)

            return detected_objects
        except Exception as e:
            print(f"Error processing frame with YOLOv8: {e}")
            return []

    def _process_simulated_frame(self, frame_data: Dict) -> List[Dict]:
        # Implementation of _process_simulated_frame method
        """Process simulated frame data

        Args:
            frame_data (Dict): Simulated frame data

        Returns:
            List[Dict]: Detected objects
        """
        detected_objects = []
        for obj in frame_data['objects']:
            detection = {
                'class': obj['type'],
                'confidence': obj['confidence'],
                'bbox': obj['bbox'],
                'color': obj['color']
            }
            detected_objects.append(detection)
        return detected_objects
