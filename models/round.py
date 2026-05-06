from models.match import Match
from datetime import datetime

class Round:
    def __init__(self, name, matches = " ", start_time = datetime(now), end_time=" "):
        self.name = name
        self.matches = matches
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Round : {self.name} / Start : {self.start_time} End : {self.end_time}"