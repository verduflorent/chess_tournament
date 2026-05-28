from models.tournament import Tournament
from models.match import Match
from models.round import Round

class TournamentController:

    # Initialisation DB
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Création d'un tournoi
    def create_tournament(
            self,
            name,
            place,
            description,
            start_date,
            end_date,
            total_rounds
        ):

        tournament = Tournament(
            name,
            place,
            description,
            start_date,
            end_date,
            total_rounds
        )

        self.db_manager.save_tournament(tournament)

        return tournament

    # Récuperation des tournois
    def get_tournaments(self):

        return self.db_manager.get_tournaments()
    
    # Ajout des joueurs à un tournoi
    def add_player_to_tournament(self, tournament_index, player_index):
        # On récuperes les données des tournois et des joueurs
        tournaments = self.db_manager.get_tournaments()
        players = self.db_manager.get_players()

        # On définis la variable tournoi et joueur en fonction de l'index de chacun
        tournament = tournaments[tournament_index]
        player = players[player_index]

        # On ajoute un joueur en fonction de son index 
        tournament.add_player(player)

        #On sauvegarde les données des tournois dans la BD
        self.db_manager.save_tournaments(tournaments)

        #On retourne le tournoi en fonction de son index
        return tournament
    
    # Generation des rounds
    def generate_round(self, tournament_index):
        tournaments = self.db_manager.get_tournaments()
        tournament = tournaments[tournament_index]

        if tournament.actual_round >= int(tournament.total_rounds):
            raise ValueError("Le tournoi a déjà atteint son nombre maximum de rounds.")
        
        # L'appel de get_tournament_ranking() retourne les joueurs triés par le classement
        players = self.get_tournament_ranking(tournament)

        if len(players) < 2:
            raise ValueError("Il faut au moins 2 joueurs pour générer un round.")

        if len(players) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair pour générer un round.") 

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
        tournaments = self.db_manager.get_tournaments()
        tournament = tournaments[tournament_index]
        selected_round = tournament.rounds[round_index]

        # Si le round possède deja un end_time cela signifie qu'il est terminé
        # On evite donc de modifier les scores plusieurs fois
        if selected_round.end_time is not None:
            raise ValueError("Les résultats de ce round ont déjà été saisis.")

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
        scores = {}

        for player in tournament.players:
            scores[player.national_id] = {
                "player": player,
                "score": 0
            }

        for tournament_round in tournament.rounds:
            for match in tournament_round.matches:
                scores[match.player1.national_id]["score"] += match.score1
                scores[match.player2.national_id]["score"] += match.score2

        ranking = sorted(
            scores.values(),
            key=lambda item: item["score"],
            reverse=True
        )

        return [item["player"] for item in ranking]
    
    # Gestion des rematchs
    # La méthode vérifie si 2 joueurs se sont déja affrontés 
    # On l'appelles dans generate_round() afin d'éviter les rematchs
    def have_played_together(self, tournament, player1, player2):
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