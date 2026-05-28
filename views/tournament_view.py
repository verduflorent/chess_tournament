class TournamentView:

    # Initialisation de TournamentView
    def __init__(self, tournament_controller, player_controller):
        self.tournament_controller = tournament_controller
        self.player_controller = player_controller
    
    # Securisation des inputs
    def get_valid_integer_input(self, message):
        while True:
            try:
                return int(input(message))

            except ValueError:
                print("Erreur : veuillez entrer un nombre valide.")
    
    # Creation de la vue tournoi
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

    #Affichage de la vue de suppression des tournois
    def delete_tournament_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input(
            "Numéro du tournoi à supprimer : "
        ) - 1

        try:
            deleted_tournament = self.tournament_controller.delete_tournament(
                tournament_index
            )
            print(f"Tournoi supprimé : {deleted_tournament}")

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
    
    # Affichage de la vue tournoi
    def display_tournaments_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for tournament in tournaments:
            print(tournament)
    
    # Affichage de la vue d'ajout de joueur
    def add_player_to_tournament_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        #Enumerate() sert à parcourir une liste en récuperant automatiquement un numéro(index)
        for index, tournament in enumerate(tournaments):
            print(index, tournament)

        players = self.player_controller.get_players()

        for index, player in enumerate(players):
            print(index, player)
        
        #On passe le format en int afin de garder l'index en entier exploitable
        tournament_index = self.get_valid_integer_input(
            "Numéro du tournoi : "
        )
        player_index = self.get_valid_integer_input(
            "Numéro du joueur : "
        )

        try:
            tournament = self.tournament_controller.add_player_to_tournament(
                tournament_index,
                player_index
            )
            print(f"Joueur ajouté au tournoi : {tournament}")

        except IndexError:
            print("Erreur : numéro de tournoi ou de joueur invalide.")

        except ValueError as error:
            print(f"Erreur : {error}")

    #Affichage la vue de suppression d'un joueur du tournoi
    def remove_player_from_tournament_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input(
            "Numéro du tournoi : "
        ) - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return

        if not tournament.players:
            print("Ce tournoi ne contient aucun joueur.")
            return

        for index, player in enumerate(tournament.players, start=1):
            print(index, player)

        player_index = self.get_valid_integer_input(
            "Numéro du joueur à retirer : "
        ) - 1

        try:
            player = self.tournament_controller.remove_player_from_tournament(
                tournament_index,
                player_index
            )
            print(f"Joueur retiré du tournoi : {player}")

        except IndexError:
            print("Erreur : numéro de joueur invalide.")    

    # Affichage de la vue de generation de round
    def generate_round_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments):
            print(index, tournament)
        
        tournament_index = self.get_valid_integer_input(
            "Numéro du tournoi : "
        )

        try:
            new_round = self.tournament_controller.generate_round(tournament_index)
            print(f"{new_round.name} généré avec succès.")

        except ValueError as error:
            print(f"Erreur : {error}")

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
    
    # Création et affichage de la vue de saisie de score de rounds
    def enter_round_results_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments):
            print(index, tournament)
        
        tournament_index = self.get_valid_integer_input(
            "Numéro du tournoi : "
        )

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return

        for index, tournament_round in enumerate(tournament.rounds, start=1):
            print(index, tournament_round)
        
        round_index = self.get_valid_integer_input(
            "Numéro du round : "
        ) - 1

        try:
            selected_round = self.tournament_controller.enter_round_results(
                tournament_index,
                round_index
            )
            print(f"Résultats enregistrés pour {selected_round.name}.")

        except IndexError:
            print("Erreur : numéro de tournoi ou de round invalide.")

        except ValueError as error:
            print(f"Erreur : {error}")
    
    # Affichage de la vue des détails des tournois
    def display_tournament_details_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input(
            "Numéro du tournoi : "
        ) - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return

        print(f"\nTournoi : {tournament.name}")
        print(f"Lieu : {tournament.place}")
        print(f"Dates : {tournament.start_date} → {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print(f"Nombre de joueurs : {len(tournament.players)}")
        print(f"Nombre de rounds : {len(tournament.rounds)}")

    # Affichage de la vue des joueurs des tournois
    def display_tournament_players_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input(
            "Numéro du tournoi : "
        ) - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return
        
        if not tournament.players:
            print("Ce tournoi ne contient aucun joueur")
            return

        print(f"\nJoueurs du tournoi : {tournament.name}")

        # sorted() est une méthode qui trie les élements d'une liste
        # key=lambda signifie que l'on trie les joueurs par l'att last_name 
        for player in sorted(tournament.players, key=lambda player: player.last_name):
            print(player)
    
    # Affichage de la vue des rounds des tournois
    def display_tournament_rounds_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input(
            "Numéro du tournoi : "
        ) - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return
        
        if not tournament.rounds:
            print("Ce tournoi ne contient aucun round")
            return

        print(f"\nRounds du tournoi : {tournament.name}")

        for tournament_round in tournament.rounds:
            print(f"\n{tournament_round.name}")
            print(f"Début : {tournament_round.start_time}")
            print(f"Fin : {tournament_round.end_time}")

            for match in tournament_round.matches:
                print(f"  - {match}")
    
    # Affichage de la vue du classement des tournois
    def display_tournament_ranking_view(self):
        tournaments = self.tournament_controller.get_tournaments()

        for index, tournament in enumerate(tournaments, start=1):
            print(index, tournament)

        tournament_index = self.get_valid_integer_input(
            "Numéro du tournoi : "
        ) - 1

        try:
            tournament = tournaments[tournament_index]

        except IndexError:
            print("Erreur : numéro de tournoi invalide.")
            return
        
        if not tournament.players:
            print("Ce tournoi ne contient aucun joueur")
            return

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