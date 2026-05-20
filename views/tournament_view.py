class TournamentView:
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller
    
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