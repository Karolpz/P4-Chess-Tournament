from views.report_view import ReportView, ReportMainView
from views.common_view import CommonView


class ReportController:
    """Contrôleur gérant l'affichage des rapports sur les joueurs et les tournois."""

    def __init__(self, database):
        """Initialise le contrôleur avec la base de données et les vues associées."""
        self.database = database
        self.main_view = ReportMainView()
        self.view = ReportView()
        self.common_view = CommonView()

    def run(self):
        """Affiche le menu des rapports et gère les choix de l'utilisateur."""
        while True:
            self.main_view.display_main_menu()
            choice = self.common_view.get_user_choice()

            match choice:
                case "1":
                    self.view.display_all_players(sorted(self.database.players))
                    self.common_view.display_press_enter()
                case "2":
                    self.report_tournament_detail()
                case "0":
                    break
                case _:
                    self.common_view.display_invalid_choice()

    def pick_tournament(self):
        """Affiche la liste des tournois et retourne celui sélectionné par l'utilisateur, ou None."""
        if not self.database.tournaments:
            self.common_view.display_press_enter()
            return None
        self.view.display_all_tournaments(self.database.tournaments)
        choice = self.common_view.get_user_choice()
        if choice == "0":
            return None
        if not choice.isdigit() or int(choice) > len(self.database.tournaments):
            self.common_view.display_invalid_choice()
            return None
        return self.database.tournaments[int(choice) - 1]

    def report_tournament_detail(self):
        """Permet de choisir un tournoi et d'afficher son détail complet."""
        tournament = self.pick_tournament()
        if tournament:
            self.view.display_tournament_detail(tournament)
            self.common_view.display_press_enter()
