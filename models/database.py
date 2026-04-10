from models.player import Player
from models.tournament import Tournament
import json
from pathlib import Path


PLAYERS_FILE = Path("data/players.json")
TOURNAMENTS_FILE = Path("data/tournaments.json")


class DataBase:
    """Classe pour gérer la persistance des données des joueurs et des tournois."""

    def __init__(self):
        self.players = []
        self.tournaments = []
        self.load()

    def save_players(self):
        """Sauvegarde la liste des joueurs dans un fichier JSON."""
        PLAYERS_FILE.parent.mkdir(exist_ok=True)
        with open(PLAYERS_FILE, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.players], f, indent=4, ensure_ascii=False)

    def save_tournaments(self):
        """Sauvegarde la liste des tournois dans un fichier JSON."""
        TOURNAMENTS_FILE.parent.mkdir(exist_ok=True)
        with open(TOURNAMENTS_FILE, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tournaments], f, indent=4, ensure_ascii=False)

    def save(self):
        """Sauvegarde les joueurs et les tournois dans les fichiers JSON."""
        self.save_players()
        self.save_tournaments()

    def load_players(self):
        """Charge la liste des joueurs depuis un fichier JSON."""
        if PLAYERS_FILE.exists():
            with open(PLAYERS_FILE, encoding="utf-8") as f:
                self.players = [Player.from_dict(p) for p in json.load(f)]

    def load_tournaments(self):
        """Charge la liste des tournois depuis un fichier JSON."""
        if TOURNAMENTS_FILE.exists():
            with open(TOURNAMENTS_FILE, encoding="utf-8") as f:
                self.tournaments = [
                    Tournament.from_dict(data, self) for data in json.load(f)
                ]

    def load(self):
        """Charge les joueurs et les tournois depuis les fichiers JSON."""
        self.load_players()
        self.load_tournaments()

    def get_active_tournaments(self):
        """Retourne la liste des tournois actifs."""
        return [tournament for tournament in self.tournaments if not tournament.is_finished]

    def find_player(self, national_id):
        """Recherche un joueur par son identifiant national."""
        for player in self.players:
            if player.national_id == national_id:
                return player
        return None
