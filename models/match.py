class Match:

    # Initialisation de la classe Match
    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    # Configuration de l'affichage des matchs
    def __str__(self):
        return f"{self.player1} : {self.score1} / {self.player2} : {self.score2}"
    
    # Serialization JSON
    def to_dict(self):
        return{
            "player1": self.player1.national_id,
            "player2": self.player2.national_id,
            "score1": self.score1,
            "score2": self.score2
        }
    
    @classmethod

    # Déserialization JSON
    def from_dict(cls, match_data, players):

        player1 = None
        player2 = None

        for player in players :
            if player.national_id == match_data["player1"]:
                player1 = player
            
            elif player.national_id == match_data["player2"]:
                player2 = player

        if player1 is None or player2 is None:
            raise ValueError("Impossible de recréer le match: joueur introuvable.")
        
        return cls(
            player1,
            player2,
            match_data["score1"],
            match_data["score2"]
        )