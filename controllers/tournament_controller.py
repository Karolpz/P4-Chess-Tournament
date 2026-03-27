from models.tournament import Tournament
from models.player import Player
from views.tournament import TournamentMainView, TournamentAddView, TournamentAddPlayerView, TournamentListView, TournamentDetailsView
from views.common_view import CommonView

class TournamentController:
    def __init__(self, database):
        self.database = database
        self.main_view = TournamentMainView()
        self.add_view = TournamentAddView()
        self.add_player_view = TournamentAddPlayerView()
        self.list_view = TournamentListView()
        self.detail_view = TournamentDetailsView()
        self.common_view = CommonView() 

    def run(self):
        while True:
            self.main_view.display_main_menu()
            choice = self.common_view.get_user_choice()

            match choice:
                case "1":
                    self.add_tournament()
                case "2":
                    self.get_tournament_details()
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
        active = self.database.get_active_tournaments()
        if not active:
            self.list_view.display_no_active_tournament()
            self.common_view.display_press_enter()
            return
        self.list_view.display_current_tournament(active)
        choice = self.common_view.get_user_choice()

        if choice == "0":
            return

        tournament = active[int(choice) - 1]
        
        while True:
            national_id = self.add_player_view.ask_player_id()
            if national_id == "0":
                break

            player = self.database.find_player(national_id)

            if player:
                tournament.players.append(player)
                self.add_player_view.display_player_added(player)
            else:
                self.add_player_view.display_player_not_found(national_id)

    def get_tournament_details(self):
        active = self.database.get_active_tournaments()
        if not active:
            self.list_view.display_no_active_tournament()
            self.common_view.display_press_enter()
            return
        
        self.list_view.display_current_tournament(active)
        choice = self.common_view.get_user_choice()

        if choice == "0":
            return

        tournament = active[int(choice) - 1]

        while True:
            self.detail_view.display_tournament_details(tournament)
            actions = self.get_available_actions(tournament)
            mapping = self.detail_view.display_actions(actions)
            choice = self.common_view.get_user_choice()

            if choice == "0":
                break

            action_map = {
                "start": self.generate_next_round,
                "enter_results": self.enter_results,
                "next_round": self.generate_next_round,
                "show_scores": self.show_scoreboard,
                "show_matches": self.show_matches
            }

            selected = mapping.get(choice)
            if selected and selected in action_map:
                action_map[selected](tournament)
            else:
                self.common_view.display_invalid_choice()
            

    def get_available_actions(self, tournament):
        actions = ["show_scores"]
        if tournament.current_round == 0:   
            actions.append("start")
        elif not tournament.is_current_round_complete:
            actions.append("enter_results")
        elif not tournament.is_finished:
            actions.append("next_round")

        if tournament.current_round > 0 and not tournament.is_finished:
            actions.append("show_matches")

        actions.append("back")
  
        return actions

    def generate_next_round(self, tournament):
        round_ =tournament.generate_round()
        self.detail_view.display_round_matches(round_)
        self.common_view.display_confirmation()
        self.common_view.display_press_enter()

    def show_scoreboard(self, tournament):
        scoreboard = tournament.scoreboard
        self.detail_view.display_show_scoreboard(scoreboard)
        self.common_view.display_press_enter()

    def enter_results(self, tournament):
        round_ = tournament.rounds[-1]
        for match in round_.matches:
            if not match.is_finished():
                self.detail_view.display_match(match)
                self.detail_view.display_match_results(match, round_)
                choice = self.common_view.get_user_choice()
                match choice:
                    case "1":
                        match.set_results(winner=match.player1)
                    case "2":
                        match.set_results(winner=match.player2)
                    case "3":
                        match.set_results(winner=None)
                    case "0":
                        break
                    case _:
                        self.common_view.display_invalid_choice()
                self.common_view.display_confirmation()
                self.common_view.display_press_enter()

    def show_matches(self, tournament):
        round_ = tournament.rounds[-1]
        self.detail_view.display_round_matches(round_)
        self.common_view.display_press_enter()
                