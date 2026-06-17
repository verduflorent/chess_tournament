from datetime import datetime


class TournamentView:
    """Gere les affichages et saisies lies aux tournois."""

    def __init__(self, tournament_controller, player_controller):
        """Initialise la vue avec les controleurs necessaires.

        Args:
            tournament_controller: Controleur utilise pour gerer les tournois.
            player_controller: Controleur utilise pour gerer les joueurs.
        """
        self.tournament_controller = tournament_controller
        self.player_controller = player_controller

    def get_valid_integer_input(self, message):
        """Demande un nombre entier valide.

        Args:
            message: Message affiche avant la saisie.

        Returns:
            Le nombre entier saisi par l'utilisateur.
        """
        while True:
            try:
                return int(input(message))

            except ValueError:
                print("Erreur : veuillez entrer un nombre valide.")

    def get_valid_datetime_input(self, message):
        """Demande une date et une heure valides.

        Args:
            message: Message affiche avant la saisie.

        Returns:
            La date et l'heure valides saisies par l'utilisateur.
        """
        while True:
            date_value = input(message)

            try:
                datetime.strptime(date_value, "%d/%m/%Y %H:%M")
                return date_value

            except ValueError:
                print(
                    "Erreur : format invalide. "
                    "Format attendu : JJ/MM/AAAA HH:MM"
                )

    def create_tournament_view(self):
        """Affiche le formulaire de creation d'un tournoi."""
        name = input("Nom : ")
        place = input("Lieu : ")
        description = input("Description : ")
        start_date = self.get_valid_datetime_input(
            "Date de début (JJ/MM/AAAA HH:MM) : "
        )
        end_date = self.get_valid_datetime_input(
            "Date de fin (JJ/MM/AAAA HH:MM) : "
        )
        total_rounds = input("Nombre de rounds : ")

        if end_date <= start_date:
            print(
                "Erreur : la date de fin doit être postérieure "
                "à la date de début."
            )
            return

        tournament = self.tournament_controller.create_tournament(
            name, place, description, start_date, end_date, total_rounds
        )

        print(f"Tournoi crée : {tournament.name}")

    def delete_tournament_view(self):
        """Affiche le formulaire de suppression d'un tournoi."""
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = (
            self.get_valid_integer_input("Numéro du tournoi à supprimer : ") - 1
        )

        try:
            deleted_tournament = self.tournament_controller.delete_tournament(
                tournament_index
            )
            print(f"Tournoi supprimé : {deleted_tournament}")

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")

    def display_tournaments_view(self):
        """Affiche la liste des tournois."""
        tournaments = self.tournament_controller.get_tournaments()

        for tournament in tournaments:
            print(tournament)

    def add_player_to_tournament_view(self):
        """Affiche le formulaire d'ajout d'un joueur a un tournoi."""
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        players = self.player_controller.get_players()

        for index, player in enumerate(players, start=1):
            print(index, player)

        tournament_index = self.get_valid_integer_input("Numéro du tournoi : ") - 1
        player_index = self.get_valid_integer_input("Numéro du joueur : ") - 1

        try:
            tournament = self.tournament_controller.add_player_to_tournament(
                tournament_index, player_index
            )
            print(f"Joueur ajouté au tournoi : {tournament}")

        except IndexError:
            print("Erreur : numéro de tournoi ou de joueur invalide.")

        except ValueError as error:
            print(f"Erreur : {error}")

    def remove_player_from_tournament_view(self):
        """Affiche le formulaire de retrait d'un joueur d'un tournoi."""
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input("Numéro du tournoi : ") - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return

        if not tournament.players:
            print("Ce tournoi ne contient aucun joueur.")
            return

        for index, player in enumerate(tournament.players, start=1):
            print(index, player)

        player_index = self.get_valid_integer_input("Numéro du joueur à retirer : ") - 1

        try:
            player = self.tournament_controller.remove_player_from_tournament(
                tournament_index, player_index
            )
            print(f"Joueur retiré du tournoi : {player}")

        except IndexError:
            print("Erreur : numéro de joueur invalide.")

        except ValueError as error:
            print(f"Erreur : {error}")

    def generate_round_view(self):
        """Affiche le formulaire de generation d'un round."""
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input("Numéro du tournoi : ") - 1

        try:
            new_round = self.tournament_controller.generate_round(tournament_index)
            print(f"{new_round.name} généré avec succès.")

            print("\nMatchs générés :")

            for match in new_round.matches:
                print(f"- {match}")

        except ValueError as error:
            print(f"Erreur : {error}")

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")

    def enter_round_results_view(self):
        """Affiche le formulaire de saisie des resultats d'un round."""
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input("Numéro du tournoi : ") - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return

        for index, tournament_round in enumerate(tournament.rounds, start=1):
            print(index, tournament_round)

        round_index = self.get_valid_integer_input("Numéro du round : ") - 1

        try:
            selected_round = self.tournament_controller.enter_round_results(
                tournament_index, round_index
            )
            print(f"Résultats enregistrés pour {selected_round.name}.")

        except IndexError:
            print("Erreur : numéro de tournoi ou de round invalide.")

        except ValueError as error:
            print(f"Erreur : {error}")

    def display_tournament_details_view(self):
        """Affiche les details d'un tournoi."""
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input("Numéro du tournoi : ") - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return

        print(f"\nTournoi : {tournament.name}")
        print(f"Lieu : {tournament.place}")
        print(f"Dates : {tournament.start_date} → {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print(f"Nombre de joueurs : {len(tournament.players)}")
        print(f"Nombre de rounds : {len(tournament.rounds)}")

    def display_tournament_players_view(self):
        """Affiche les joueurs d'un tournoi."""
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input("Numéro du tournoi : ") - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return

        if not tournament.players:
            print("Ce tournoi ne contient aucun joueur")
            return

        print(f"\nJoueurs du tournoi : {tournament.name}")

        for player in sorted(tournament.players, key=lambda player: player.last_name):
            print(player)

    def display_tournament_rounds_view(self):
        """Affiche les rounds et matchs d'un tournoi."""
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input("Numéro du tournoi : ") - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return

        if not tournament.rounds:
            print("Ce tournoi ne contient aucun round")
            return

        print(f"\nRounds du tournoi : {tournament.name}")

        for tournament_round in tournament.rounds:
            print(f"\n{tournament_round.name}")
            print(f"Début : {tournament_round.start_time}")
            print(f"Fin : {tournament_round.end_time}")

            for match in tournament_round.matches:
                print(f"  - {match}")

    def display_tournament_ranking_view(self):
        """Affiche le classement d'un tournoi."""
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input("Numéro du tournoi : ") - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return

        if not tournament.players:
            print("Ce tournoi ne contient aucun joueur")
            return

        scores = {}

        for player in tournament.players:
            scores[player.national_id] = {"player": player, "score": 0}

        for tournament_round in tournament.rounds:
            for match in tournament_round.matches:
                scores[match.player1.national_id]["score"] += match.score1
                scores[match.player2.national_id]["score"] += match.score2

        ranking = sorted(scores.values(), key=lambda item: item["score"], reverse=True)

        print(f"\nClassement du tournoi : {tournament.name}")

        for index, item in enumerate(ranking, start=1):
            print(f"{index}. {item['player']} - {item['score']} pts")
