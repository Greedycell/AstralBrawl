import json
from Utils.Writer import Writer

class LeaderboardMessage(Writer):

    def __init__(self, device, player, LeaderboardType, LeaderboardInfo):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 24403
        self.LeaderboardType = LeaderboardType
        self.LeaderboardInfo = LeaderboardInfo

    def encode(self):
        self.writeVInt(self.LeaderboardInfo)
        self.writeVInt(0)
        if self.LeaderboardType == 0:
        	self.writeString()
        else:
        	self.writeString("EN")

        if self.LeaderboardInfo == 0:
            self.writeVInt(1) # Players Count

            self.writeVInt(0) # High ID
            self.writeVInt(1) # Low ID
            self.writeVInt(1)
            self.writeVInt(0) # Player Trophies
            self.writeVInt(1)
            self.writeString("Astral")  # Player Name
            self.writeString("<c2aff00>O<c54ff00>b<c7fff00>j<ca9ff00>e<cd4ff00>c<cfefe00>t<cffff00> <cffd400>T<cffaa00>e<cff7f00>a<cff5500>m</c>") # Club Name
            self.writeVInt(1) # Player Level
            self.writeVInt(28)
            self.writeVInt(0)
            self.writeVInt(0)
        elif self.LeaderboardInfo == 1:
            self.writeVInt(1) # Players Count

            self.writeVInt(0) # High ID
            self.writeVInt(1) # Low ID
            self.writeVInt(1)
            self.writeVInt(0) # Player Trophies
            self.writeVInt(1)
            self.writeString("Astral")  # Player Name
            self.writeString("<c2aff00>O<c54ff00>b<c7fff00>j<ca9ff00>e<cd4ff00>c<cfefe00>t<cffff00> <cffd400>T<cffaa00>e<cff7f00>a<cff5500>m</c>") # Club Name
            self.writeVInt(1) # Player Level
            self.writeVInt(28)
            self.writeVInt(0)
            self.writeVInt(0)
        elif self.LeaderboardInfo == 2:
            self.writeVInt(1) # Clubs Count

            self.writeVInt(0) # Club High ID
            self.writeVInt(1) # Club Low ID
            self.writeVInt(1)
            self.writeVInt(0) # Club Trophies
            self.writeVInt(2)
            self.writeString("Greedycell") # Club Name
            self.writeVInt(5) # Club Members Count
            self.writeVInt(8) # Club Badge
            self.writeVInt(5) # Club Name Color
      
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeString("EN")