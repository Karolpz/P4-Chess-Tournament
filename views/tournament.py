class TournamentMainView:
    def display_main_menu(self):
        print("=== MENU TOURNOIS ===")
        print("1. Créer un tournoi")
        print("2. Liste des tournois")
        print("3. Ajouter un joueur au tournoi")
        print("0. Retour")

    def get_user_choice(self):
        return input("\nVotre choix : ")

class TournamentAddView:
    def display_add_tournament(self):
        print("=== AJOUTER UN TOURNOI ===")

    def get_tournament_data(self):
        rounds_input = input("Nombre de rondes (par defaut 4) : ").strip()
        return {
            "name": input("Nom du tournoi : "),
            "location": input("Lieu du tournoi : "),
            "start_date": input("Date de commencement (YYYY-MM-DD) : "),
            "end_date": input("Date de fin (YYYY-MM-DD) : "),
            "number_of_rounds": int(rounds_input) if rounds_input else 4,
            "description": input("Description du tournoi (facultatif) : ")   
        }
    
class TournamentAddPlayerView:
    def display_current_tournament(self, tournaments):
        print("=== SELECTIONNER UN TOURNOI ===")
        for number, tournament in enumerate(tournaments, 1):
            if tournament:
                print(f"{number}. {tournament.name}, {tournament.location}")
            else:
                print(f"{number}. Aucun tournoi")
        print ("0. Retour")
        
    def ask_player_id(self):
        return input("National ID du joueur (ou '0' pour terminer) : ").strip()

    def display_player_added(self, player):
        print(f"  -> {player.first_name} {player.last_name} ajouté au tournoi.")

    def display_player_not_found(self, national_id):
        print(f"  Aucun joueur trouvé avec l'ID : {national_id}")