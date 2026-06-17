class Player:
    """Represente un joueur du tournoi."""

    # __init__ permet d'initialiser l'objet a sa création et stocke les donnée dans l'objet concerné avec précision
    # self sert a cibler l'objet à l'intérieur de la classe sinon tout les objets player partageraient les meme valeurs
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

    # __str__ permet d'afficher les données de l'objet en format string
    def __str__(self):
        """Retourne l'affichage lisible du joueur.

        Returns:
            Le joueur sous forme de texte.
        """
        return f"{self.first_name} {self.last_name} ({self.national_id})"

    # to_dict() sert a transformer un objet en dictionnaire JSON
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

    # from_dict() recrée un objet à partir des données JSON
    # @classmethod précise que la méthode appartient à la classe
    # -- cela nous permet de réutiliser la même methode sur une autre classe
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
