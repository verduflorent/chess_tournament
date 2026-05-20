from tinydb import TinyDB
from models.player import Player
from models.tournament import Tournament


class DatabaseManager:
    # db_path determine le chemin de la BD
    def __init__(self, db_path="data/db.json"):
        #l'attribut db est notre raccourci vers la DB
        self.db = TinyDB(db_path)
        # definition de la table player_table 
        self.players_table = self.db.table("players")
        #definition de la table tournament_table
        self.tournaments_table = self.db.table("tournaments")

    def save_player(self, player):
        self.players_table.insert(player.to_dict())

    def get_players(self):
        #On indique qu'il faut recuperer tout les dictionnaires de la table players
        players_data = self.players_table.all()
        #On crée une variables players qui vas stocker le résultat de notre boucle
        players = [
            #Pour chaque dictionnaire de la boucle on reconstruit l'objet Player
            Player.from_dict(player_data)
            for player_data in players_data
        ]
        
        return players
    
    def save_tournament(self, tournament):
        self.tournaments_table.insert(tournament.to_dict())

    def get_tournament(self):
        tournaments_data = self.tournaments_table.all()

        tournaments = [
            Tournament.from_dict(tournament_data)
            for tournament_data in tournaments_data
        ]

        return tournaments