from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

from Protocol.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage

class CancelMatchmakingMessage(Writer, Reader):

    def __init__(self, data, device):
        Reader.__init__(self, data)
        Writer.__init__(self, device)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self, crypter):
        OwnHomeDataMessage(self.client, self.player).Send(crypter)