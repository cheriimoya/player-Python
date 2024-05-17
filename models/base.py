from dataclasses import dataclass

from models.position import Position


@dataclass
class Base:
    position: Position  # position of the base
    uid: int  # uid of the base
    player: int  # uid of the owning player
    population: int  # number of bits in the base
    level: int  # level of the base
    units_until_upgrade: int  # bits needed for until the next upgrade

    def __init__(self, base: dict):
        self.position = base["position"]
        self.uid = base["uid"]
        self.player = base["player"]
        self.population = base["population"]
        self.level = base["level"]
        self.units_until_upgrade = base["units_until_upgrade"]
