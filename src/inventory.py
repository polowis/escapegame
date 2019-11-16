"""
This is player's invetory, allow player to keep the key for the next map
"""
class Inventory:
    def __init__(self, player):
        self.player = player
        self.keyList = []

    def collectKey(self, key):
        return self.keyList.append(key)
    
    def keyIsAvailable(self, key):
        for i in self.keyList:
            if i == key:
                return True
    
