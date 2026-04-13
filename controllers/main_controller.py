from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from views.common_view import CommonView
from models.database import DataBase


class MainController:
    """Contrôleur principal gérant la navigation entre les modules de l'application."""

    def __init__(self):
        """Initialise le contrôleur principal avec la base de données et les vues associées."""
        self.view = MainView()
        self.common_view = CommonView()
        self.database = DataBase()

    def run(self):
        """Affiche le menu principal et redirige vers le contrôleur correspondant au choix."""
        while True:
            self.view.display_main_menu()
            choice = self.common_view.get_user_choice()

            match choice:
                case "1":
                    PlayerController(self.database).run()
                case "2":
                    TournamentController(self.database).run()
                case "3":
                    ReportController(self.database).run()
                case "0":
                    self.common_view.display_goodbye()
                    break
                case _:
                    self.common_view.display_invalid_choice()
