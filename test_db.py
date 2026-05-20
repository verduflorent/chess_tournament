from database.db_manager import DatabaseManager
from models.player import Player

db_manager = DatabaseManager()

player = Player(
    "Thierry", 
    "Goleau", 
    "20/05/1987", 
    "A111548"
    )

db_manager.save_player(player)