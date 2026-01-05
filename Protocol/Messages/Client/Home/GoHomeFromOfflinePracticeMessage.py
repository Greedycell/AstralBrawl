from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

from Protocol.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage

class GoHomeFromOfflinePracticeMessage(Writer, Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self, crypter):
        OwnHomeDataMessage(self.client, self.player).Send(crypter)