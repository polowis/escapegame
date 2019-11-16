from config import * 
from inventory import *

global spikemonster_list
global monster_list
global tile_list
global sky_list
global level_1
global bullet_list
global boss_list
spikemonster_list = []
monster_list = []
tile_list = []
bullet_list = []
boss_list = []

class Character:
    def __init__(self, x, y):
        self.image = assetLibrary['playerright']
        self.rect = pygame.Rect(x, y, 16, 30)
        self.face = 'right'
        self.jump = 0
        self.keyRelease = True
        self.gameOver = False
        self.fall = False
        self.state = "start"
        self.coin = 0
        self.key = ""
        self.damage = 5

    def shoot(self, direction):
        """player shoot"""
        #create Bullet
        Bullet(direction)
        
    def getPlayerPosition(self):
        """return player position"""
        return self.rect
        
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
            self.image = assetLibrary['playerright']
            self.face = 'right'

        if direction_x < 0:
            self.image = assetLibrary['playerleft']
            self.face = 'left'

    def moveForward(self, direction_x, direction_y, tiles):
        """move player"""
        self.rect.x += direction_x
        self.rect.y += direction_y
        """check if player hits the block"""
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

    def scrollX(self, screenSurf, offsetX):
        width, height = screenSurf.get_size()
        copySurf = screenSurf.copy()
        screenSurf.blit(copySurf, (offsetX, 0))
        if offsetX < 0:
            screenSurf.blit(copySurf, (width + offsetX, 0), (0, 0, -offsetX, height))
        else:
            screenSurf.blit(copySurf, (0, 0), (width - offsetX, 0, offsetX, height))

    def handle_input(self, map_level):
        """Handle key input"""
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2,0, map_level.tiles)
            self.scrollX(screen, -8)
        if key[pygame.K_RIGHT]:
            player.move(2,0, map_level.tiles)
            self.scrollX(screen, 8)
        if key[pygame.K_UP]:
            if self.keyRelease: 
                if self.jump < 20:
                    self.move(0,-5, map_level.tiles)
                    self.jump += 1
        
        if key[pygame.K_SPACE]:
            if self.face == 'right':
                self.shoot(2)
            if self.face == "left":
                self.shoot(-2)

        if self.rect.bottom < 480:
                self.move(0,2.5, map_level.tiles)
        if key[pygame.K_UP] == False:
            self.keyRelease = True

    def die(self):
        """return true if player dies"""
        for spikemonsters in spikemonster_list:
            if self.rect.colliderect(spikemonsters.rect):
                return True
        for monster in monster_list:
            if self.rect.colliderect(monster.rect):
                return True
        if self.rect.bottom >= 480:
            return True

class Bullet:
    """create bullet object"""
    def __init__(self, direction):
        bullet_list.append(self)
        self.rect = pygame.Rect(player.rect.x, player.rect.y + 5, 21, 21)
        self.direction = direction
        """get player's position and update the bullet"""

    def kill(self):
        self.rect.x += 1000
        self.rect.y += 1000
    

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
    def __init__(self, pos_x, pos_y, image_r, image_l, rect_x, rect_y):
        monster_list.append(self)
        self.direction = 1
        self.image = assetLibrary[image_l]
        self.imageL = image_l
        self.imageR = image_r
        self.rect = pygame.Rect(pos_x, pos_y, rect_x, rect_y)
        self.health = 100
    
    def move(self, direction_x, direction_y, tiles):
        """Monster moves"""
        if direction_x != 0:
            if(self.rect.left + direction_x) > 0:
                if(self.rect.right + direction_x) < 640:
                    if direction_x > 0:
                        self.moveForward(direction_x, 0, tiles)
                        self.image = assetLibrary[self.imageL]
                    if direction_x < 0:
                        self.moveForward(direction_x, 0, tiles)
                        self.image = assetLibrary[self.imageR]
            if(self.rect.left + direction_x <= 0) or (self.rect.left + direction_x >= 640):
                self.direction = -self.direction

        if direction_y != 0:
            self.moveForward(direction_x, direction_y, tiles)

    def moveForward(self, dir_x, dir_y, tiles):
        self.rect.x += dir_x
        self.rect.y += dir_y
        # if target collides, change direction. 
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if dir_x > 0:
                    self.rect.right = tile.rect.left
                    self.direction = -self.direction
                elif dir_x < 0:
                    self.rect.left  = tile.rect.right
                    self.direction = -self.direction
                if dir_y > 0:
                    self.rect.bottom = tile.rect.top
                if dir_y < 0:
                    self.rect.top = tile.rect.bottom
    def die(self):
        if self.health <= 0:
            return True
        
    def kill(self):
        self.rect.x += 1000
        self.rect.y += 1000


class Spike():
    def __init__(self, pos_x, pos_y, direction, speed):
        self.image = assetLibrary['spikeblock']
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 21, 21)
        self.speed = speed
        self.direction = direction
        self.health = 40

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
    
    def die(self):
        if self.health <= 0:
            return True
        
    def kill(self):
        self.rect.x += 1000
        self.rect.y += 1000

class Door():
    def __init__(self, position, level):
        self.rect = pygame.Rect(position[0], position[1], 32, 32)
        self.image = assetLibrary['door']
        self.level = level

    def onChangeMap(self):
        if self.rect.colliderect(player.rect):
            if self.level == "1":
                if inventory.keyIsAvailable('key1'):
                    global level_1
                    level_1 = "finish"
                    player.state = "finish1"
            elif self.level == "2":
                if inventory.keyIsAvailable('key2'):
                    global level_2
                    level_2 = "finish"
                    player.state = "finish2"
            elif self.level == "3":
                global level_3
                level_3 = "finish"

class Key:
    def __init__(self, position, level):
        self.rect = pygame.Rect(position[0], position[1], 32, 32)
        self.image = pygame.transform.scale(assetLibrary['key'], (25, 25))
        self.level = level
    
    def checkKey(self):
        """Check if player collides key"""
        if self.rect.colliderect(player.rect):
            inventory.collectKey(self.level)
            self.rect.x += 1000

class Enemy_bullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

class Boss:
    def __init__(self, pos_x, pos_y, image_r, image_l, rect_x, rect_y):
        monster_list.append(self)
        self.direction = 1
        self.image = assetLibrary[image_l]
        self.imageL = image_l
        self.imageR = image_r
        self.rect = pygame.Rect(pos_x, pos_y, rect_x, rect_y)
        self.health = 100
                   
global player
player = Character(32, 370)
inventory = Inventory(player)
