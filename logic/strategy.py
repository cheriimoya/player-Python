from typing import List, Tuple

from logic.kd_tree import KDTree
from models.base import Base
from models.game_state import GameState
from models.player_action import PlayerAction


def getdistance(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> int:
    return int(((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5)


def get_base_distance(base1: Base, base2: Base) -> int:
    return getdistance(base1.position.x, base1.position.y, base1.position.z, base2.position.x, base2.position.y,
                       base2.position.z)


class OwnState:

    def __init__(self, gamestate: GameState):
        self.unoccupied_bases = [base for base in gamestate.bases if not base.player]
        self.unoccupied_bases_kd_tree = KDTree([[base.position.x, base.position.y, base.position.z, base] for base in self.unoccupied_bases], 3)
        self.occupied_bases = [base for base in gamestate.bases if base.player and base.player != gamestate.game.player]
        self.occupied_kd_tree = KDTree([[base.position.x, base.position.y, base.position.z, base] for base in self.occupied_bases], 3)
        self.own_bases = [base for base in gamestate.bases if base.player == gamestate.game.player]
        print("own_bases", self.own_bases)
        self.own_kd_tree = KDTree([[base.position.x, base.position.y, base.position.z, base] for base in self.own_bases], 3)


    def get_no_brainers(self) -> List[Tuple[Base, Base]]:
        no_brainers = []

        for unoccupied_base in self.unoccupied_bases:
            nearest_own = self.own_kd_tree.get_nearest([unoccupied_base.position.x, unoccupied_base.position.y, unoccupied_base.position.z])
            nearest_occupied = self.occupied_kd_tree.get_nearest([unoccupied_base.position.x, unoccupied_base.position.y, unoccupied_base.position.z])
            if nearest_own is None:
                continue
            if nearest_occupied is None:
                continue

            nearest_own = nearest_own[1]
            nearest_occupied = nearest_occupied[1]


            print("kd-res", nearest_own, nearest_occupied)

            if getdistance(nearest_own[0], nearest_own[1], nearest_own[2], unoccupied_base.position.x, unoccupied_base.position.y, unoccupied_base.position.z) < getdistance(nearest_occupied[0], nearest_occupied[1], nearest_occupied[2], unoccupied_base.position.x, unoccupied_base.position.y, unoccupied_base.position.z):
                no_brainers.append((unoccupied_base, nearest_own[3]))
        return no_brainers


    def get_nearest_bases(self) -> list[tuple[int, Base, Base]]:
        distances_between_bases = [(get_base_distance(o, u), o, u) for u in self.unoccupied_bases for o in self.own_bases]
        return sorted(distances_between_bases, key=lambda x: x[0])



def decide(gamestate: GameState) -> List[PlayerAction]:
    print("Deciding")
    print(gamestate)
    own_state = OwnState(gamestate)

    actions = []

    no_brainers = own_state.get_no_brainers()

    for unoccupied_base, nearest_own in no_brainers:
        if nearest_own.population == 0:
            continue
        actions.append(PlayerAction(nearest_own.uid, unoccupied_base.uid, 1))
        nearest_own.population -= 1

    nearest_bases = own_state.get_nearest_bases()

    for nearest_base in nearest_bases:
        if nearest_base[1].population == 0:
            continue
        actions.append(PlayerAction(nearest_base[1].uid, nearest_base[2].uid, 1))
        nearest_base[1].population -= 1


    for occupied in own_state.occupied_bases:
        own = own_state.own_kd_tree.get_nearest([occupied.position.x, occupied.position.y, occupied.position.z])
        if not own or own[3].population == 0:
            continue
        own = own[3]
        actions.append(PlayerAction(own.uid, occupied.uid, 1))
        own.population -= 1

    return actions
