from typing import List, Dict

def get_security_rules() -> List[Dict]:
    """
    Define standard security rules for the system
    """
    return [
        {
            'id': 'night_activity',
            'description': 'Person detected during night hours',
            'severity': 'high',
            'type': 'temporal',
            'conditions': {
                'object_type': 'person',
                'time_range': ['22:00', '06:00']
            }
        },
        {
            'id': 'vehicle_maingate',
            'description': 'Vehicle at main gate',
            'severity': 'medium',
            'type': 'spatial',
            'conditions': {
                'object_type': ['car', 'truck'],
                'location': 'Main Gate'
            }
        },
        {
            'id': 'low_altitude',
            'description': 'Drone flying too low',
            'severity': 'warning',
            'type': 'operational',
            'conditions': {
                'altitude_min': 15.0
            }
        }
    ]
