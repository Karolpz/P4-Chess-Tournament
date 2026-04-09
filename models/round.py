from datetime import datetime
from models.match import Match


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class Round:
    """Représente un round dans un tournoi d'échecs."""

    def __init__(self, name):
        """Initialise un round avec son nom et des valeurs par défaut."""
        self.name = name
        self.start_time = None
        self.end_time = None
        self.matches = []

    def to_dict(self):
        """Convertit le round en un dictionnaire."""
        return {
            "name": self.name,
            "start_time": self.start_time.strftime(DATETIME_FORMAT) if self.start_time else None,
            "end_time": self.end_time.strftime(DATETIME_FORMAT) if self.end_time else None,
            "matches": [m.to_dict() for m in self.matches],
        }

    @classmethod
    def from_dict(cls, data, database):
        """Crée un round à partir d'un dictionnaire et d'une base de données."""
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
        """Retourne une représentation du round."""
        return f"{self.name}"

    def mark_start_time(self):
        """Enregistre l'heure de début du round."""
        self.start_time = datetime.now()

    def mark_end_time(self):
        """Enregistre l'heure de fin du round."""
        self.end_time = datetime.now()

    @property
    def is_complete(self):
        """Retourne True si tous les matchs du round ont un résultat enregistré."""
        return bool(self.matches) and all(match.is_finished for match in self.matches)