from models.tournament import Tournament
from views.tournament import (
    TournamentMainView,
    TournamentAddView,
    TournamentAddPlayerView,
    TournamentListView,
    TournamentDetailsView
    )
from views.common_view import CommonView
from utils.decorators import autosave


class TournamentController:
    """Contrôleur gérant la création et le déroulement des tournois."""

    def __init__(self, database):
        """Initialise le contrôleur avec la base de données et les vues associées."""
        self.database = database
        self.main_view = TournamentMainView()
        self.add_view = TournamentAddView()
        self.add_player_view = TournamentAddPlayerView()
        self.list_view = TournamentListView()
        self.detail_view = TournamentDetailsView()
        self.common_view = CommonView()

    def run(self):
        """Affiche le menu des tournois et gère les choix de l'utilisateur."""
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

    @autosave
    def add_tournament(self):
        """Collecte les données d'un nouveau tournoi, le crée et l'ajoute à la base de données."""
        self.add_view.display_add_tournament()
        data = self.add_view.get_tournament_data()
        tournament = Tournament(**data)
        self.database.tournaments.append(tournament)
        self.common_view.display_confirmation()

    @autosave
    def add_tournament_player(self):
        """Permet d'ajouter des joueurs à un tournoi actif en saisissant leur identifiant national."""
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
        """Affiche les détails d'un tournoi actif et propose les actions disponibles."""
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
        """Retourne la liste des actions disponibles selon l'état actuel du tournoi."""
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

    @autosave
    def generate_next_round(self, tournament):
        """Génère le prochain round du tournoi et affiche les matchs créés."""
        round_ = tournament.generate_round()
        self.detail_view.display_round_matches(round_)
        self.common_view.display_confirmation()
        self.common_view.display_press_enter()

    def show_scoreboard(self, tournament):
        """Affiche le classement actuel du tournoi."""
        scoreboard = tournament.scoreboard
        self.detail_view.display_show_scoreboard(scoreboard)
        self.common_view.display_press_enter()

    @autosave
    def enter_results(self, tournament):
        """Permet de saisir les résultats des matchs non terminés du round en cours."""
        round_ = tournament.rounds[-1]
        for match in round_.matches:
            if not match.is_finished:
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
        round_.mark_end_time()
        self.common_view.display_confirmation()
        self.common_view.display_press_enter()

    def show_matches(self, tournament):
        """Affiche les matchs du round en cours."""
        round_ = tournament.rounds[-1]
        self.detail_view.display_round_matches(round_)
        self.common_view.display_press_enter()
