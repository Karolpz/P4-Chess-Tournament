class Match:
    """Représente une partie entre deux joueurs dans un tournoi d'échecs."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def to_dict(self):
        """Convertit la partie en un dictionnaire."""
        return {
            "player1": self.player1.national_id,
            "player2": self.player2.national_id,
            "score1": self.score1,
            "score2": self.score2,
        }

    @classmethod
    def from_dict(cls, data, database):
        """Crée une partie à partir d'un dictionnaire et d'une base de données."""
        match = cls(
            player1=database.find_player(data["player1"]),
            player2=database.find_player(data["player2"]),
        )
        match.score1 = data["score1"]
        match.score2 = data["score2"]
        return match

    def __repr__(self):
        """Retourne une représentation de la partie."""
        return f"{self.player1} {self.score1} - {self.score2} {self.player2}"

    def set_results(self, winner=None):
        """Définit les scores de la partie en fonction du gagnant."""
        if winner is None:
            self.score1 = 0.5
            self.score2 = 0.5
        elif winner == self.player1:
            self.score1 = 1
            self.score2 = 0
        elif winner == self.player2:
            self.score1 = 0
            self.score2 = 1

    @property
    def is_finished(self):
        """Retourne True si la partie a un résultat enregistré."""
        return self.score1 != 0 or self.score2 != 0
