import pandas as pd
from typing import Dict, List, Tuple
from datetime import datetime

class FrameIndexer:
    def __init__(self):
        self.frames_df = pd.DataFrame(columns=[
            'timestamp', 'frame_id', 'description', 'objects'
        ])
        
    def add_frame(self, frame_data: Dict):
        """Add frame data to storage"""
        new_row = pd.DataFrame([{
            'timestamp': frame_data['timestamp'],
            'frame_id': frame_data['frame_id'],
            'description': frame_data['description'],
            'objects': frame_data['objects']
        }])
        self.frames_df = pd.concat([self.frames_df, new_row], ignore_index=True)
        
    def query_frames(self, object_type: str = None, time_range: Tuple[datetime, datetime] = None) -> pd.DataFrame:
        """Query frames based on filters"""
        result = self.frames_df.copy()
        
        if object_type:
            result = result[result['description'].str.contains(object_type, case=False)]
            
        if time_range:
            start, end = time_range
            result = result[(result['timestamp'] >= start) & (result['timestamp'] <= end)]
            
        return result
