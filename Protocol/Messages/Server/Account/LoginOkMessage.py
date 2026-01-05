import json
from Utils.Writer import Writer

class LoginOkMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20104
        self.version = 4

    def encode(self):
        self.writeInt(0) # HighID
        self.writeInt(1) # LowID
        self.writeInt(0) # HighID
        self.writeInt(1) # LowID
        self.writeString('JustAToken') # Token
        self.writeString()
        self.writeString()
        self.writeInt(11)
        self.writeInt(112)
        self.writeInt(1)
        self.writeString("integration")
        self.writeInt(0) #1
        self.writeInt(0) #1
        self.writeInt(0) #61
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeVInt(0)