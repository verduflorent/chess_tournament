from tinydb import TinyDB
from models.player import Player
from models.tournament import Tournament


class DatabaseManager:
    """Gere les acces a la base de donnees TinyDB."""

    def __init__(self, db_path="data/db.json"):
        """Initialise la base de donnees et ses tables.

        Args:
            db_path: Chemin du fichier de base de donnees.
        """
        self.db = TinyDB(db_path)
        self.players_table = self.db.table("players")
        self.tournaments_table = self.db.table("tournaments")

    def save_player(self, player):
        """Enregistre un joueur en base de donnees.

        Args:
            player: Joueur a enregistrer.
        """
        self.players_table.insert(player.to_dict())

    def get_players(self):
        """Recupere tous les joueurs en base de donnees.

        Returns:
            La liste des joueurs enregistres.
        """
        players_data = self.players_table.all()
        players = [
            Player.from_dict(player_data)
            for player_data in players_data
        ]

        return players

    def save_tournament(self, tournament):
        """Enregistre un tournoi en base de donnees.

        Args:
            tournament: Tournoi a enregistrer.
        """
        self.tournaments_table.insert(tournament.to_dict())

    def save_tournaments(self, tournaments):
        """Remplace la liste des tournois en base de donnees.

        Args:
            tournaments: Liste des tournois a enregistrer.
        """
        self.tournaments_table.truncate()
        for tournament in tournaments:
            self.tournaments_table.insert(tournament.to_dict())

    def get_tournaments(self):
        """Recupere tous les tournois en base de donnees.

        Returns:
            La liste des tournois enregistres.
        """
        tournaments_data = self.tournaments_table.all()

        tournaments = [
            Tournament.from_dict(tournament_data)
            for tournament_data in tournaments_data
        ]

        return tournaments
