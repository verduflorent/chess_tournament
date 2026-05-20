class PlayerView:
    def __init__(self, player_controller):
        self.player_controller = player_controller

    def create_player_view(self):
        first_name = input("Prénom : ")
        last_name = input("Nom de famile : ")
        birth_date = input("Date de naissance (JJ-MM-AAAA) : ")
        national_id = input("Identifiant National : ")

        player = self.player_controller.create_player(
            first_name,
            last_name,
            birth_date,
            national_id
        )

        print(f"Joueur crée : {player}")

    def display_players_view(self):
        players = self.player_controller.get_players()

        for player in players:
            print(player)