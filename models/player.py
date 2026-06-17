class Player:
    """Represente un joueur du tournoi."""

    def __init__(self, first_name, last_name, birth_date, national_id):
        """Initialise un joueur avec ses informations principales.

        Args:
            first_name: Prenom du joueur.
            last_name: Nom du joueur.
            birth_date: Date de naissance du joueur.
            national_id: Identifiant national du joueur.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.national_id = national_id

    def __str__(self):
        """Retourne l'affichage lisible du joueur.

        Returns:
            Le joueur sous forme de texte.
        """
        return f"{self.first_name} {self.last_name} ({self.national_id})"

    def to_dict(self):
        """Transforme le joueur en dictionnaire.

        Returns:
            Les donnees du joueur sous forme de dictionnaire.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
        }

    @classmethod
    def from_dict(cls, player_data):
        """Cree un joueur depuis un dictionnaire.

        Args:
            player_data: Donnees du joueur.

        Returns:
            Une instance de Player.
        """
        return cls(
            player_data["first_name"],
            player_data["last_name"],
            player_data["birth_date"],
            player_data["national_id"],
        )
