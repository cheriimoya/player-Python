from dataclasses import dataclass

from models.base_level import BaseLevel


@dataclass
class PathsConfig:
    grace_period: int  # time until groups of bits take damage
    death_rate: int  # time until groups of bits take damage

    def __init__(self, pathsconfig: dict):
        self.grace_period = pathsconfig["grace_period"]
        self.death_rate = pathsconfig["death_rate"]


@dataclass
class GameConfig:
    base_levels: list[BaseLevel]  # all available base levels
    paths: PathsConfig  # settings containing paths between bases

    def __init__(self, gameconfig: dict) -> None:
        self.base_levels = [BaseLevel(l) for l in gameconfig["base_levels"]]
        self.paths = PathsConfig(gameconfig["paths"])
