class CommonView:
    def get_user_choice(self):
        return input("\nVotre choix : ")
    def display_confirmation(self):
        print("\nOpération confirmée.")
    def display_invalid_choice(self):
        print("Choix invalide")
    def display_cancelled(self):
        print("\nOpération annulée.")
    def display_press_enter(self):
        input("\nAppuyez sur Entrée pour continuer...")