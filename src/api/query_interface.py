from typing import Dict, List
from datetime import datetime, timedelta
import pandas as pd

class QueryInterface:
    def __init__(self, frame_indexer, event_logger):
        self.frame_indexer = frame_indexer
        self.event_logger = event_logger
        
    def search_frames(self, 
                     object_type: str = None,
                     time_range: tuple = None,
                     location: str = None) -> Dict:
        """
        Search indexed frames based on criteria
        """
        frames = self.frame_indexer.query_frames(object_type, time_range)
        
        if location:
            frames = frames[frames['location'] == location]
            
        return {
            'total_matches': len(frames),
            'frames': frames.to_dict('records')
        }
        
    def get_events(self,
                  event_type: str = None,
                  severity: str = None,
                  last_hours: int = None) -> Dict:
        """
        Get security/operational events
        """
        time_range = None
        if last_hours:
            end_time = datetime.now()
            start_time = end_time - timedelta(hours=last_hours)
            time_range = (start_time, end_time)
            
        events = self.event_logger.query_events(
            event_type=event_type,
            severity=severity,
            time_range=time_range
        )
        
        return {
            'total_events': len(events),
            'events': events.to_dict('records')
        }
