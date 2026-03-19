from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.common_view import CommonView
from models.database import DataBase

class MainController:
    def __init__(self):
        self.view = MainView()
        self.common_view = CommonView()
        self.database = DataBase()  

    def run(self):
        while True:
            self.view.display_main_menu()
            choice = self.view.get_user_choice()

            match choice:
                case "1":
                    PlayerController(self.database).run()
                case "2":
                    TournamentController(self.database).run()
                case "3":
                    print("Rapports - à venir")
                case "0":
                    print("Au revoir !")
                    break
                case _:
                    self.common_view.display_invalid_choice()