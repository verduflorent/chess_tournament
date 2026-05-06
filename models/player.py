class Player:
    # __init__ permet d'initialiser l'objet a sa création et stocke les donnée dans l'objet concerné avec précision
    # self sert a cibler l'objet à l'intérieur de la classe sinon tout les objets player partageraient les meme valeurs
    def __init__(self, first_name, last_name, birth_date, national_id):
        self.first_name = first_name 
        self.last_name = last_name
        self.birth_date = birth_date
        self.national_id = national_id 

    #__str__ permet d'afficher les données de l'objet en format string
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.national_id})"