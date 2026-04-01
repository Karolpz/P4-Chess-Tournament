from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.matches = []

    def to_dict(self):
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [m.to_dict() for m in self.matches],
        }

    @classmethod
    def from_dict(cls, data):
        round_ = cls(name=data["name"])
        round_.start_time = data["start_time"]
        round_.end_time = data["end_time"]
        round_.matches = [Match.from_dict(m) for m in data["matches"]]
        return round_

    def __repr__(self):
        return f"{self.name}"

    def mark_start_time(self):
        self.start_time = datetime.now()

    def mark_end_time(self):
        self.end_time = datetime.now()

    @property
    def is_complete(self):
        return bool(self.matches) and all(match.is_finished() for match in self.matches)
    