class PlayerMainView:
    """Vue du menu principal de la gestion des joueurs."""

    def display_main_players(self):
        """Affiche le menu de gestion des joueurs."""
        print("=== MENU JOUEURS ===")
        print("1. Liste des joueurs")
        print("2. Ajouter un joueur")
        print("0. Retour")

    def get_user_choice(self):
        """Récupère le choix saisi par l'utilisateur."""
        return input("\nVotre choix : ")


class PlayerListView:
    """Vue pour l'affichage de la liste des joueurs."""

    def display_players(self, players):
        """Affiche la liste des joueurs avec leurs informations."""
        print("=== LISTE DES JOUEURS ===")
        for player in players:
            print(f"{player.last_name} {player.first_name} - {player.national_id} - {player.date_of_birth}")


class PlayerAddView:
    """Vue pour l'ajout d'un nouveau joueur."""

    def display_add_player(self):
        """Affiche le titre de la section d'ajout de joueur."""
        print("=== AJOUTER UN JOUEUR ===")

    def get_player_data(self):
        """Collecte et retourne les données saisies pour le nouveau joueur."""
        return {
            "last_name": input("Nom : "),
            "first_name": input("Prénom : "),
            "date_of_birth": input("Date de naissance (YYYY-MM-DD) : "),
            "national_id": input("National ID : ")
        }

    def confirm_player(self):
        """Demande une confirmation avant d'ajouter le joueur et retourne le choix."""
        return input("\nConfirmez-vous l'ajout du joueur ? (1 = Oui / 0 = Annuler) : ")
