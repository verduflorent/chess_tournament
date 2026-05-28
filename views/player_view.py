class PlayerView:

    # Initialisation de PlayerView
    def __init__(self, player_controller):
        self.player_controller = player_controller

    # Creéation de la vue joueur
    def create_player_view(self):
        first_name = input("Prénom : ")
        last_name = input("Nom de famile : ")
        birth_date = input("Date de naissance (JJ-MM-AAAA) : ")
        national_id = input("Identifiant National : ")

        player = self.player_controller.create_player(
            first_name, last_name, birth_date, national_id
        )

        print(f"Joueur crée : {player}")

    # Affichage de la vue player
    def display_players_view(self):
        players = self.player_controller.get_players()

        for player in players:
            print(player)

    # Affichage de la vue de suppression de joueur
    def delete_player_view(self):
        players = self.player_controller.get_players()

        for index, player in enumerate(players, start=1):
            print(index, player)

        player_index = int(input("Numéro du joueur à supprimer : ")) - 1

        try:
            deleted_player = self.player_controller.delete_player(player_index)
            print(f"Joueur supprimé : {deleted_player}")

        except IndexError:
            print("Erreur : numéro de joueur invalide.")
