import json
from Utils.Writer import Writer

class TeamLeftMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 24125

    def encode(self):
        self.writeVInt(0)