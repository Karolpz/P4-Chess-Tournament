class CommonView:
    """Vue commune pour les différentes interfaces utilisateur."""

    def get_user_choice(self):
        """Affiche les options et récupère le choix de l'utilisateur."""
        return input("\nVotre choix : ")

    def display_confirmation(self):
        """Affiche un message de confirmation après une opération réussie."""
        print("\nOpération confirmée.")

    def display_invalid_choice(self):
        """Affiche un message d'erreur pour un choix invalide."""
        print("Choix invalide")

    def display_cancelled(self):
        """Affiche un message lorsque une opération est annulée."""
        print("\nOpération annulée.")

    def display_press_enter(self):
        """Affiche un message indiquant que l'utilisateur doit appuyer sur Entrée."""
        input("\nAppuyez sur Entrée pour continuer...")

    def display_invalid_data(self, error):
        """Affiche un message d'erreur pour des données invalides."""
        print(f"Données invalides : {error}")

    def display_goodbye(self):
        """Affiche un message d'au revoir."""
        print("Au revoir !")
