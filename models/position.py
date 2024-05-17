from dataclasses import dataclass


@dataclass
class Position:
    x: int  # x coordinate
    y: int  # y coordinate
    z: int  # z coordinate

    def __init__(self, position: dict):
        self.x = position["x"]
        self.y = position["y"]
        self.z = position["z"]

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
