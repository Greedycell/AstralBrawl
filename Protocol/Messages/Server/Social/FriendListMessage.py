import json
from Utils.Writer import Writer

class FriendListMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20105

    def encode(self):
        self.writeInt(1)
        self.writeInt(1)

        self.writeInt(1)
        self.writeInt(1)

        self.writeString("BrawlStarsPro69")
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeVint(1)
        self.writeVint(10)

        self.writeString()
        self.writeInt(0)

        self.writeVint(0)

        self.writeString()
        self.writeVint(28)
        self.writeVint(11)