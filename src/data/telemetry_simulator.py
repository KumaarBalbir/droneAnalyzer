from dataclasses import dataclass
from datetime import datetime
import random

@dataclass
class TelemetryData:
    timestamp: datetime
    location: str
    altitude: float
    battery: int

class TelemetrySimulator:
    def __init__(self):
        self.locations = ["Main Gate", "Garage", "Backyard", "Perimeter", "Parking"]
        
    def generate_telemetry(self) -> TelemetryData:
        """Generate simulated telemetry data"""
        return TelemetryData(
            timestamp=datetime.now(),
            location=random.choice(self.locations),
            altitude=random.uniform(10.0, 30.0),
            battery=random.randint(50, 100)
        )
