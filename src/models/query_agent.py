from typing import List, Dict
from collections import Counter
from datetime import datetime, timedelta

class QueryAgent:
    def __init__(self, frame_indexer, event_logger):
        self.frame_indexer = frame_indexer
        self.event_logger = event_logger

    def answer_question(self, question: str) -> str:
        """Process questions about video content and events"""
        question = question.lower()

        if "object" in question or "detect" in question:
            return self._summarize_objects()
        elif "event" in question or "happen" in question:
            return self._summarize_events()
        elif "alert" in question or "warning" in question:
            return self._summarize_alerts()
        elif "frequent" in question or "time" in question:
            return self._analyze_object_frequency()
        else:
            return "I can answer questions about detected objects, events, and alerts. Please try asking about one of these topics."

    def _summarize_objects(self) -> str:
        """Summarize detected objects"""
        frames = self.frame_indexer.query_frames()
        if len(frames) == 0:
            return "No objects have been detected in the current session."

        objects = []
        for _, row in frames.iterrows():
            for obj in row['objects']:
                objects.append(f"{obj['color']} {obj['type']}")

        object_counts = Counter(objects)
        if not object_counts:
            return "No objects detected yet."

        summary = ", ".join([f"{count} {obj}" for obj, count in object_counts.most_common(5)])
        return f"Recently detected: {summary}"

    def _summarize_events(self) -> str:
        """Summarize recent events"""
        recent_time = datetime.now() - timedelta(minutes=5)
        events = self.event_logger.query_events(time_range=(recent_time, datetime.now()))

        if len(events) == 0:
            return "Monitoring is active but no significant events detected in the last 5 minutes."

        return "Recent events: " + "; ".join(events['description'].tolist()[-3:])

    def _summarize_alerts(self) -> str:
        """Summarize recent alerts"""
        events = self.event_logger.query_events(severity='high')

        if len(events) == 0:
            active_monitoring = "Monitoring is active. " if True else ""
            return f"{active_monitoring}No security alerts at the moment."

        return "Active alerts: " + "; ".join(events['description'].tolist()[-3:])

    def _analyze_object_frequency(self) -> str:
        """Analyze object frequency over time"""
        frames = self.frame_indexer.query_frames()
        if len(frames) == 0:
            return "No object detection data available yet."

        objects_by_time = {}
        for _, row in frames.iterrows():
            hour = row['timestamp'].strftime('%H:%M')
            for obj in row['objects']:
                key = f"{obj['color']} {obj['type']}"
                if hour not in objects_by_time:
                    objects_by_time[hour] = Counter()
                objects_by_time[hour][key] += 1

        if not objects_by_time:
            return "No object frequency data available yet."

        # Find the most frequent objects and their time periods
        most_frequent = Counter()
        for hour, counts in objects_by_time.items():
            for obj, count in counts.items():
                most_frequent[f"{obj} at {hour}"] = count

        top_3 = most_frequent.most_common(3)
        if not top_3:
            return "Still collecting object frequency data."

        summary = "; ".join([f"{count}x {obj}" for obj, count in top_3])
        return f"Most frequent detections: {summary}"