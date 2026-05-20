from models.player import Player


class PlayerController:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_player(
            self,
            first_name,
            last_name,
            birth_date,
            national_id
        ):
        
        player = Player(
            first_name,
            last_name,
            birth_date,
            national_id
        )

        self.db_manager.save_player(player)

        return player

    def get_players(self):

        return self.db_manager.get_players()

   