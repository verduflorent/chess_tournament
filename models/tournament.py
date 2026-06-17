from models.player import Player
from models.round import Round


class Tournament:
    """Represente un tournoi avec ses joueurs et ses rounds."""

    # Initialisation de Tournament
    def __init__(
        self,
        name,
        place,
        description,
        start_date,
        end_date,
        total_rounds,
        actual_round=0,
        rounds=None,
        players=None,
    ):
        """Initialise un tournoi avec ses informations principales.

        Args:
            name: Nom du tournoi.
            place: Lieu du tournoi.
            description: Description du tournoi.
            start_date: Date de debut du tournoi.
            end_date: Date de fin du tournoi.
            total_rounds: Nombre total de rounds prevus.
            actual_round: Numero du round actuel.
            rounds: Liste des rounds du tournoi.
            players: Liste des joueurs inscrits.
        """
        self.name = name
        self.place = place
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_rounds = total_rounds
        self.actual_round = actual_round
        self.rounds = rounds or []
        self.players = players or []

    # Configuration de l'affichage de Tournament
    def __str__(self):
        """Retourne l'affichage lisible du tournoi.

        Returns:
            Le tournoi sous forme de texte.
        """
        return f"{self.name} ({self.start_date})"

    # Ajout d'un joueur au tournoi
    def add_player(self, player):
        """Ajoute un joueur au tournoi s'il n'est pas deja inscrit.

        Args:
            player: Joueur a ajouter au tournoi.
        """
        for existing_player in self.players:
            if existing_player.national_id == player.national_id:
                return

        self.players.append(player)

    # Ajout d'un round au tournoi
    def add_round(self, new_round):
        """Ajoute un round au tournoi s'il n'existe pas deja.

        Args:
            new_round: Round a ajouter au tournoi.
        """
        if new_round not in self.rounds:
            self.rounds.append(new_round)

    # Cette méthode sert a transformer un objet python en dictionnaire simple et compréhensible par JSON
    # Serialization JSON
    def to_dict(self):
        """Transforme le tournoi en dictionnaire.

        Returns:
            Les donnees du tournoi sous forme de dictionnaire.
        """
        return {
            "name": self.name,
            "place": self.place,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "total_rounds": self.total_rounds,
            "actual_round": self.actual_round,
            # Pour chaque objet dans la liste d'objet on appelle la méthode to_dict()
            # pour mettre le résultat dans une nouvelle liste
            "rounds": [new_round.to_dict() for new_round in self.rounds],
            "players": [player.to_dict() for player in self.players],
        }

    # Deserialization JSON
    @classmethod
    def from_dict(cls, tournament_data):
        """Cree un tournoi depuis un dictionnaire.

        Args:
            tournament_data: Donnees du tournoi.

        Returns:
            Une instance de Tournament.
        """
        players = [
            Player.from_dict(player_data) for player_data in tournament_data["players"]
        ]

        rounds = [
            Round.from_dict(round_data, players)
            for round_data in tournament_data["rounds"]
        ]

        tournament_instance = cls(
            tournament_data["name"],
            tournament_data["place"],
            tournament_data["description"],
            tournament_data["start_date"],
            tournament_data["end_date"],
            tournament_data["total_rounds"],
            tournament_data["actual_round"],
            rounds,
            players,
        )

        return tournament_instance
