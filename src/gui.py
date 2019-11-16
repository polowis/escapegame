
"""
author: Polowis
Contain some useful user interface grids. 
"""

from assets import *


def text(message, color, text_x, text_y, text_width, text_height, size="small"):
    """display text to the screen"""
    text_rect = pygame.Rect(text_x, text_y, text_width, text_height)
    text_rect.center = ((text_x+(text_width/2)), text_y+(text_height/2))
    screen.blit(font_game.render(message, False, color), text_rect)

def button(message, color, text_x, text_y, text_width, text_height, callback):
    """display button to the screen"""
    text_rect = pygame.Rect(text_x, text_y, text_width, text_height)
    text_rect.center = ((text_x+(text_width/2)), text_y+(text_height/2))
    screen.blit(font_game.render(message, False, color), text_rect)
    callback()

