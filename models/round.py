from datetime import datetime

class Round:
    def __init__(self, name):
        self.name = name
        #On ne demande pas ces attributs en paramètres car on les définis dans l'objet
        #Pour matches on commence avec une liste vide qu'on rempliras dans le script
        self.matches = []
        #Pour start_time la valeur se définit automatiquement au moment de la création du round
        self.start_time = datetime.now()
        #Pour end_time le round n'est pas terminé au moment de sa création donc la valeur finale de l'attribut n'est pas definie dans l'init
        self.end_time = None

    def add_match(self, match):
        self.matches.append(match)

    def end_round(self):
        self.end_time = datetime.now()


    def __str__(self):
        return f"Round : {self.name} / Start : {self.start_time} End : {self.end_time}"
    
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