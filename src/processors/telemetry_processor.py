from typing import Dict
from datetime import datetime
from src.data.telemetry_simulator import TelemetryData


class TelemetryProcessor:
    def __init__(self):
        pass

    def process_telemetry(self, telemetry_data: TelemetryData) -> Dict:
        """
        Process drone telemetry data.
        Add derived metrics and analysis.
        """
        processed_data = {
            'timestamp': telemetry_data.timestamp,
            'location': telemetry_data.location,
            'altitude': telemetry_data.altitude,
            'battery': telemetry_data.battery,
            'is_low_altitude': telemetry_data.altitude < 15.0,
            'battery_status': 'low' if telemetry_data.battery < 30 else 'normal'
        }

        return processed_data
