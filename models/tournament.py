from models.round import Round
from models.match import Match
import random

class Tournament:
    def __init__(self, name, location, start_date, end_date,
                 number_of_rounds=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.rounds = []
        self.players = []
        self.description = description

    def __repr__(self):
        return f"{self.name} / {self.location} / ({self.start_date} - {self.end_date})"

    def next_round(self):
        self.current_round += 1

    @property
    def scores(self):
        scores = {player: 0 for player in self.players}
        for round_ in self.rounds:
            for match in round_.matches:
                scores[match.player1] += match.score1
                scores[match.player2] += match.score2
        return scores

    @property
    def scoreboard(self):
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
    
    def has_played(self, player1, player2):
        for round_ in self.rounds:
            for match in round_.matches:
                if {match.player1, match.player2} == {player1, player2}:
                    return True
        return False

    def generate_pairs(self):
        # Premier round : ordre aléatoire
        # Rounds suivants : triés par score
        if not self.rounds:
            players = random.sample(self.players, len(self.players))
        else:
            sorted_scores = self.scoreboard  # déjà trié par score desc
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
                # Tous les adversaires possibles ont déjà été affrontés
                # On prend le premier disponible par défaut
                pairs.append((player1, remaining.pop(0)))

        return pairs

    def generate_round(self):
        round_ = Round(f"Round {self.current_round + 1}")
        for player1, player2 in self.generate_pairs():
            round_.matches.append(Match(player1, player2))
        self.rounds.append(round_)
        self.next_round()
        return round_