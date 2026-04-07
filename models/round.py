from datetime import datetime
from models.match import Match


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.matches = []

    def to_dict(self):
        return {
            "name": self.name,
            "start_time": self.start_time.strftime(DATETIME_FORMAT) if self.start_time else None,
            "end_time": self.end_time.strftime(DATETIME_FORMAT) if self.end_time else None,
            "matches": [m.to_dict() for m in self.matches],
        }

    @classmethod
    def from_dict(cls, data, database):
        round_ = cls(name=data["name"])
        round_.start_time = (
            datetime.strptime(data["start_time"], DATETIME_FORMAT)
            if data.get("start_time") else None
        )
        round_.end_time = (
            datetime.strptime(data["end_time"], DATETIME_FORMAT)
            if data.get("end_time") else None
        )
        round_.matches = [Match.from_dict(m, database) for m in data.get("matches", [])]
        return round_

    def __repr__(self):
        return f"{self.name}"

    def mark_start_time(self):
        self.start_time = datetime.now()

    def mark_end_time(self):
        self.end_time = datetime.now()

    @property
    def is_complete(self):
        return bool(self.matches) and all(match.is_finished for match in self.matches)
