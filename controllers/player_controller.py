from models.player import Player
from views.player_view import PlayerMainView, PlayerListView, PlayerAddView
from views.common_view import CommonView
from utils.decorators import autosave

class PlayerController:
    def __init__(self, database):
        self.database = database
        self.main_view = PlayerMainView()
        self.list_view = PlayerListView()
        self.add_view = PlayerAddView()
        self.common_view = CommonView()

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
                    self.common_view.display_invalid_choice()

    def show_players(self):
        players = self.database.get_sorted_players()
        self.list_view.display_players(players)
        self.list_view.get_user_choice()

    @autosave
    def add_player(self):
        self.add_view.display_add_player()
        data = self.add_view.get_player_data()
        try:
            player = Player(**data)
        except ValueError as e:
            self.common_view.display_invalid_data(e)
            return
        confirm = self.add_view.confirm_player()
        
        match confirm:
            case "1":
                self.database.players.append(player)
                self.common_view.display_confirmation()
            case "0":
                return
            case _:
                self.common_view.display_invalid_choice()

        