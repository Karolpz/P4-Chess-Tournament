from models.player import Player
from models.tournament import Tournament

class DataBase:
    def __init__(self):
        self.players = [
            Player("AB12345", "Alice", "Dupont", "1990-01-01"),
            Player("CD67890", "Bob", "Martin", "1985-05-15"),
            Player("EF54321", "Charlie", "Durand", "1992-03-20"),
            Player("GH09876", "Diana", "Lemoine", "1988-11-30")
        ]

        t1 = Tournament("Tournoi d'echecs", "Paris", "2024-07-01", "2024-07-10", 4)
        t1.current_round = 4
        t2 = Tournament("Tournoi de foot", "Marseille", "2024-06-15", "2024-06-25", 4)
        self.tournaments = [t1, t2]

    def get_active_tournaments(self):
        return [tournament for tournament in self.tournaments if not tournament.is_finished]
    
    def get_sorted_players(self):
        return sorted(self.players)