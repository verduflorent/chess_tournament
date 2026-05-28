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

    def generate_round_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments):
            print(index, tournament)
        
        tournament_index = int(input("Numéro du tournoi : "))

        new_round = self.tournament_controller.generate_round(tournament_index)

        print(f"{new_round.name} génené avec succès.")
    
    def enter_round_results_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments):
            print(index, tournament)
        
        tournament_index = int(input("Numéro du tournoi : "))

        tournament = tournaments[tournament_index]

        for index, tournament_round in enumerate(tournament.rounds, start=1):
            print(index, tournament_round)
        
        round_index = int(input("Numéro du round : ")) - 1

        selected_round = self.tournament_controller.enter_round_results(
            tournament_index,
            round_index
        )

        print(f"Résultats enregistrés pour {selected_round.name}")
    
    def display_tournament_details_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = int(input("Numéro du tournoi : ")) - 1
        tournament = tournaments[tournament_index]

        print(f"\nTournoi : {tournament.name}")
        print(f"Lieu : {tournament.place}")
        print(f"Dates : {tournament.start_date} → {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print(f"Nombre de joueurs : {len(tournament.players)}")
        print(f"Nombre de rounds : {len(tournament.rounds)}")

    def display_tournament_players_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = int(input("Numéro du tournoi : ")) - 1
        tournament = tournaments[tournament_index]

        print(f"\nJoueurs du tournoi : {tournament.name}")

        # sorted() est une méthode qui trie les élements d'une liste
        # key=lambda signifie que l'on trie les joueurs par l'att last_name 
        for player in sorted(tournament.players, key=lambda player: player.last_name):
            print(player)
    
    def display_tournament_rounds_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = int(input("Numéro du tournoi : ")) - 1
        tournament = tournaments[tournament_index]

        print(f"\nRounds du tournoi : {tournament.name}")

        for tournament_round in tournament.rounds:
            print(f"\n{tournament_round.name}")
            print(f"Début : {tournament_round.start_time}")
            print(f"Fin : {tournament_round.end_time}")

            for match in tournament_round.matches:
                print(f"  - {match}")
    
    def display_tournament_ranking_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = int(input("Numéro du tournoi : ")) - 1
        tournament = tournaments[tournament_index]

        # On définis un objet score vide
        scores = {}

        # Pour chaque joueur on crée un attribut score via son ID
        for player in tournament.players:
            scores[player.national_id] = {
                "player": player,
                "score": 0
            }

        # Pour chaque match de chaque round on récupère le score et on l'implemente 
        for tournament_round in tournament.rounds:
            for match in tournament_round.matches:
                scores[match.player1.national_id]["score"] += match.score1
                scores[match.player2.national_id]["score"] += match.score2

        # On crée une variable ranking dans laquelle on trie les scores par leur valeur
        # reverse = True inverse l'ordre du tri qui est croissant par défault
        ranking = sorted(
            scores.values(),
            key=lambda item: item["score"],
            reverse=True
        )

        print(f"\nClassement du tournoi : {tournament.name}")

        for index, item in enumerate(ranking, start=1):
            print(f"{index}. {item['player']} - {item['score']} pts")