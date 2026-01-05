from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

from Protocol.Messages.Server.Social.FriendListMessage import FriendListMessage

class AskForPlayingFacebookFriendsMessage(Writer, Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self, crypter):
        FriendListMessage(self.client, self.player).Send(crypter)