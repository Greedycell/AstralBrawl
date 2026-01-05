from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

class SetDeviceTokenMessage(Writer, Reader):

    def __init__(self, data, device):
        Reader.__init__(self, data)
        Writer.__init__(self, device)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self, crypter):
        pass