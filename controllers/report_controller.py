from views.report_view import ReportView, ReportMainView
from views.common_view import CommonView

class ReportController:
    def __init__(self, database):
        self.database = database
        self.main_view = ReportMainView()
        self.view = ReportView()
        self.common_view = CommonView()

    def run(self):
        while True:
            self.main_view.display_main_menu()
            choice = self.common_view.get_user_choice()

            match choice:
                case "1":
                    self.view.display_all_players(sorted(self.database.players))
                    self.common_view.display_press_enter()
                case "2":
                    self.view.display_all_tournaments(self.database.tournaments)
                    self.common_view.display_press_enter()
                case "3":
                    self.report_tournament_detail()
                case "0":
                    break
                case _:
                    self.common_view.display_invalid_choice()

    def pick_tournament(self):
        if not self.database.tournaments:
            self.view.display_all_tournaments([])
            self.common_view.display_press_enter()
            return None
        self.view.display_all_tournaments(self.database.tournaments)
        choice = self.common_view.get_user_choice()
        if choice == "0":
            return None
        return self.database.tournaments[int(choice) - 1]

    def report_tournament_detail(self):
        tournament = self.pick_tournament()
        if tournament:
            self.view.display_tournament_detail(tournament)
            self.common_view.display_press_enter()