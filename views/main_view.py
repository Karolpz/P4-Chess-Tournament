class MainView:
    def display_main_menu(self):
        print("=== MENU PRINCIPAL ===")
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Rapports")
        print("0. Quitter")

    def get_user_choice(self):
        return input("\nVotre choix : ")
