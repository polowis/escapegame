from assets import *

def messageScreen(message, color, dislay=0, size="small"):
    lop = 1

def button(message, color, button_x, button_y, button_width, button_height, size="small"):
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    button_rect.center = ((button_x+(button_width/2)), button_y+(button_height/2))
    screen.blit(font_game.render(message, False, color), button_rect)

