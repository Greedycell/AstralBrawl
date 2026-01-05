from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

from Protocol.Messages.Server.Account.LoginOkMessage import LoginOkMessage
from Protocol.Messages.Server.Account.LoginFailedMessage import LoginFailedMessage
from Protocol.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage

class LoginMessage(Writer, Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self, crypter):
        LoginOkMessage(self.client, self.player).Send(crypter)
        OwnHomeDataMessage(self.client, self.player).Send(crypter)