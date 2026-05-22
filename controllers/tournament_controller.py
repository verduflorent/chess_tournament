from models.tournament import Tournament

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

