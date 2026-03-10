from datetime import datetime
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

    def __repr__(self):
        return f"{self.player1} {self.score1} - {self.score2} {self.player2}"

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


# Création d'un tournois et ajout des joueurs

tournoi = Tournament("Tournoi d'échecs", "Paris", "2024-07-01", "2024-07-10")
print("Tournoi créé :", tournoi)

joueur1 = Player("AB12345", "Alice", "Dupont", "1990-01-01")
joueur2 = Player("CD67890", "Bob", "Martin", "1985-05-15")
joueur3 = Player("EF54321", "Charlie", "Durand", "1992-03-20")
joueur4 = Player("GH09876", "Diana", "Lemoine", "1988-11-30")

tournoi.players.append(joueur1)
tournoi.players.append(joueur2)
tournoi.players.append(joueur3)
tournoi.players.append(joueur4)

print("Joueurs inscrits :", tournoi.players)

round1 =tournoi.generate_round()

round1.mark_start_time()

for match in round1.matches:
    match.set_result()

print("Matches terminés :", round1.matches)

round1.mark_end_time()
print("Round terminé :", round1)

# Affichage des résultats

print("\nResultats Round 1 :")
for match in round1.matches:
    print(f"  {match.player1} {match.score1} - {match.score2} {match.player2}")

print("\nScores :")
for player, score in tournoi.scores.items():
    print(f"  {player} : {score} pts")

print("\nJoueurs par ordre alphabetique :")
for player in sorted(tournoi.players):
    print(f"  {player}")

#Lancement du deuxieme round

# tournoi.next_round()
# round2 = Round(f"Round {tournoi.current_round}")
# round2.mark_start_time()

# round2.matches[0].set_result()  # match nul
# round2.matches[1].set_result(winner=joueur4)
# round2.mark_end_time()
# tournoi.rounds.append(round2)

# print("\nResultats Round 2 :")
# for match in round2.matches:
#     print(f"  {match.player1} {match.score1} - {match.score2} {match.player2}")

# print("\nScores apres Round 2 :")
# for player, score in tournoi.scores.items():
#     print(f"  {player} : {score} pts")

# print ('\n Fin du tournoi, classement :')
# for result in tournoi.scoreboard:
#     print(f"  {result}")
