from uuid import UUID
from models.player_action import PlayerAction
from models.progress import Progress


class BoardAction(PlayerAction):
    uuid: UUID  # uuid of the action
    player: int  # uid of the owning player
    progress: Progress  # progress of the units on the path

    def __init__(self, boardaction: dict):
        super().__init__(boardaction['src'], boardaction['dest'], boardaction['amount'])
        self.uuid = UUID(boardaction["uuid"])
        self.player = boardaction["player"]
        self.progress = Progress(boardaction["progress"])
