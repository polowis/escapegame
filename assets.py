
from character import *

class Map1():
    def __init__(self):
        self.tiles = []
        self.ramps = []
        self.background = []
        self.speed = 2
        self.door = (19*32,26*16)
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
            "40000000000000000000",
            "40000000000000000000",
            "40000000000000000000",
            "40000000000000000000",
            "40000000000000000000",
            "40000000000000000000",
            "40000000000000000000",
            "40000000000000000000",
            "40000000000000000330",
            "40000000000000000440",
            "40000000000000033440",
            "40000000000333344440",
            "40000003300444444440",
            "40000000000444444440",
            "40033000000444444440",
            "40000000000444444440",
            "40000003333444444440",
            "40000004444444444440",
            "43333334444444444444",
            "44444444444444444444",
        ]
        self.spikeMonsters = []

    def draw(self):
        x = 0
        y = 0
        for row in self.map:
            for key in row:
                if key == "3":
                    tile_list.append(Tile((x,y,), 'tiletop'))
                    self.tiles.append(Tile((x, y), 'tiletop'))
                if key == "4":
                    tile_list.append(Tile((x,y,), 'tilebottom3'))
                    self.tiles.append(Tile((x, y), 'tilebottom3'))
                if key == '5':
                    tile_list.append(Ramp((x, y), 'right', 'rampright'))
                x += 32
            y += 16
            x = 0
        a = 0

        
        spikemonster = Spike(50, 360, 'x', 2)
        spikemonster_list.append(spikemonster)
        self.spikeMonsters.append(spikemonster)

        #Monster(40,370,"dinosaur","dinosaur small",27,29)
       
class Map2():
    def __init__(self):
        self.tiles = []
        self.spikemonster = []
        self.monster = []
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
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "0000000300000030000",
            "00000004444444400000",
            "00000300000000030000",
            "00000000000000003000",
            "00003000000000000300",
            "00000000000000000000",
            "33330000000000000033",
            "44440000000000000044",  
        ]
    
    def draw(self):
        x = 0
        y = 0
        for row in self.map:
            for key in row:
                if key == "3":
                    tile_list.append(Tile((x,y,), 'tiletop'))
                    self.tiles.append(Tile((x, y), 'tiletop'))
                if key == "4":
                    tile_list.append(Tile((x,y,), 'tilebottom3'))
                    self.tiles.append(Tile((x, y), 'tilebottom3'))
                if key == '5':
                    tile_list.append(Ramp((x, y), 'right', 'rampright'))
                x += 32
            y += 16
            x = 0
        spikemonster = Spike(200, 450, "y", -80)
        spikemonster_list.append(spikemonster)
        self.spikemonster.append(spikemonster)
        monster = Monster(9*32,20*16,"dinosaur","dinosaur small",27,29)
        self.monster.append(monster)
