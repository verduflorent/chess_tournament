from models.match import Match
from datetime import datetime


class Round:
    """Represente un round compose de matchs."""

    def __init__(self, name):
        """Initialise un round avec son nom et son heure de debut.

        Args:
            name: Nom du round.
        """
        self.name = name
        self.matches = []
        self.start_time = datetime.now()
        self.end_time = None

    def add_match(self, match):
        """Ajoute un match au round.

        Args:
            match: Match a ajouter au round.
        """
        self.matches.append(match)

    def end_round(self):
        """Enregistre l'heure de fin du round."""
        self.end_time = datetime.now()

    def __str__(self):
        """Retourne l'affichage lisible du round.

        Returns:
            Le round sous forme de texte.
        """
        return f"Round : {self.name} / Start : {self.start_time} End : {self.end_time}"

    def to_dict(self):
        """Transforme le round en dictionnaire.

        Returns:
            Les donnees du round sous forme de dictionnaire.
        """

        end_time_value = self.end_time.isoformat() if self.end_time else None

        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_time": self.start_time.isoformat(),
            "end_time": end_time_value,
        }

    @classmethod
    def from_dict(cls, round_data, players):
        """Cree un round depuis un dictionnaire.

        Args:
            round_data: Donnees du round.
            players: Liste des joueurs disponibles.

        Returns:
            Une instance de Round.
        """
        matches = [
            Match.from_dict(match_data, players) for match_data in round_data["matches"]
        ]

        round_instance = cls(round_data["name"])
        round_instance.matches = matches
        round_instance.start_time = datetime.fromisoformat(round_data["start_time"])

        if round_data["end_time"]:
            round_instance.end_time = datetime.fromisoformat(round_data["end_time"])

        else:
            round_instance.end_time = None

        return round_instance
