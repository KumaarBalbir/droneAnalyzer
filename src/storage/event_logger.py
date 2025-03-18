from typing import Dict, List
import pandas as pd
from datetime import datetime

class EventLogger:
    def __init__(self):
        self.events_df = pd.DataFrame(columns=[
            'timestamp', 'event_type', 'description', 'severity',
            'location', 'objects_involved'
        ])
        
    def log_event(self, event: Dict):
        """Log a security or operational event"""
        new_row = pd.DataFrame([{
            'timestamp': event['timestamp'],
            'event_type': event['type'],
            'description': event['description'],
            'severity': event.get('severity', 'info'),
            'location': event.get('location', 'unknown'),
            'objects_involved': str(event.get('objects', []))
        }])
        self.events_df = pd.concat([self.events_df, new_row], ignore_index=True)
        
    def query_events(self, 
                    event_type: str = None,
                    severity: str = None,
                    time_range: tuple = None) -> pd.DataFrame:
        """Query events based on filters"""
        result = self.events_df.copy()
        
        if event_type:
            result = result[result['event_type'] == event_type]
            
        if severity:
            result = result[result['severity'] == severity]
            
        if time_range:
            start, end = time_range
            result = result[(result['timestamp'] >= start) & 
                          (result['timestamp'] <= end)]
            
        return result
