from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

class EndClientTurnMessage(Writer, Reader):

    def __init__(self, data, device):
        Reader.__init__(self, data)
        Writer.__init__(self, device)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.tickCheck = self.readVInt()
        if self.tickCheck != 0:
            self.commandID = self.readVInt()

    def process(self, crypter):
        pass