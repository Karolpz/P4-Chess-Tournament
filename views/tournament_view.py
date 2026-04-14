class TournamentMainView:
    """Vue du menu principal de la gestion des tournois."""

    def display_main_menu(self):
        """Affiche le menu de gestion des tournois."""
        print("=== MENU TOURNOIS ===")
        print("1. Créer un tournoi")
        print("2. Liste des tournois en cours")
        print("3. Ajouter un joueur au tournoi")
        print("0. Retour")


class TournamentAddView:
    """Vue pour la création d'un nouveau tournoi."""

    def display_add_tournament(self):
        """Affiche le titre de la section de création de tournoi."""
        print("=== AJOUTER UN TOURNOI ===")

    def get_tournament_data(self):
        """Collecte et retourne les données saisies pour le nouveau tournoi."""
        rounds_input = input("Nombre de rondes (par defaut 4) : ").strip()
        return {
            "name": input("Nom du tournoi : "),
            "location": input("Lieu du tournoi : "),
            "start_date": input("Date de commencement (YYYY-MM-DD) : "),
            "end_date": input("Date de fin (YYYY-MM-DD) : "),
            "number_of_rounds": int(rounds_input) if rounds_input else 4,
            "description": input("Description du tournoi (facultatif) : ")
        }

    def confirm_tournament(self):
        """Confirme la création du tournoi."""
        return input("\nConfirmez-vous l'ajout du tournoi ? (1 = Oui / 0 = Annuler) : ")


class TournamentAddPlayerView:
    """Vue pour l'ajout de joueurs à un tournoi."""

    def ask_player_id(self):
        """Demande et retourne l'identifiant national d'un joueur à ajouter."""
        return input("National ID du joueur (ou '0' pour terminer) : ").strip()

    def display_player_added(self, player):
        """Affiche un message confirmant l'ajout du joueur au tournoi."""
        print(f"  -> {player.first_name} {player.last_name} ajouté au tournoi.")

    def display_player_not_found(self, national_id):
        """Affiche un message indiquant qu'aucun joueur n'a été trouvé pour l'identifiant donné."""
        print(f"  Aucun joueur trouvé avec l'ID : {national_id}")


class TournamentListView:
    """Vue pour l'affichage de la liste des tournois."""

    def display_current_tournament(self, tournaments):
        """Affiche la liste des tournois en cours avec leur numéro de sélection."""
        print("=== LISTE DES TOURNOIS EN COURS ===")
        for number, tournament in enumerate(tournaments, 1):
            print(f"  {number}. {tournament.name} - {tournament.location}")
        print("0. Retour")

    def display_no_active_tournament(self):
        """Affiche un message indiquant qu'aucun tournoi n'est en cours."""
        print("Aucun tournoi en cours.")


class TournamentDetailsView:
    """Vue pour l'affichage du détail et des actions d'un tournoi."""

    def display_tournament_details(self, tournament):
        """Affiche les informations générales du tournoi."""
        print("=== DETAIL DU TOURNOI ===")
        print(f"Nom du tournoi : {tournament.name}")
        print(f"Lieu du tournoi : {tournament.location}")
        print(f"Date de commencement : {tournament.start_date}")
        print(f"Date de fin : {tournament.end_date}")
        print(f"Nombre de rondes : {tournament.number_of_rounds}")
        print(f"Ronde en cours : {tournament.current_round}")
        print(f"Joueurs inscrits : {len(tournament.players)}")
        print(f"Description : {tournament.description}")
        if tournament.is_finished:
            print(f"Le tournoi {tournament.name} est terminé.")

    def display_actions(self, actions):
        """Affiche les actions disponibles et retourne un dictionnaire numéro → action."""
        labels = {
            "start": "Lancer le tournoi",
            "next_round": "Lancer le prochain round",
            "finished_round": "Terminer le round en cours",
            "enter_results": "Entrer les résultats",
            "show_scores": "Afficher les scores",
            "show_matches": "Afficher les matchs en cours",
            "back": "Retour"
        }
        mapping = {}
        number = 1
        for action in actions:
            if action == "back":
                print(f"0. {labels[action]}")
            else:
                print(f"{number}. {labels[action]}")
                mapping[str(number)] = action
                number += 1
        return mapping

    def display_round_matches(self, round_):
        """Affiche les matchs d'un round."""
        print(f"=== {round_.name} ===")
        for i, match in enumerate(round_.matches, 1):
            print(f"  {i}. {match.player1} vs {match.player2}")

    def display_show_scoreboard(self, scoreboard):
        """Affiche le classement des joueurs avec leurs scores."""
        print("=== CLASSEMENT ===")
        for i, (player, score) in enumerate(scoreboard, 1):
            print(f"  {i}. {player} - {score} pts")

    def display_match(self, match):
        """Affiche les deux joueurs d'un match."""
        print(f"\n{match.player1} vs {match.player2}")

    def display_match_results(self, match, round_):
        """Affiche les options de résultat pour un match donné."""
        print(f"=== RESULTATS DU {round_.name}  ===")
        print(f"1. {match.player1} gagne")
        print(f"2. {match.player2} gagne")
        print("3. Match nul")
        print("0. Retour")
