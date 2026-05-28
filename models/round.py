from models.match import Match
from datetime import datetime

class Round:

    # Initialisation de Round
    def __init__(self, name):
        self.name = name
        #On ne demande pas ces attributs en paramètres car on les définis dans l'objet
        #Pour matches on commence avec une liste vide qu'on rempliras dans le script
        self.matches = []
        #Pour start_time la valeur se définit automatiquement au moment de la création du round
        self.start_time = datetime.now()
        #Pour end_time le round n'est pas terminé au moment de sa création donc la valeur finale de l'attribut n'est pas definie dans l'init
        self.end_time = None

    # Ajout de match au round
    def add_match(self, match):
        self.matches.append(match)

    # Automatisation de la variable de fin de round
    def end_round(self):
        self.end_time = datetime.now()

    # Configuratin de l'affichage de Round
    def __str__(self):
        return f"Round : {self.name} / Start : {self.start_time} End : {self.end_time}"
    
    # Serialization JSON
    def to_dict(self):

        end_time_value = (
            self.end_time.isoformat()
            if self.end_time
            else None
            )

        return{
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_time": self.start_time.isoformat(),
            "end_time" : end_time_value
        }
    
    @classmethod

    # Deserialization JSON
    def from_dict(cls, round_data, players):
        matches = [
                Match.from_dict(match_data, players)
            for match_data in round_data["matches"] 
            ]
        
        # On doit recréer un round_instance pour remplacer les valeurs générés automatiquement dant notre __init__
        round_instance = cls(round_data["name"])
        round_instance.matches = matches
        #avec datetime.isoformat()on reconvertit la date au format iso(JSON) en format datetime(objet)
        round_instance.start_time = datetime.fromisoformat(round_data["start_time"])
        
        if round_data["end_time"]:
            round_instance.end_time = datetime.fromisoformat(round_data["end_time"])
        
        else:
            round_instance.end_time = None

        return round_instance