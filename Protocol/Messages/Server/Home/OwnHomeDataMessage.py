import json
from Utils.Writer import Writer

class OwnHomeDataMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 24101
        self.version = 1

    def encode(self):
        print('Loaded own home from server')
        self.player.LogicClientHome(self)
        self.player.LogicClientAvatar(self)
        self.writeVInt(10)