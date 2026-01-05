import json
from Utils.Writer import Writer

class BattleEndMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 23456

    def encode(self):
        self.writeVInt(2) #Battle End Screen Type
        self.writeVInt(1) #Rank Score
            
        self.writeVInt(0) #Battle Tokens 
        self.writeVInt(0) #Trophies Value
        self.writeVInt(0) #Doubled Tokens
        self.writeVInt(0) #Token Doubler Remaining
        self.writeVInt(0) #Unknown
        self.writeVInt(32) #Type (Capped XP, Star Token, Capped Tokens)
        self.writeVInt(1) #End Screen Players

        self.writeString('Astral') #Your Name
        self.writeVInt(1)  
        self.writeVInt(16) # CsvID
        self.writeVInt(0)  # BrawlerID
        self.writeVInt(29) # CsvID
        self.writeVInt(0)  
        self.writeVInt(0) #Brawler Trophies
        self.writeVInt(10) #Brawler Power Level
        self.writeVInt(0)  #Unknown
        
        self.writeVInt(0)  #Unknown
        self.writeVInt(0)  #Unknown
        self.writeVInt(0)  #Unknown
        self.writeVInt(28) #Unknown
        self.writeVInt(0)  #Unknown