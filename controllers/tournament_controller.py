from models.tournament import Tournament
from models.match import Match
from models.round import Round

class TournamentController:

    def __init__(self, db_manager):
        self.db_manager = db_manager

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

    def get_tournaments(self):

        return self.db_manager.get_tournaments()
    
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
    
    def generate_round(self, tournament_index):
        tournaments = self.db_manager.get_tournaments()
        tournament = tournaments[tournament_index]

        players = tournament.players

        matches = []

        if len(players) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair pour generer un round")
        # On parcours l'index avec la méthode range() qui sert a définir la portée de notre recherche
        # len(players) signifie qu'on parcours toute la liste players et le 2 signifie qu'on veut les recuperer par 2
        for index in range(0, len(players), 2) :

            player1 = players[index]
            player2 = players[index + 1]

            match = Match(player1, player2)
            matches.append(match)

        new_round = Round(f"Round {tournament.actual_round + 1}")

        for match in matches:
            new_round.add_match(match)
        
        tournament.add_round(new_round)

        tournament.actual_round += 1

        self.db_manager.save_tournaments(tournaments)

        return new_round