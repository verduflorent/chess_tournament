class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def __str__(self):
        return f"{self.player1} : {self.score1} / {self.player2} : {self.score2}"
   
    def to_dict(self):
        return{
            "player1": self.player1.national_id,
            "player2": self.player2.national_id,
            "score1": self.score1,
            "score2": self.score2
        }