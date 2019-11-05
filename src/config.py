import pygame

pygame.init()
pygame.font.init() 

font_game = pygame.font.SysFont('Comic Sans MS', 30)

width = 640
height = 480
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

def loadImage(name):
    return pygame.image.load("asset/" + name + ".gif").convert()

assetName = ['dinosaur small', 'dinosaur', 'door', 'Dungeontile1', 'gameover', 'guardLEFT', 'guardRIGHT', 'guardWOequipmentR', 'ivypillar', 'ivywall',
            'levelcomplete', 'mike invert', 'mike side', 'playerleft', 'playerright', 'moon', 'rampleft', 'rampright', 'small mike', 'spikeblock', 'spikes', 
            'spikes2', 'stars', 'stars2', 'stonefloor', 'stonefloor2', 'tile', 'tilebottom', 'tilebottom2', 'tilebottom3',  'tilebottom2dark', 'tiletop', 'tiletop2',
            'TotoMoving1', 'TotoMoving2', 'Totomoving3', 'TotoStill', 'sky', 'bullet', 'dungeon', 'menu']
            
assetLibrary = {}
for i in assetName:
    assetLibrary[i] = loadImage(i)








