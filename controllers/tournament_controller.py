from models.tournament import Tournament
from models.player import Player
from views.tournament import TournamentMainView, TournamentAddView, TournamentAddPlayerView
from views.common_view import CommonView

class TournamentController:
    def __init__(self, database):
        self.database = database
        self.main_view = TournamentMainView()
        self.add_view = TournamentAddView()
        self.add_player_view = TournamentAddPlayerView()
        self.common_view = CommonView()

    def run(self):
        while True:
            self.main_view.display_main_menu()
            choice = self.main_view.get_user_choice()

            match choice:
                case "1":
                    self.add_tournament()
                case "2":
                    print("Liste des tournois - à venir")
                case "3":
                    self.add_tournament_player()
                case "0":
                    break
                case _:
                    self.common_view.display_invalid_choice()

    def add_tournament(self):
        self.add_view.display_add_tournament()
        data = self.add_view.get_tournament_data()
        tournament = Tournament(**data)
        self.database.tournaments.append(tournament)
        self.common_view.display_confirmation()

    def add_tournament_player(self):
        active = self.database.tournament.get_active_tournaments()
        self.add_player_view.display_current_tournament(active)
        choice = self.common_view.get_user_choice()

        if choice == "0":
            return

        tournament = active[int(choice) - 1]
        
        while True:
            national_id = self.add_player_view.ask_player_id()
            if national_id == "0":
                break

            player = None
            for p in self.database.players:
                if p.national_id == national_id:
                    player = p
                    break

            if player:
                tournament.players.append(player)
                self.add_player_view.display_player_added(player)
            else:
                self.add_player_view.display_player_not_found(national_id)
