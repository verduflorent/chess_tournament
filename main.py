from models.player import Player
from models.match import Match
from models.round import Round

player1 = Player("Jean","Duzboub","06/07/1992","A111")
player2 = Player("Alice","Lachoin","24/12/1987","A112")

match1 = Match(player1, player2)

round1 = Round("Test")

round1.add_match(match1)

print(round1)

round1.end_round()

print(round1)