class ReportMainView:
    """Vue du menu principal des rapports."""

    def display_main_menu(self):
        """Affiche le menu des rapports avec les options disponibles."""
        print("\n=== RAPPORTS ===")
        print("1. Tous les joueurs")
        print("2. Tous les tournois")
        print("3. Détail d'un tournoi")
        print("0. Retour")


class ReportView:
    """Vue pour l'affichage des rapports détaillés."""

    def display_all_players(self, players):
        """Affiche la liste complète de tous les joueurs enregistrés."""
        print("\n=== TOUS LES JOUEURS ===")
        if not players:
            print("Aucun joueur enregistré.")
            return
        for player in players:
            print(f"  {player.last_name} {player.first_name} "
                  f"({player.national_id}) — né le {player.date_of_birth}")

    def display_all_tournaments(self, tournaments):
        """Affiche la liste complète de tous les tournois enregistrés."""
        print("\n=== TOUS LES TOURNOIS ===")
        if not tournaments:
            print("Aucun tournoi enregistré.")
            return
        for i, t in enumerate(tournaments, 1):
            print(f"  {i}. {t.name} — {t.location} "
                  f"({t.start_date} / {t.end_date})")

    def display_tournament_detail(self, tournament):
        """Affiche le détail complet d'un tournoi : joueurs, rounds, matchs et classement."""
        print(f"\n=== {tournament.name} ===")
        print(f"  Lieu       : {tournament.location}")
        print(f"  Dates      : {tournament.start_date} → {tournament.end_date}")
        print(f"  Rounds     : {tournament.number_of_rounds}")
        if tournament.description:
            print(f"  Description: {tournament.description}")

        print("\n--- JOUEURS ---")
        if not tournament.players:
            print("  Aucun joueur inscrit.")
        else:
            for player in sorted(tournament.players):
                print(f"  {player.last_name} {player.first_name} ({player.national_id})")

        print("\n--- ROUNDS & MATCHS ---")
        if not tournament.rounds:
            print("  Aucun round joué.")
        else:
            for round_ in tournament.rounds:
                status = f"terminé le {round_.end_time}" if round_.end_time else "en cours"
                print(f"\n  {round_.name} — débuté le {round_.start_time} — {status}")
                for match in round_.matches:
                    print(f"    {match.player1.last_name} {match.score1} "
                          f"— {match.score2} {match.player2.last_name}")

        print("\n--- CLASSEMENT ---")
        if not tournament.scores:
            print("  Pas encore de scores.")
        else:
            for i, (player, score) in enumerate(tournament.scoreboard, 1):
                print(f"  {i}. {player.last_name} {player.first_name} — {score} pts")
