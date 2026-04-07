from models.player import Player
from models.tournament import Tournament
import json
from pathlib import Path


PLAYERS_FILE = Path("data/players.json")
TOURNAMENTS_FILE = Path("data/tournaments.json")


class DataBase:
    def __init__(self):
        self.players = []
        self.tournaments = []
        self.load()

    def save_players(self):
        PLAYERS_FILE.parent.mkdir(exist_ok=True)
        with open(PLAYERS_FILE, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.players], f, indent=4, ensure_ascii=False)

    def save_tournaments(self):
        TOURNAMENTS_FILE.parent.mkdir(exist_ok=True)
        with open(TOURNAMENTS_FILE, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tournaments], f, indent=4, ensure_ascii=False)

    def save(self):
        self.save_players()
        self.save_tournaments()

    def load_players(self):
        if PLAYERS_FILE.exists():
            with open(PLAYERS_FILE, encoding="utf-8") as f:
                self.players = [Player.from_dict(p) for p in json.load(f)]

    def load_tournaments(self):
        if TOURNAMENTS_FILE.exists():
            with open(TOURNAMENTS_FILE, encoding="utf-8") as f:
                self.tournaments = [
                    Tournament.from_dict(data, self) for data in json.load(f)
                ]

    def load(self):
        self.load_players()
        self.load_tournaments()

    def get_active_tournaments(self):
        return [tournament for tournament in self.tournaments if not tournament.is_finished]

    def find_player(self, national_id):
        for player in self.players:
            if player.national_id == national_id:
                return player
        return None
