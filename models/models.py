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

    def add_player(self, player):
        self.players.append(player)

class Player:
    def __init__(self, national_id, first_name, last_name, date_of_birth):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        
class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.matches = []

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0