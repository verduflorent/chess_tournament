from models.tournament import Tournament

class TournamentController:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_tournament(
            self,
            name,
            place,
            description,
            start_date,
            end_date,
            total_rounds
        ):

        tournament = Tournament(
            name,
            place,
            description,
            start_date,
            end_date,
            total_rounds
        )

        self.db_manager.save_tournament(tournament)

        return tournament

    def get_tournaments(self):

        return self.db_manager.get_tournaments()

