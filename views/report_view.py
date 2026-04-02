# views/report_view.py

class ReportMainView:
    def display_main_menu(self):
        print("\n=== RAPPORTS ===")
        print("1. Tous les joueurs (alphabétique)")
        print("2. Tous les tournois")
        print("3. Joueurs d'un tournoi")
        print("4. Rounds d'un tournoi")
        print("5. Matchs d'un tournoi")
        print("0. Retour")


class ReportView:

    def display_all_players(self, players):
        print("\n=== TOUS LES JOUEURS ===")
        if not players:
            print("Aucun joueur enregistré.")
            return
        for player in players:
            print(f"  {player.last_name} {player.first_name} "
                  f"({player.national_id}) — né le {player.date_of_birth}")

    def display_all_tournaments(self, tournaments):
        print("\n=== TOUS LES TOURNOIS ===")
        if not tournaments:
            print("Aucun tournoi enregistré.")
            return
        for i, t in enumerate(tournaments, 1):
            print(f"  {i}. {t.name} — {t.location} "
                  f"({t.start_date} / {t.end_date})")
        print("0. Retour")

    def display_tournament_players(self, tournament):
        print(f"\n=== JOUEURS — {tournament.name} ===")
        if not tournament.players:
            print("Aucun joueur inscrit.")
            return
        for player in sorted(tournament.players):
            print(f"  {player.last_name} {player.first_name} ({player.national_id})")

    def display_tournament_rounds(self, tournament):
        print(f"\n=== ROUNDS — {tournament.name} ===")
        if not tournament.rounds:
            print("Aucun round joué.")
            return
        for round_ in tournament.rounds:
            status = f"terminé le {round_.end_time}" if round_.end_time else "en cours"
            print(f"  {round_.name} — débuté le {round_.start_time} ({status})")

    def display_tournament_matches(self, tournament):
        print(f"\n=== MATCHS — {tournament.name} ===")
        if not tournament.rounds:
            print("Aucun match joué.")
            return
        for round_ in tournament.rounds:
            print(f"\n  {round_.name}")
            for match in round_.matches:
                print(f"    {match.player1.last_name} {match.score1} "
                      f"— {match.score2} {match.player2.last_name}")
 