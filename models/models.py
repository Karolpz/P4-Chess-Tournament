from datetime import datetime

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

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round_):
        self.rounds.append(round_)

    def next_round(self):
        self.current_round += 1

    def get_scores(self):
        scores = {player: 0 for player in self.players}
        for round_ in self.rounds:
            for match in round_.matches:
                scores[match.player1] += match.score1
                scores[match.player2] += match.score2
        return scores

    def get_scoreboard(self):
        scoreboard = []
        for round_ in self.rounds:
            for match in round_.matches:
                scoreboard.append(match.get_tuple_result())
        return scoreboard

class Player:
    def __init__(self, national_id, first_name, last_name, date_of_birth):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"{self.last_name} {self.first_name} ({self.national_id})"

    def __lt__(self, other):
        return (self.last_name.lower(), self.first_name.lower()) < \
               (other.last_name.lower(), other.first_name.lower()) # Permet de comparer les joueurs pour ensuite les trier par ordre alphabétique
        
class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.matches = []

    def __repr__(self):
        return f"{self.name}"

    def add_match(self, match):
        self.matches.append(match)

    def mark_start_time(self):
        self.start_time = datetime.now()

    def mark_end_time(self):
        self.end_time = datetime.now()

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def get_tuple_result(self):
        return ([self.player1, self.score1], [self.player2, self.score2])

    def set_result(self, winner=None):
        if winner is None:
            self.score1 = 0.5
            self.score2 = 0.5
        elif winner == self.player1:
            self.score1 = 1
            self.score2 = 0
        elif winner == self.player2:
            self.score1 = 0
            self.score2 = 1