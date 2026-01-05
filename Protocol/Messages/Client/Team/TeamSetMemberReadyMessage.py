from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

from Protocol.Messages.Server.Team.TeamMessage import TeamMessage
from Protocol.Messages.Server.Team.TeamGameStartingMessage import TeamGameStartingMessage

class TeamSetMemberReadyMessage(Writer, Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self, crypter):
        TeamGameStartingMessage(self.client, self.player).Send(crypter)