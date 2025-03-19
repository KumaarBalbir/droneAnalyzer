import cv2
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from typing import Dict, List
import numpy as np
from datetime import datetime


class VideoProcessor:
    def __init__(self, video_path: str = None, stream_url: str = None):
        self.video_path = video_path
        self.stream_url = stream_url
        self.cap = None
        self.fps = 0
        self.frame_interval = 1  # Process 1 frame per second

        # Initialize BLIP model
        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base")

    def start(self):
        """Initialize video capture"""
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
        elif self.stream_url:
            self.cap = cv2.VideoCapture(self.stream_url)

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_interval = int(self.fps)  # Process 1 frame per second

    def process_frame(self, frame: np.ndarray) -> Dict:
        """Process a single frame using BLIP"""
        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process image with BLIP
        inputs = self.processor(frame_rgb, return_tensors="pt")
        out = self.model.generate(**inputs, max_length=50)
        caption = self.processor.decode(out[0], skip_special_tokens=True)

        return {
            'timestamp': datetime.now(),
            'frame_id': int(self.cap.get(cv2.CAP_PROP_POS_FRAMES)),
            'description': caption,
            'objects': self._extract_objects(caption)
        }

    def _extract_objects(self, caption: str) -> List[Dict]:
        """Extract objects from BLIP caption"""
        # Simple object extraction - can be enhanced with NLP
        objects = []
        words = caption.lower().split()

        # Common object categories
        categories = ['person', 'car', 'truck', 'bicycle', 'motorcycle', 'bus']

        for word in words:
            if word in categories:
                objects.append({
                    'type': word,
                    'confidence': 0.95,  # BLIP confidence
                    # Placeholder - can be enhanced with object detection
                    'bbox': [0, 0, 0, 0]
                })

        return objects

    def process_video(self):
        """Process video frames at fixed intervals"""
        if not self.cap:
            self.start()

        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            # Process every nth frame based on interval
            if int(self.cap.get(cv2.CAP_PROP_POS_FRAMES)) % self.frame_interval == 0:
                result = self.process_frame(frame)
                yield result

        self.cap.release()
