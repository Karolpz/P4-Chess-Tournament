from models.player import Player
from views.player_view import PlayerMainView, PlayerListView, PlayerAddView

class PlayerController:
    def __init__(self, players):
        self.players = players  # liste des joueurs partagée
        self.main_view = PlayerMainView()
        self.list_view = PlayerListView()
        self.add_view = PlayerAddView()

    def run(self):
        while True:
            self.main_view.display_main_players()
            choice = self.main_view.get_user_choice()

            match choice:
                case "1":
                    self.show_players()
                case "2":
                    self.add_player()
                case "0":
                    break
                case _:
                    print("Choix invalide")

    def show_players(self):
        self.list_view.display_players(self.players)
        self.list_view.get_user_choice()

    def add_player(self):
        self.add_view.display_add_player()
        last_name, first_name, date_of_birth, national_id = self.add_view.get_player_data()
        player = Player(national_id, first_name, last_name, date_of_birth)
        self.players.append(player)
        print(f"\nJoueur {player} ajouté !")