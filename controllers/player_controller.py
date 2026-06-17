from models.player import Player


class PlayerController:
    """Controle les actions liees aux joueurs."""

    # Initialisation DB
    def __init__(self, db_manager):
        """Initialise le controleur avec le gestionnaire de base de donnees.

        Args:
            db_manager: Gestionnaire de base de donnees utilise par le controleur.
        """
        self.db_manager = db_manager

    # Création d'un joueur
    def create_player(self, first_name, last_name, birth_date, national_id):
        """Cree un joueur et l'enregistre en base de donnees.

        Args:
            first_name: Prenom du joueur.
            last_name: Nom du joueur.
            birth_date: Date de naissance du joueur.
            national_id: Identifiant national du joueur.

        Returns:
            Le joueur cree.
        """

        player = Player(first_name, last_name, birth_date, national_id)

        self.db_manager.save_player(player)

        return player

    # Récuperation des joueurs
    def get_players(self):
        """Recupere la liste des joueurs.

        Returns:
            La liste des joueurs enregistres.
        """

        return self.db_manager.get_players()

    # Suppression d'un joueur
    def delete_player(self, player_index):
        """Supprime un joueur s'il n'est inscrit dans aucun tournoi.

        Args:
            player_index: Index du joueur a supprimer.

        Returns:
            Le joueur supprime.

        Raises:
            ValueError: Si le joueur est inscrit dans un tournoi.
        """
        players = self.db_manager.get_players()
        player_to_delete = players[player_index]

        tournaments = self.db_manager.get_tournaments()

        for tournament in tournaments:
            for tournament_player in tournament.players:
                if tournament_player.national_id == player_to_delete.national_id:
                    raise ValueError(
                        "Impossible de supprimer ce joueur : "
                        "il est inscrit dans un tournoi."
                    )

        deleted_player = players.pop(player_index)

        self.db_manager.players_table.truncate()

        for player in players:
            self.db_manager.save_player(player)

        return deleted_player
