from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

from Protocol.Messages.Server.Home.LeaderboardMessage import LeaderboardMessage

class GetLeaderboardMessage(Writer, Reader):

    def __init__(self, data, device):
        Reader.__init__(self, data)
        Writer.__init__(self, device)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        self.LeaderboardType = self.readVInt()
        self.LeaderboardInfo = self.readVInt()

    def process(self, crypter):
        LeaderboardMessage(self.client, self.player, self.LeaderboardType, self.LeaderboardInfo).Send(crypter)