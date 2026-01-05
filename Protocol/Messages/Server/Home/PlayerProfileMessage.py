import json
from Utils.Writer import Writer

class PlayerProfileMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 24113
        self.version = 1

    def encode(self):
        self.writeVInt(0) #HighID
        self.writeVInt(1) #LowID
        self.writeString("Astral")
        self.writeVInt(0)

        self.writeVInt(1)

        self.writeVInt(16)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(9999)
        self.writeVInt(9999)
        self.writeVInt(10)

        self.writeVInt(11)

        self.writeVInt(0)
        self.writeVInt(0) # Total victories

        self.writeVInt(0)
        self.writeVInt(0) # Player experience

        self.writeVInt(0)
        self.writeVInt(0) # Trophies

        self.writeVInt(0)
        self.writeVInt(0) # Highest trophies

        self.writeVInt(5)
        self.writeVInt(1) # Brawlers count

        self.writeVInt(6)
        self.writeVInt(0) # Unknown

        self.writeVInt(7)
        self.writeVInt(0) # Profile icon

        self.writeVInt(8)
        self.writeVInt(0) # Solo victories

        self.writeVInt(9)
        self.writeVInt(0) # Best robo rumble time

        self.writeVInt(10)
        self.writeVInt(0) # Best time as big brawler

        self.writeVInt(11)
        self.writeVInt(0) # Duo victories

        self.writeVInt(0)
        self.writeVInt(0)