class TournamentView:
    def __init__(self, tournament_controller, player_controller):
        self.tournament_controller = tournament_controller
        self.player_controller = player_controller
    
    def create_tournament_view(self):
        name = input("Nom : ")
        place = input("Lieu : ")
        description = input("Description : ")
        start_date = input("Début du tournoi (JJ/MM/AAAA HH:MM) : ")
        end_date = input("Fin du tournoi (JJ/MM/DDDD HH:MM) : ")
        total_rounds = input("Nombre de rounds : ")
    
        tournament = self.tournament_controller.create_tournament(
            name,
            place,
            description,
            start_date,
            end_date,
            total_rounds
        )

        print(f"Tournoi crée : {tournament.name}")
    
    def display_tournaments_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for tournament in tournaments:
            print(tournament)
    
    def add_player_to_tournament_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        #Enumerate() sert à parcourir une liste en récuperant automatiquement un numéro(index)
        for index, tournament in enumerate(tournaments):
            print(index, tournament)

        players = self.player_controller.get_players()

        for index, player in enumerate(players):
            print(index, player)
        
        #On passe le format en int afin de garder l'index en entier exploitable
        tournament_index = int(input("Numéro du tournoi : "))
        player_index = int(input("Numéro du joueur : "))

        tournament = self.tournament_controller.add_player_to_tournament(
            tournament_index,
            player_index
        )

        print(f"Joueur ajouté au tournoi : {tournament}")