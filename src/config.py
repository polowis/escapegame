"""
When run the application, this is where the code will be executed first. 
This part of code responsible for creating basic layout and information for the game
Such as create window, loading all images from assets folders, set font size.
"""
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

assetName = ['dinosaur small', 'dinosaur', 'door', 'Dungeontile1', 'guardLEFT', 'guardRIGHT', 'guardWOequipmentR', 'ivypillar', 'ivywall',
             'mike invert', 'mike side', 'playerleft', 'playerright','small mike', 'spikeblock', 'spikes', 
            'spikes2', 'stonefloor', 'stonefloor2', 'tile', 'tilebottom', 'tilebottom2', 'tilebottom3',  'tilebottom2dark', 'tiletop', 'tiletop2',
             'sky', 'bullet', 'dungeon', 'menu', 'key']
            
assetLibrary = {}
for i in assetName:
    assetLibrary[i] = loadImage(i)








