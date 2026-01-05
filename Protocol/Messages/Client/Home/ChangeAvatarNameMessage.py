from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

from Protocol.Commands.Server.Home.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand

class ChangeAvatarNameMessage(Writer, Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self, crypter):
        LogicChangeAvatarNameCommand(self.client, self.player).Send(crypter)