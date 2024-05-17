from models.base import Base
from models.board_action import BoardAction
from models.game import Game
from models.game_config import GameConfig


class GameState:
    actions: list[BoardAction]
    bases: list[Base]
    config: GameConfig
    game: Game

    @classmethod
    def fromAttributes(cls, actions: list[BoardAction], bases: list[Base], config: GameConfig, game: Game):
        gameState = {"actions": actions, "bases": bases, "config": config, "game": game}
        return cls(gameState)

    def __init__(self, gameState: dict) -> None:
        self.actions = gameState["actions"]
        self.bases = gameState["bases"]
        self.config = gameState["config"]
        self.game = gameState["game"]
