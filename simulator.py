import datetime
import random
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class TelemetryData:
    timestamp: datetime.datetime
    location: str
    altitude: float
    battery: int
    
@dataclass
class VideoFrame:
    timestamp: datetime.datetime
    frame_id: int
    description: str
    objects: List[Dict]

class DroneSimulator:
    def __init__(self):
        self.locations = ["Main Gate", "Garage", "Backyard", "Perimeter", "Parking"]
        self.objects = ["person", "car", "truck", "bicycle", "motorcycle"]
        self.colors = ["blue", "red", "black", "white", "silver"]
        self.current_frame = 0
        
    def generate_telemetry(self) -> TelemetryData:
        """Generate simulated telemetry data"""
        return TelemetryData(
            timestamp=datetime.datetime.now(),
            location=random.choice(self.locations),
            altitude=random.uniform(10.0, 30.0),
            battery=random.randint(50, 100)
        )
        
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
            timestamp=datetime.datetime.now(),
            frame_id=self.current_frame,
            description=description,
            objects=objects
        )
