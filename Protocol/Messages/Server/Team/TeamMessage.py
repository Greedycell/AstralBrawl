import json
from Utils.Writer import Writer

class TeamMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 24124

    def encode(self):
        self.writeVInt(1) #mode
        self.writeByte(0)
        self.writeVInt(1)
        self.writeInt(0)
        self.writeInt(1) #teamid
        self.writeVInt(0)
        self.writeByte(0)
        self.writeByte(0)
        self.writeVInt(0)
        
        self.writeVInt(15)
        self.writeVInt(7) # mapid
        
        self.writeVInt(1)
        
        self.writeByte(1)
        self.writeInt(0) #HighID
        self.writeInt(1) #LowID
        self.writeString("<c2>Astral</c>")
        self.writeVInt(3)
        
        self.writeVInt(16)
        self.writeVInt(5) # selected_brawler
        
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3) #Playerstate
        self.writeVInt(0) # ready (0 = not ready, 1 = ready)
        
        self.writeByte(0)
        self.writeVInt(0)
        
        self.writeVInt(0)      
        
        self.writeVInt(0)