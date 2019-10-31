from config import * 

global lists 
lists = []
class Character:
    def __init__(self, x, y):
        self.image = assetLibrary['mikenewright']
        self.rect = pygame.Rect(x, y, 16, 30)
        self.jump = 0
        self.keyRelease = True
        self.gameOver = False
        self.fall = False
    
    def move(self, direction_x, direction_y, tiles):
        """Move player"""
        if direction_x != 0:
            if(self.rect.left + direction_x) < 640 and (self.rect.right + direction_x) > 16:
                self.moveForward(direction_x, 0, tiles)
                
        if direction_y != 0:
            if(self.rect.top + direction_y) > 0:
                if(self.rect.bottom + direction_y) < screen.get_height() +2:
                    self.moveForward(0, direction_y, tiles)
    
        if direction_x > 0:
            self.image = assetLibrary['mikenewright']

        if direction_x < 0:
            self.image = assetLibrary['mikenewleft']

    def moveForward(self, direction_x, direction_y, tiles):
        """"""
        self.rect.x += direction_x
        self.rect.y += direction_y
        
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if direction_x > 0:
                    self.rect.right = tile.rect.left
                elif direction_x < 0:
                    self.rect.left = tile.rect.right
                elif direction_y > 0:
                    self.rect.bottom = tile.rect.top
                    self.jump = 0
                    self.keyRelease = False
                elif direction_y < 0:
                    self.rect.top = tile.rect.bottom
    
    def handle_input(self, map_level):
        """Handle key input"""
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2,0, map_level.tiles)
        if key[pygame.K_RIGHT]:
            player.move(2,0, map_level.tiles)
        if key[pygame.K_UP]:
            if self.keyRelease: 
                if self.jump < 20:
                    self.move(0,-5, map_level.tiles)
                    self.jump += 1 
        if self.rect.bottom < 480:
                self.move(0,2.5, map_level.tiles)
        if key[pygame.K_UP] == False:
            self.keyRelease = True

class Tile():
    def __init__(self, position, image_name):
        self.rect = pygame.Rect(position[0], position[1], 32, 16)
        self.image = assetLibrary[image_name]

class Ramp():
    def __init__(self, position, slope_direction, image):
        self.rect = pygame.Rect(position[0], position[1], 32, 32)
        self.slope = self.slope_direction
        self.image = assetLibrary[image]
        
class Monster():
    def __init__(self, pos_x, pos_y, image_r, image_l, rect_r, rect_l):
        self.direction = 1

class Spike():
    def __init__(self, pos_x, pos_y, direction, speed):
        lists.append(self)
        self.image = assetLibrary['spikeblock']
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 21, 21)
        self.speed = speed
        self.direction = direction

    def move(self, x, y, current_map):
        if x != 0:
            self.moveForward(x, 0, current_map)
        if y != 0:
            self.moveForward(0, y, current_map)

    def moveForward(self, dir_x, dir_y, current_map):
        self.rect.x += dir_x
        self.rect.y += dir_y
        for tile in current_map:
            if self.rect.colliderect(tile.rect):
                if dir_x > 0:
                    self.rect.right = tile.rect.left
                    self.speed = - self.speed
                elif dir_x < 0:
                    self.rect.left = tile.rect.right
                    self.speed = -self.speed
                elif dir_y > 0:
                    self.rect.bottom = tile.rect.top
                    self.speed = -self.speed
                elif dir_y < 0:
                    self.rect.top = tile.rect.bottom
                    self.speed = -self.speed


player = Character(32, 370)