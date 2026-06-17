from datetime import datetime


class PlayerView:
    """Gere les affichages et saisies lies aux joueurs."""

    # Initialisation de PlayerView
    def __init__(self, player_controller):
        """Initialise la vue avec le controleur des joueurs."""
        self.player_controller = player_controller

    # Gestion des dates de naissances
    def get_valid_date_input(self, message):
        """Demande une date valide au format JJ/MM/AAAA."""
        while True:
            date_value = input(message)

            try:
                datetime.strptime(date_value, "%d/%m/%Y")
                return date_value

            except ValueError:
                print("Erreur : date invalide. Format attendu : JJ/MM/AAAA.")

    # Creéation de la vue joueur
    def create_player_view(self):
        """Affiche le formulaire de creation d'un joueur."""
        first_name = input("Prénom : ")
        last_name = input("Nom de famile : ")
        birth_date = self.get_valid_date_input(
            "Date de naissance (JJ/MM/AAAA) : "
        )
        national_id = input("Identifiant National : ")

        player = self.player_controller.create_player(
            first_name, last_name, birth_date, national_id
        )

        print(f"Joueur crée : {player}")

    # Affichage de la vue player
    def display_players_view(self):
        """Affiche la liste des joueurs."""
        players = self.player_controller.get_players()

        for player in players:
            print(player)

    # Affichage de la vue de suppression de joueur
    def delete_player_view(self):
        """Affiche le formulaire de suppression d'un joueur."""
        players = self.player_controller.get_players()

        for index, player in enumerate(players, start=1):
            print(index, player)

        player_index = int(input("Numéro du joueur à supprimer : ")) - 1

        try:
            deleted_player = self.player_controller.delete_player(player_index)
            print(f"Joueur supprimé : {deleted_player}")

        except IndexError:
            print("Erreur : numéro de joueur invalide.")

        except ValueError as error:
            print(f"Erreur : {error}")
