from tinydb import TinyDB
from models.player import Player
from models.tournament import Tournament


class DatabaseManager:
    """Gere les acces a la base de donnees TinyDB."""

    # db_path determine le chemin de la BD
    def __init__(self, db_path="data/db.json"):
        """Initialise la base de donnees et ses tables."""
        # l'attribut db est notre raccourci vers la DB
        self.db = TinyDB(db_path)
        # definition de la table player_table
        self.players_table = self.db.table("players")
        # definition de la table tournament_table
        self.tournaments_table = self.db.table("tournaments")

    def save_player(self, player):
        """Enregistre un joueur en base de donnees."""
        self.players_table.insert(player.to_dict())

    def get_players(self):
        """Recupere tous les joueurs en base de donnees."""
        # On indique qu'il faut recuperer tout les dictionnaires de la table players
        players_data = self.players_table.all()
        # On crée une variables players qui vas stocker le résultat de notre boucle
        players = [
            # Pour chaque dictionnaire de la boucle on reconstruit l'objet Player
            Player.from_dict(player_data)
            for player_data in players_data
        ]

        return players

    def save_tournament(self, tournament):
        """Enregistre un tournoi en base de donnees."""
        self.tournaments_table.insert(tournament.to_dict())

    def save_tournaments(self, tournaments):
        """Remplace la liste des tournois en base de donnees."""
        # La méthode trunkate vide la table tournaments
        self.tournaments_table.truncate()
        # On réecris ensuite la table pour éviter les doublons
        for tournament in tournaments:
            self.tournaments_table.insert(tournament.to_dict())

    def get_tournaments(self):
        """Recupere tous les tournois en base de donnees."""
        tournaments_data = self.tournaments_table.all()

        tournaments = [
            Tournament.from_dict(tournament_data)
            for tournament_data in tournaments_data
        ]

        return tournaments
