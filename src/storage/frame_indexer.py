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
        # Create new row without explicit dtype specification
        new_row = pd.DataFrame([{
            'timestamp': frame_data['timestamp'],
            'frame_id': frame_data['frame_id'],
            'description': frame_data['description'],
            'objects': frame_data['objects']
        }])

        # Use concat with ignore_index
        self.frames_df = pd.concat(
            [self.frames_df, new_row],
            ignore_index=True,
            copy=False
        )

    def query_frames(self, object_type: str = None, time_range: Tuple[datetime, datetime] = None) -> pd.DataFrame:
        """Query frames based on filters"""
        result = self.frames_df.copy()

        if object_type:
            result = result[result['description'].str.contains(
                object_type, case=False)]

        if time_range:
            start, end = time_range
            result = result[(result['timestamp'] >= start)
                            & (result['timestamp'] <= end)]

        return result

    def index_frame(self, frame_data: Dict, detections: List[Dict]):
        # Store frame with metadata for searching
        pass


class EventLogger:
    def log_event(self, event: Dict):
        # Log security events
        pass
