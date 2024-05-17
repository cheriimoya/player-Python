from dataclasses import dataclass


@dataclass
class Game:
    uid: int  # uid of game
    tick: int  # tick in game
    player_count: int  # number of players
    remaining_players: int  # number of players remaining
    player: int  # uid of your player


    def __init__(self, game: dict):
        self.uid = game["uid"]
        self.tick = game["tick"]
        self.player_count = game["player_count"]
        self.remaining_players = game["remaining_players"]
        self.player = game["player"]
