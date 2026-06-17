from models.tournament import Tournament
from models.match import Match
from models.round import Round


class TournamentController:
    """Controle les actions liees aux tournois."""

    # Initialisation DB
    def __init__(self, db_manager):
        """Initialise le controleur avec le gestionnaire de base de donnees."""
        self.db_manager = db_manager

    # Création d'un tournoi
    def create_tournament(
        self, name, place, description, start_date, end_date, total_rounds
    ):
        """Cree un tournoi et l'enregistre en base de donnees."""

        tournament = Tournament(
            name, place, description, start_date, end_date, total_rounds
        )

        self.db_manager.save_tournament(tournament)

        return tournament

    # Récuperation des tournois
    def get_tournaments(self):
        """Recupere la liste des tournois."""

        return self.db_manager.get_tournaments()

    # Suppression d'un tournoi
    def delete_tournament(self, tournament_index):
        """Supprime un tournoi a partir de son index."""
        tournaments = self.db_manager.get_tournaments()

        deleted_tournament = tournaments.pop(tournament_index)

        self.db_manager.save_tournaments(tournaments)

        return deleted_tournament

    # Ajout des joueurs à un tournoi
    def add_player_to_tournament(self, tournament_index, player_index):
        """Ajoute un joueur selectionne a un tournoi selectionne."""
        # On récuperes les données des tournois et des joueurs
        tournaments = self.db_manager.get_tournaments()
        players = self.db_manager.get_players()

        # On définis la variable tournoi et joueur en fonction de l'index de chacun
        tournament = tournaments[tournament_index]
        player = players[player_index]

        # On check si le joueur existe déja
        for existing_player in tournament.players:
            if existing_player.national_id == player.national_id:
                raise ValueError("Ce joueur est déjà inscrit dans le tournoi.")

        # On ajoute un joueur en fonction de son index
        tournament.add_player(player)

        # On sauvegarde les données des tournois dans la BD
        self.db_manager.save_tournaments(tournaments)

        # On retourne le tournoi en fonction de son index
        return tournament

    # Suppression d'un joueur du tournoi
    def remove_player_from_tournament(self, tournament_index, player_index):
        """Retire un joueur d'un tournoi si aucun round n'a commence."""
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

    # Generation des rounds
    def generate_round(self, tournament_index):
        """Genere le prochain round d'un tournoi."""
        tournaments = self.db_manager.get_tournaments()
        tournament = tournaments[tournament_index]

        # ------ GESTION DES ERREURS -----
        if tournament.rounds and tournament.rounds[-1].end_time is None:
            raise ValueError(
                "Le round précédent doit être terminé avant d'en générer un nouveau."
            )

        if tournament.actual_round >= int(tournament.total_rounds):
            raise ValueError("Le tournoi a déjà atteint son nombre maximum de rounds.")

        # L'appel de get_tournament_ranking() retourne les joueurs triés par le classement
        players = self.get_tournament_ranking(tournament)

        if len(players) < 2:
            raise ValueError("Il faut au moins 2 joueurs pour générer un round.")

        if len(players) % 2 != 0:
            raise ValueError(
                "Le nombre de joueurs doit être pair pour générer un round."
            )

        # ------ GESTION DES ROUNDS -----
        matches = []
        # copy() crée une copie de la liste originale afin de retirer des joueurs sans modifier la liste originale
        available_players = players.copy()

        while available_players:
            # On prends le premier joueur (le mieux classé) et pop() le retire de la liste
            player1 = available_players.pop(0)
            # On prépare une variable pour stocker son futur adversaire
            opponent = None

            # On parcours le reste de la liste pour trouver un adversaire
            for player2 in available_players:
                # On verifie que player 1 et 2 ne se sont pas affrontés
                if not self.have_played_together(tournament, player1, player2):
                    # Si les critères sont remplis alors player2 devient la variable que l'on a stocké au préalable
                    opponent = player2
                    break

            # Si aucun adversaire répondant a notre critère n'as été trouvé
            if opponent is None:
                # On prend le premier joueur de la liste pour éviter de bloquer le processus de création de round
                opponent = available_players[0]

            # remove() retire l'opposant de la liste copiée
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

    # Saisie manuelle des résultats du round
    def enter_round_results(self, tournament_index, round_index):
        """Saisit les resultats d'un round et le termine."""
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

    # Récupération du classement du tournoi
    def get_tournament_ranking(self, tournament):
        """Retourne les joueurs du tournoi tries par score."""
        scores = {}

        for player in tournament.players:
            scores[player.national_id] = {"player": player, "score": 0}

        for tournament_round in tournament.rounds:
            for match in tournament_round.matches:
                scores[match.player1.national_id]["score"] += match.score1
                scores[match.player2.national_id]["score"] += match.score2

        # sorted cree une liste des valeurs a trier
        # Lambda + item definisse l'attribut que l'on veut trier
        ranking = sorted(scores.values(), key=lambda item: item["score"], reverse=True)

        return [item["player"] for item in ranking]

    # Gestion des rematchs
    # La méthode vérifie si 2 joueurs se sont déja affrontés
    # On l'appelles dans generate_round() afin d'éviter les rematchs
    def have_played_together(self, tournament, player1, player2):
        """Verifie si deux joueurs se sont deja affrontes."""
        for tournament_round in tournament.rounds:
            for match in tournament_round.matches:
                # On verifie dans l'ordre des paramètres
                same_order = (
                    match.player1.national_id == player1.national_id
                    and match.player2.national_id == player2.national_id
                )

                # Puis on vérifie dans l'ordre inverse des paramètres
                reverse_order = (
                    match.player1.national_id == player2.national_id
                    and match.player2.national_id == player1.national_id
                )

                # Si une des vérification renvoie true alors la rencontre a déja eu lieu et on return True
                if same_order or reverse_order:
                    return True

        # Si aucune vérification return True alors la rencontre n'as pas lieu et on return False
        return False
