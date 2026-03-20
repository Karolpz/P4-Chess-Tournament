class TournamentMainView:
    def display_main_menu(self):
        print("=== MENU TOURNOIS ===")
        print("1. Créer un tournoi")
        print("2. Liste des tournois")
        print("3. Ajouter un joueur au tournoi")
        print("0. Retour")

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
    
    def ask_player_id(self):
        return input("National ID du joueur (ou '0' pour terminer) : ").strip()

    def display_player_added(self, player):
        print(f"  -> {player.first_name} {player.last_name} ajouté au tournoi.")

    def display_player_not_found(self, national_id):
        print(f"  Aucun joueur trouvé avec l'ID : {national_id}")

class TournamentListView:
    def display_current_tournament(self, tournaments):
        print("=== LISTE DES TOURNOIS EN COURS ===")
        for number, tournament in enumerate(tournaments, 1):
            print(f"  {number}. {tournament.name} - {tournament.location}")
        print("0. Retour")
    
    def display_no_active_tournament(self):
        print("Aucun tournoi en cours.")


class TournamentDetailsView:
    def display_tournament_details(self, tournament):
        print("=== DETAIL DU TOURNOI ===")
        print(f"Nom du tournoi : {tournament.name}")
        print(f"Lieu du tournoi : {tournament.location}")
        print(f"Date de commencement : {tournament.start_date}")
        print(f"Date de fin : {tournament.end_date}")
        print(f"Nombre de rondes : {tournament.number_of_rounds}")
        print(f"Ronde en cours : {tournament.current_round}")
        print(f"Description : {tournament.description}")

        print("1. Lancer le prochain round")
        print("2. Afficher les matchs")
        print("3. Afficher le classement")
        print("4. Afficher les joueurs inscrits")
        print("0. Retour")

    def start_next_round(self):
        print("Lancer le prochain round")

    
    