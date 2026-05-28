from models.player import Player


class PlayerController:

    # Initialisation DB
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Création d'un joueur
    def create_player(self, first_name, last_name, birth_date, national_id):

        player = Player(first_name, last_name, birth_date, national_id)

        self.db_manager.save_player(player)

        return player

    # Récuperation des joueurs
    def get_players(self):

        return self.db_manager.get_players()

    # Suppression d'un joueur
    def delete_player(self, player_index):
        players = self.db_manager.get_players()

        deleted_player = players.pop(player_index)

        # truncate() vide totalement la table players afin de la réecrire
        self.db_manager.players_table.truncate()

        for player in players:
            self.db_manager.save_player(player)

        return deleted_player
