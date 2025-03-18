from typing import Dict, List
from datetime import datetime, time
from dataclasses import dataclass


@dataclass
class SecurityEvent:
    timestamp: float
    location: str
    event_type: str
    details: dict


class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: Dict):
        """Add a security rule to the engine"""
        self.rules.append(rule)

    def evaluate_frame(self, frame_data: Dict, telemetry_data: Dict) -> List[Dict]:
        """
        Evaluate all rules against current frame and telemetry data
        """
        rule_results = []
        for rule in self.rules:
            if self._check_rule_conditions(rule, frame_data, telemetry_data):
                rule_results.append({
                    'rule_id': rule['id'],
                    'trigger_time': datetime.now(),
                    'severity': rule['severity'],
                    'description': rule['description']
                })

        return rule_results

    def _check_rule_conditions(self, rule: Dict, frame_data: Dict, telemetry_data: Dict) -> bool:
        """
        Check if rule conditions are met
        To be implemented based on specific rule types
        """
        return False  # Placeholder

    def evaluate(self, event: SecurityEvent) -> List[str]:
        alerts = []
        for rule in self.rules:
            if rule.matches(event):
                alerts.append(rule.generate_alert(event))
        return alerts
