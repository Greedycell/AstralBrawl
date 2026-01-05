from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

from Protocol.Messages.Server.Home.BattleEndMessage import BattleEndMessage

class AskForBattleEndMessage(Writer, Reader):

    def __init__(self, data, device):
        Reader.__init__(self, data)
        Writer.__init__(self, device)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self, crypter):
        BattleEndMessage(self.client, self.player).Send(crypter)