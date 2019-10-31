
from character import *

class Map1():
    def __init__(self):
        self.tiles = []
        self.ramps = []
        self.map = ["00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000330",
            "00000000000000000440",
            "00000000000000033440",
            "00000000000333344440",
            "00000003300444444440",
            "00000000000444444440",
            "00033000000444444440",
            "00000000000444444440",
            "00000003333444444440",
            "00000004444444444440",
            "33333334444444444444",
            "44444444444444444444",
        ]
        self.spikeMonsters = []

    def draw(self):
        x = 0
        y = 0
        for row in self.map:
            for key in row:
                if key == "3":
                    self.tiles.append(Tile((x,y,), 'tiletop'))
                if key == "4":
                    self.tiles.append(Tile((x,y,), 'tilebottom3'))
                if key == '5':
                    self.ramps.append(Ramp((x, y), 'right', 'rampright'))
                x += 32
            y += 16
            x = 0
        a = 0
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)
        
        spikemonster = Spike(32, 360, 'x', 2)
        self.spikeMonsters.append(spikemonster)
       
        