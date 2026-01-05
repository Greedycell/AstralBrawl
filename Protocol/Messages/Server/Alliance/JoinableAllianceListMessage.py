import json
from Utils.Writer import Writer

class JoinableAllianceListMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 24304

    def encode(self):
        self.writeVInt(1) # How many clubs

        self.writeLong(0, 1, 'Int')
        self.writeString('Greedycell') # Club Name
        self.writeDataReference(8, 1) # Badge ID
        self.writeVInt(1) # Type
        self.writeVInt(1) # How many members
        self.writeVInt(0) # Trophies
        self.writeVInt(0) # Required Trophies
        self.writeDataReference(0, 0)
        self.writeString('International') # Region
        self.writeVInt(0)
        self.writeVInt(0)