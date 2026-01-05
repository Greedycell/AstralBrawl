import json
from Utils.Writer import Writer

class AllianceDataMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 24301

    def encode(self):
        self.writeVInt(0)
        self.writeLong(0, 1, 'Int') # Club ID
        self.writeString('Greedycell') # Club name
        self.writeLong(8, 1, 'VInt') # Badge ID
        self.writeVInt(3) # Club Type | 1 = open, 2 = invite only, 3 = closed
        self.writeVInt(1) # Club Members Count
        self.writeVInt(0) # Trophies
        self.writeVInt(0) # Required Trophies
        self.writeDataReference(0, 0)
        self.writeString('The official club of Greedycell!')

        self.writeVInt(1) # How many members

        self.writeLong(0, 1, 'Int') # Member ID
        self.writeString('Astral') # Member Name
        self.writeVInt(2) # Member Role | 0 = Non-Member, 1 = Member, 3 = Elder, 4 = Co-Leader, 2 = Leader
        self.writeVInt(0)
        self.writeVInt(0) # Member Trophies
        self.writeVInt(2) # Player Status | 0 = last online 1 hour ago, 1 = battling, 2 = menu, 4 = matchmaking, 6 = last online 1 month ago, 7 = spectating, 8 = practicing
        self.writeVInt(0)
        self.writeVInt(28)#100)
        self.writeVInt(28000000 + 20) # 20 = Player Icon
        #self.writeVInt(43000000 + 16) # 16 = Name Color