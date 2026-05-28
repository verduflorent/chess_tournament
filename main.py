from database.db_manager import DatabaseManager

from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

from views.player_view import PlayerView
from views.tournament_view import TournamentView


# =========================
# INITIALISATION MVC
# =========================

db_manager = DatabaseManager()

player_controller = PlayerController(db_manager)
tournament_controller = TournamentController(db_manager)

player_view = PlayerView(player_controller)

tournament_view = TournamentView(
    tournament_controller,
    player_controller
)


# =========================
# MENUS
# =========================

def player_menu():

    while True:

        print("\n=== GESTION JOUEURS ===")
        print("1. Créer un joueur")
        print("2. Afficher les joueurs")
        print("0. Retour")

        choice = input("Votre choix : ")

        match choice:

            case "1":
                player_view.create_player_view()

            case "2":
                player_view.display_players_view()

            case "0":
                break

            case _:
                print("Choix invalide.")


def tournament_menu():

    while True:

        print("\n=== GESTION TOURNOIS ===")
        print("1. Créer un tournoi")
        print("2. Afficher les tournois")
        print("3. Ajouter un joueur à un tournoi")
        print("4. Générer un round")
        print("5. Saisir les résultats d'un round")
        print("0. Retour")

        choice = input("Votre choix : ")

        match choice:

            case "1":
                tournament_view.create_tournament_view()

            case "2":
                tournament_view.display_tournaments_view()

            case "3":
                tournament_view.add_player_to_tournament_view()

            case "4":
                tournament_view.generate_round_view()

            case "5":
                tournament_view.enter_round_results_view()

            case "0":
                break

            case _:
                print("Choix invalide.")


def reports_menu():

    while True:

        print("\n=== RAPPORTS ===")
        print("1. Afficher les détails d'un tournoi")
        print("2. Afficher les joueurs d'un tournoi")
        print("3. Afficher les rounds et matchs d'un tournoi")
        print("4. Afficher le classement d'un tournoi")
        print("0. Retour")

        choice = input("Votre choix : ")

        match choice:

            case "1":
                tournament_view.display_tournament_details_view()

            case "2":
                tournament_view.display_tournament_players_view()

            case "3":
                tournament_view.display_tournament_rounds_view()
            
            case "4":
                tournament_view.display_tournament_ranking_view()

            case "0":
                break

            case _:
                print("Choix invalide.")


# =========================
# MENU PRINCIPAL
# =========================

while True:

    print("\n=== MENU PRINCIPAL ===")
    print("1. Gestion des joueurs")
    print("2. Gestion des tournois")
    print("3. Rapports")
    print("0. Quitter")

    choice = input("Votre choix : ")

    match choice:

        case "1":
            player_menu()

        case "2":
            tournament_menu()

        case "3":
            reports_menu()

        case "0":
            print("Au revoir !")
            break

        case _:
            print("Choix invalide.")