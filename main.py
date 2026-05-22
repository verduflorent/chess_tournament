from database.db_manager import DatabaseManager

from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

from views.player_view import PlayerView
from views.tournament_view import TournamentView

db_manager = DatabaseManager()
player_controller = PlayerController(db_manager)
tournament_controller = TournamentController(db_manager)
player_view = PlayerView(player_controller)
tournament_view = TournamentView(
    tournament_controller,
    player_controller
    )

#Le while True signifie que tant que l'utilisateur ne quitte pas en chosissant le break, le menu s'affiche
while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Créer un joueur")
    print("2. Afficher les joueurs")
    print("3. Créer un tournoi")
    print("4. Afficher les tournois")
    print("5. Ajouter un joueur a un tournoi")
    print("0. Quitter")

    choice = input("Votre choix : ")

    if choice == "1":
        player_view.create_player_view()

    elif choice == "2":
        player_view.display_players_view()

    elif choice == "3":
        tournament_view.create_tournament_view()

    elif choice == "4":
        tournament_view.display_tournaments_view()
    
    elif choice == "5":
        tournament_view.add_player_to_tournament_view()

    elif choice == "0":
        print("Au revoir !")
        break

    else:
        print("Choix invalide.")