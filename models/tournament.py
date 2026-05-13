

class Tournament:
    def __init__(
            self,
            name, 
            place,
            description, 
            start_date, 
            end_date, 
            total_rounds, 
            actual_round = 0, 
            rounds = None, 
            players = None 
            ):
        self.name = name
        self.place = place
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_rounds = total_rounds
        self.actual_round = actual_round
        self.rounds = rounds or []
        self.players = players or []

    def add_player(self,player):
        if player not in self.players:
            self.players.append(player)
    
    def add_round(self,new_round):
        if new_round not in self.rounds:
            self.rounds.append(new_round)

# Cette méthode sert a transformer un objet python en dictionnaire simple et compréhensible par JSON
    def to_dict(self):
        return{
            "name": self.name,
            "place": self.place,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "total_rounds": self.total_rounds,
            "actual_round": self.actual_round,
            #Pour chaque objet dans la liste d'objet on appelle la méthode to_dict() pour mettre le résultat dans une nouvelle liste
            "rounds": [new_round.to_dict() for new_round in self.rounds],
            "players": [player.to_dict() for player in self.players]
        }