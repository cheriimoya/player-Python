from dataclasses import dataclass

from models.base import Base
from models.board_action import BoardAction
from models.game import Game
from models.game_config import GameConfig


@dataclass
class GameState:
    actions: list[BoardAction]
    bases: list[Base]
    config: GameConfig
    game: Game

    def __init__(self, gameState: dict) -> None:
        self.actions = [BoardAction(a) for a in  gameState["actions"]]
        self.bases = [Base(b) for b in gameState["bases"]]
        self.config = GameConfig(gameState["config"])
        self.game = Game(gameState["game"])
