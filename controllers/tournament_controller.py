from models.tournament import Tournament
from models.match import Match
from models.round import Round


class TournamentController:
    """Controle les actions liees aux tournois."""

    def __init__(self, db_manager):
        """Initialise le controleur avec le gestionnaire de base de donnees.

        Args:
            db_manager: Gestionnaire de base de donnees utilise par le controleur.
        """
        self.db_manager = db_manager

    def create_tournament(
        self, name, place, description, start_date, end_date, total_rounds
    ):
        """Cree un tournoi et l'enregistre en base de donnees.

        Args:
            name: Nom du tournoi.
            place: Lieu du tournoi.
            description: Description du tournoi.
            start_date: Date de debut du tournoi.
            end_date: Date de fin du tournoi.
            total_rounds: Nombre total de rounds prevus.

        Returns:
            Le tournoi cree.
        """

        tournament = Tournament(
            name, place, description, start_date, end_date, total_rounds
        )

        self.db_manager.save_tournament(tournament)

        return tournament

    def get_tournaments(self):
        """Recupere la liste des tournois.

        Returns:
            La liste des tournois enregistres.
        """

        return self.db_manager.get_tournaments()

    def delete_tournament(self, tournament_index):
        """Supprime un tournoi a partir de son index.

        Args:
            tournament_index: Index du tournoi a supprimer.

        Returns:
            Le tournoi supprime.
        """
        tournaments = self.db_manager.get_tournaments()

        deleted_tournament = tournaments.pop(tournament_index)

        self.db_manager.save_tournaments(tournaments)

        return deleted_tournament

    def add_player_to_tournament(self, tournament_index, player_index):
        """Ajoute un joueur selectionne a un tournoi selectionne.

        Args:
            tournament_index: Index du tournoi choisi.
            player_index: Index du joueur choisi.

        Returns:
            Le tournoi mis a jour.

        Raises:
            ValueError: Si le joueur est deja inscrit dans le tournoi.
        """
        tournaments = self.db_manager.get_tournaments()
        players = self.db_manager.get_players()

        tournament = tournaments[tournament_index]
        player = players[player_index]

        for existing_player in tournament.players:
            if existing_player.national_id == player.national_id:
                raise ValueError("Ce joueur est déjà inscrit dans le tournoi.")

        tournament.add_player(player)

        self.db_manager.save_tournaments(tournaments)

        return tournament

    def remove_player_from_tournament(self, tournament_index, player_index):
        """Retire un joueur d'un tournoi si aucun round n'a commence.

        Args:
            tournament_index: Index du tournoi choisi.
            player_index: Index du joueur a retirer.

        Returns:
            Le joueur retire du tournoi.

        Raises:
            ValueError: Si le tournoi a deja commence.
        """
        tournaments = self.db_manager.get_tournaments()
        tournament = tournaments[tournament_index]

        if tournament.rounds:
            raise ValueError(
                "Impossible de retirer un joueur : le tournoi a déjà commencé."
            )

        player = tournament.players[player_index]
        tournament.players.remove(player)

        self.db_manager.save_tournaments(tournaments)

        return player

    def generate_round(self, tournament_index):
        """Genere le prochain round d'un tournoi.

        Args:
            tournament_index: Index du tournoi choisi.

        Returns:
            Le round genere.

        Raises:
            ValueError: Si le round ne peut pas etre genere.
        """
        tournaments = self.db_manager.get_tournaments()
        tournament = tournaments[tournament_index]

        if tournament.rounds and tournament.rounds[-1].end_time is None:
            raise ValueError(
                "Le round précédent doit être terminé avant d'en générer un nouveau."
            )

        if tournament.actual_round >= int(tournament.total_rounds):
            raise ValueError("Le tournoi a déjà atteint son nombre maximum de rounds.")

        players = self.get_tournament_ranking(tournament)

        if len(players) < 2:
            raise ValueError("Il faut au moins 2 joueurs pour générer un round.")

        if len(players) % 2 != 0:
            raise ValueError(
                "Le nombre de joueurs doit être pair pour générer un round."
            )

        matches = []
        available_players = players.copy()

        while available_players:
            player1 = available_players.pop(0)
            opponent = None

            for player2 in available_players:
                if not self.have_played_together(tournament, player1, player2):
                    opponent = player2
                    break

            if opponent is None:
                opponent = available_players[0]

            available_players.remove(opponent)

            match = Match(player1, opponent)
            matches.append(match)

        new_round = Round(f"Round {tournament.actual_round + 1}")

        for match in matches:
            new_round.add_match(match)

        tournament.add_round(new_round)

        tournament.actual_round += 1

        self.db_manager.save_tournaments(tournaments)

        return new_round

    def enter_round_results(self, tournament_index, round_index):
        """Saisit les resultats d'un round et le termine.

        Args:
            tournament_index: Index du tournoi choisi.
            round_index: Index du round choisi.

        Returns:
            Le round termine avec ses resultats.
        """
        tournaments = self.db_manager.get_tournaments()
        tournament = tournaments[tournament_index]
        selected_round = tournament.rounds[round_index]

        for match in selected_round.matches:
            print(match)
            score1 = float(input(f"Score de {match.player1} : "))
            score2 = float(input(f"Score de {match.player2} : "))

            match.score1 = score1
            match.score2 = score2

        selected_round.end_round()

        self.db_manager.save_tournaments(tournaments)

        return selected_round

    def get_tournament_ranking(self, tournament):
        """Retourne les joueurs du tournoi tries par score.

        Args:
            tournament: Tournoi dont le classement est calcule.

        Returns:
            La liste des joueurs triee par score decroissant.
        """
        scores = {}

        for player in tournament.players:
            scores[player.national_id] = {"player": player, "score": 0}

        for tournament_round in tournament.rounds:
            for match in tournament_round.matches:
                scores[match.player1.national_id]["score"] += match.score1
                scores[match.player2.national_id]["score"] += match.score2

        ranking = sorted(scores.values(), key=lambda item: item["score"], reverse=True)

        return [item["player"] for item in ranking]

    def have_played_together(self, tournament, player1, player2):
        """Verifie si deux joueurs se sont deja affrontes.

        Args:
            tournament: Tournoi dans lequel chercher les matchs.
            player1: Premier joueur a comparer.
            player2: Deuxieme joueur a comparer.

        Returns:
            True si les joueurs se sont deja affrontes, sinon False.
        """
        for tournament_round in tournament.rounds:
            for match in tournament_round.matches:
                same_order = (
                    match.player1.national_id == player1.national_id
                    and match.player2.national_id == player2.national_id
                )

                reverse_order = (
                    match.player1.national_id == player2.national_id
                    and match.player2.national_id == player1.national_id
                )

                if same_order or reverse_order:
                    return True

        return False
