import json
from Utils.Writer import Writer

class TeamGameStartingMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 24130

    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(23)
        self.writeVInt(0)