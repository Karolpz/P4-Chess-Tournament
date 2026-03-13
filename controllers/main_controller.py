from views.main_view import MainView
from controllers.player_controller import PlayerController
from views.common_view import CommonView

class MainController:
    def __init__(self):
        self.view = MainView()
        self.common_view = CommonView()
        self.players = []

    def run(self):
        while True:
            self.view.display_main_menu()
            choice = self.view.get_user_choice()

            match choice:
                case "1":
                    PlayerController(self.players).run()
                case "2":
                    print("Tournois - à venir")
                case "3":
                    print("Rapports - à venir")
                case "0":
                    print("Au revoir !")
                    break
                case _:
                    self.common_view.display_invalid_choice()