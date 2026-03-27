class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def __repr__(self):
        return f"{self.player1} {self.score1} - {self.score2} {self.player2}"

    def set_results(self, winner=None):
        if winner is None:
            self.score1 = 0.5
            self.score2 = 0.5
        elif winner == self.player1:
            self.score1 = 1
            self.score2 = 0
        elif winner == self.player2:
            self.score1 = 0
            self.score2 = 1

    def is_finished(self):
        return self.score1 != 0 or self.score2 != 0