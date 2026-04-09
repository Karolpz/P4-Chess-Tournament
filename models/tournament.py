from models.round import Round
from models.match import Match
import random


class Tournament:
    """Représente un tournoi d'échecs avec ses joueurs, rounds et résultats."""

    def __init__(self, name, location, start_date, end_date,
                 number_of_rounds=4, description=""):
        """Initialise un tournoi avec ses informations de base."""
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = int(number_of_rounds)
        self.current_round = 0
        self.rounds = []
        self.players = []
        self.description = description

    def to_dict(self):
        """Convertit le tournoi en un dictionnaire sérialisable."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "description": self.description,
            "players": [p.national_id for p in self.players],
            "rounds": [r.to_dict() for r in self.rounds],
        }

    @classmethod
    def from_dict(cls, data, database):
        """Crée un tournoi à partir d'un dictionnaire et d'une base de données."""
        tournament = cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            number_of_rounds=data["number_of_rounds"],
            description=data["description"],
        )
        tournament.current_round = data.get("current_round", 0)
        tournament.players = [
            database.find_player(national_id) for national_id in data["players"]
        ]
        tournament.rounds = [Round.from_dict(r, database) for r in data["rounds"]]
        return tournament

    def __repr__(self):
        """Retourne une représentation du tournoi."""
        return f"{self.name} / {self.location} / ({self.start_date} - {self.end_date})"

    def next_round(self):
        """Incrémente le compteur de rounds du tournoi."""
        self.current_round += 1

    @property
    def scores(self):
        """Retourne un dictionnaire associant chaque joueur à son score total."""
        scores = {player: 0 for player in self.players}
        for round_ in self.rounds:
            for match in round_.matches:
                scores[match.player1] += match.score1
                scores[match.player2] += match.score2
        return scores

    @property
    def scoreboard(self):
        """Retourne la liste des joueurs triés par score décroissant."""
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)

    def has_played(self, player1, player2):
        """Retourne True si les deux joueurs se sont déjà affrontés dans ce tournoi."""
        for round_ in self.rounds:
            for match in round_.matches:
                if {match.player1, match.player2} == {player1, player2}:
                    return True
        return False

    def generate_pairs(self):
        """Génère les paires de joueurs pour le prochain round en évitant les rematches."""
        if not self.rounds:
            players = random.sample(self.players, len(self.players))
        else:
            sorted_scores = self.scoreboard
            players = [player for player, _ in sorted_scores]

        pairs = []
        remaining = players.copy()

        while len(remaining) >= 2:
            player1 = remaining.pop(0)
            paired = False
            for i, player2 in enumerate(remaining):
                if not self.has_played(player1, player2):
                    pairs.append((player1, player2))
                    remaining.pop(i)
                    paired = True
                    break
            if not paired:
                pairs.append((player1, remaining.pop(0)))

        return pairs

    def generate_round(self):
        """Crée un nouveau round avec les matchs générés et l'ajoute au tournoi."""
        round_ = Round(f"Round {self.current_round + 1}")
        round_.mark_start_time()
        for player1, player2 in self.generate_pairs():
            round_.matches.append(Match(player1, player2))
        self.rounds.append(round_)
        self.next_round()
        return round_

    @property
    def is_current_round_complete(self):
        """Retourne True si le round en cours est terminé."""
        if not self.rounds:
            return False
        return self.rounds[-1].is_complete

    @property
    def is_finished(self):
        """Retourne True si tous les rounds ont été joués et complétés."""
        if self.current_round < self.number_of_rounds:
            return False
        return self.is_current_round_complete
