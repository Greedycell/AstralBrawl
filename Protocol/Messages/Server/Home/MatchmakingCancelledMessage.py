import json
from Utils.Writer import Writer

class MatchmakingCancelledMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20406

    def encode(self):
        pass