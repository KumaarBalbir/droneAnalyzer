from typing import List, Dict
from collections import Counter
from datetime import datetime
from .captioning_model import CaptioningModel

class VideoSummarizer:
    def __init__(self):
        self.object_history = []
        self.last_summary = ""
        self.last_summary_time = None
        self.captioning_model = CaptioningModel()

    def add_frame(self, frame_data: Dict):
        """Add frame data to history"""
        self.object_history.extend(frame_data['objects'])

        # Generate caption if image is available
        if 'image' in frame_data and frame_data['image'] is not None:
            caption = self.captioning_model.generate_caption(
                image=frame_data['image'],
                objects=frame_data['objects']
            )
            if caption:
                self.last_summary = caption
                self.last_summary_time = datetime.now()

    def generate_summary(self) -> str:
        """Generate a one-sentence summary of recent activity"""
        if not self.object_history:
            return "No activity detected in the current session."

        # Use last caption if available and recent
        if self.last_summary and self.last_summary_time:
            time_diff = (datetime.now() - self.last_summary_time).total_seconds()
            if time_diff < 10:  # Use caption if less than 10 seconds old
                return self.last_summary

        # Fallback to object-based summary
        object_counts = Counter(obj['type'] for obj in self.object_history)
        color_counts = Counter(obj['color'] for obj in self.object_history)

        # Get most common objects and colors
        common_objects = object_counts.most_common(3)
        main_color = color_counts.most_common(1)[0][0] if color_counts else "unknown"

        # Generate summary
        object_list = ", ".join([f"{count} {obj}" + ("s" if count > 1 else "") 
                               for obj, count in common_objects])

        summary = f"Detected {object_list} with {main_color} being the most common color"

        return summary

    def clear_history(self):
        """Clear object history"""
        self.object_history = []