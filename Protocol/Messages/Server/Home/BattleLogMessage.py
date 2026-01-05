import json
from Utils.Writer import Writer

class BattleLogMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 23458

    def encode(self):
        self.writeVInt(1)
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeBool(False)
        
        self.writeVInt(0)
        
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeVInt(1)
        
        self.writeVInt(0)
        self.writeInt(0)
        self.writeInt(0)        
        self.writeVInt(0)
        self.writeBool(False)
        self.writeInt(0)
        self.writeInt(0) 

        self.writeVInt(0)       

        self.writeVInt(0)
        self.writeVInt(0)