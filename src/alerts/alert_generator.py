from datetime import datetime, time
from typing import Dict, List


class AlertGenerator:
    def __init__(self):
        self.alerts = []

    def check_rules(self, frame_data: Dict, telemetry_data: Dict) -> List[str]:
        """Check security rules and generate alerts"""
        current_alerts = []
        current_time = frame_data['timestamp'].time()

        # Rule 1: Detect people during night hours (22:00 - 06:00)
        night_start = time(22, 0)
        night_end = time(6, 0)

        for obj in frame_data['objects']:
            # Night time person detection
            if (current_time >= night_start or current_time <= night_end) and obj['type'] == 'person':
                alert = f"ALERT: Person detected at {telemetry_data['location']} during night hours"
                current_alerts.append(alert)

            # Multiple vehicle detection
            if obj['type'] in ['car', 'truck'] and telemetry_data['location'] == "Main Gate":
                alert = f"ALERT: Vehicle ({obj['color']} {obj['type']}) at main gate"
                current_alerts.append(alert)

            # Low altitude alert
            if telemetry_data['altitude'] < 15.0:
                alert = f"WARNING: Drone flying too low at {telemetry_data['location']}"
                current_alerts.append(alert)

        self.alerts.extend(current_alerts)
        return current_alerts

    def generate_alert(self, rule_violation: Dict):
        return {
            'severity': rule_violation['severity'],
            'message': f"Alert: {rule_violation['description']}",
            'timestamp': datetime.now()
        }
