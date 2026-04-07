class PlayerMainView:
    def display_main_players(self):
        print("=== MENU JOUEURS ===")
        print("1. Liste des joueurs")
        print("2. Ajouter un joueur")
        print("0. Retour")

    def get_user_choice(self):
        return input("\nVotre choix : ")


class PlayerListView:
    def display_players(self, players):
        print("=== LISTE DES JOUEURS ===")
        for player in players:
            print(f"{player.last_name} {player.first_name} - {player.national_id} - {player.date_of_birth}")

    def get_user_choice(self):
        return input("\nAppuyez sur Entrée pour retourner au menu des joueurs")


class PlayerAddView:
    def display_add_player(self):
        print("=== AJOUTER UN JOUEUR ===")

    def get_player_data(self):
        return {
            "last_name": input("Nom : "),
            "first_name": input("Prénom : "),
            "date_of_birth": input("Date de naissance (YYYY-MM-DD) : "),
            "national_id": input("National ID : ")
        }

    def confirm_player(self):
        return input("\nConfirmez-vous l'ajout du joueur ? (1 = Oui / 0 = Annuler) : ")
