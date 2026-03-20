from datetime import datetime

class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.matches = []

    def __repr__(self):
        return f"{self.name}"

    def mark_start_time(self):
        self.start_time = datetime.now()

    def mark_end_time(self):
        self.end_time = datetime.now()

    @property
    def is_current_round_complete(self):
        round_ = self.rounds[-1] if self.rounds else None
        if not round_:
            return False
        return all(match.is_finished() for match in round_.matches)