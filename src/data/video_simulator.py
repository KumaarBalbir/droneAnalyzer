from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional
import random
import numpy as np

@dataclass
class VideoFrame:
    timestamp: datetime
    frame_id: int
    description: str
    objects: List[Dict]
    image: Optional[np.ndarray] = None  # For real video frames

class VideoSimulator:
    def __init__(self):
        self.objects = ["person", "car", "truck", "bicycle", "motorcycle"]
        self.colors = ["blue", "red", "black", "white", "silver"]
        self.current_frame = 0

    def generate_frame(self) -> VideoFrame:
        """Generate simulated video frame data"""
        self.current_frame += 1
        num_objects = random.randint(0, 3)

        objects = []
        for _ in range(num_objects):
            obj = {
                'type': random.choice(self.objects),
                'color': random.choice(self.colors),
                'confidence': random.uniform(0.7, 0.99),
                'bbox': [
                    random.uniform(0, 1),
                    random.uniform(0, 1),
                    random.uniform(0, 1),
                    random.uniform(0, 1)
                ]
            }
            objects.append(obj)

        description = f"Frame {self.current_frame}: "
        if objects:
            obj_descriptions = [f"{obj['color']} {obj['type']}" for obj in objects]
            description += f"Detected {', '.join(obj_descriptions)}"
        else:
            description += "No objects detected"

        return VideoFrame(
            timestamp=datetime.now(),
            frame_id=self.current_frame,
            description=description,
            objects=objects
        )

    def set_video_source(self, source):
        """
        Configure video source for real video processing
        To be implemented for real video capture
        """
        pass